import os
import time
import json
from django.core.management.base import BaseCommand
from courses.models import Topic
import google.generativeai as genai

class Command(BaseCommand):
    help = 'Iterates over topics with a video file, uploads the video to Gemini to generate an MCQ quiz, and saves it to predefined_quiz.'

    def handle(self, *args, **options):
        from dotenv import load_dotenv
        
        # Look specifically in the project root for the .env
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), '.env')
        load_dotenv(env_path)
        
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY not found in environment variables.'))
            return

        genai.configure(api_key=api_key)
        
        # We use a 1.5 flash model to process video efficiently and cheaply
        model = genai.GenerativeModel('gemini-2.5-flash') 

        topics = Topic.objects.filter(video_file__isnull=False).exclude(video_file='')

        for topic in topics:
            if topic.predefined_quiz:
                self.stdout.write(self.style.SUCCESS(f'Skipping "{topic.title}" - predefined quiz already exists.'))
                continue

            self.stdout.write(f'--- Processing Video for: {topic.title} ---')
            video_path = topic.video_file.path

            if not os.path.exists(video_path):
                self.stderr.write(self.style.WARNING(f'File not found at {video_path}'))
                continue

            self.stdout.write(f'Uploading video: {os.path.basename(video_path)}...')
            
            try:
                # 1. Upload the file to Gemini API
                video_file = genai.upload_file(path=video_path)

                # 2. Poll until it processes
                self.stdout.write('Waiting for video processing...')
                while video_file.state.name == "PROCESSING":
                    self.stdout.write('.', ending='')
                    time.sleep(5)
                    video_file = genai.get_file(video_file.name)
                
                self.stdout.write('') # Newline after dots
                
                if video_file.state.name == "FAILED":
                    self.stderr.write(self.style.ERROR(f"Video processing failed for {topic.title}."))
                    continue

                # 3. Prompt Gemini with the Video object
                self.stdout.write('Analyzing video and generating quiz...')
                course_title = topic.course.title if topic.course else "programming"
                prompt = f"""
You are an expert programming tutor for the course "{course_title}".
Watch the provided video very carefully. Based ONLY on the concepts taught and explained in this specific video about "{topic.title}", create a 5-question multiple choice quiz.

Return the result EXACTLY as a JSON array of objects. Do not include markdown formatting, markdown backticks, or the word "json" in your response. Just output the raw JSON array.

Format strictly like this example:
[
  {{
    "id": 1,
    "question": "Based on the video, what does Python use to indicate a block of code?",
    "options": ["Curly braces", "Indentation", "Parentheses", "Keywords"],
    "correct": 1
  }}
]
Important: "correct" field must be an integer (0 to 3) representing the index of the correct option in the "options" array.
"""
                response = model.generate_content([prompt, video_file], request_options={"timeout": 600})
                
                # Clean up JSON formatting artifacts
                text = response.text.replace("```json", "").replace("```", "").strip()
                questions = json.loads(text)
                
                if isinstance(questions, list) and len(questions) > 0:
                    topic.predefined_quiz = questions[:5]
                    topic.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully generated and saved quiz for "{topic.title}"!'))
                else:
                    self.stderr.write(self.style.ERROR(f'Invalid JSON format returned for "{topic.title}".'))
                    
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error processing "{topic.title}": {str(e)}'))
                
            finally:
                # 4. Cleanup the File from Gemini storage to prevent quota limits
                if 'video_file' in locals():
                    try:
                        genai.delete_file(video_file.name)
                        self.stdout.write(f'Cleaned up Gemini temporary file: {video_file.name}')
                    except Exception as e:
                        pass # Ignore deletion errors to keep loop going

        self.stdout.write(self.style.SUCCESS('\nFinished processing all videos! The fallback system is fully primed.'))
