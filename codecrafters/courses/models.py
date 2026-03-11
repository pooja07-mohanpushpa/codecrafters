from django.db import models
from django.contrib.auth.models import User
import uuid


class Course(models.Model):
    """
    A learning path (e.g., Python Masterclass, C Foundations).
    """
    title           = models.CharField(max_length=200)
    description     = models.TextField(blank=True)
    icon_url        = models.URLField(blank=True)
    gradient_from   = models.CharField(max_length=60, default='from-blue-500')
    gradient_to     = models.CharField(max_length=60, default='to-indigo-700')
    points_available = models.IntegerField(default=500)
    order           = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def total_topics(self):
        return self.topics.count()


class Topic(models.Model):
    """
    A single lesson inside a Course, ordered to build on each other.
    """
    course      = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    title       = models.CharField(max_length=200)
    order       = models.IntegerField(default=0)
    video_file  = models.FileField(upload_to='topics/videos/', blank=True, null=True,
                                   help_text="Upload the video file (mp4 recommended).")
    video_url   = models.URLField(blank=True, help_text="OR paste an external video URL (YouTube embed, etc.)")
    content     = models.TextField(blank=True, help_text="Lesson text / transcript used by Gemini for quiz generation.")
    points_reward = models.IntegerField(default=50)
    predefined_quiz = models.JSONField(blank=True, null=True, help_text="AI-generated fallback quiz questions.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} — {self.title}"


class UserProgress(models.Model):
    """
    Tracks which topics a user has completed and their quiz score.
    One row per (user, topic) pair.
    """
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    topic           = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='progress')
    is_completed    = models.BooleanField(default=False)
    quiz_score      = models.IntegerField(default=0)
    highest_quiz_score = models.IntegerField(default=0)
    completed_at    = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'topic')

    def __str__(self):
        status = "✅" if self.is_completed else "⏳"
        return f"{status} {self.user.username} — {self.topic.title}"


class CourseProgress(models.Model):
    """
    Tracks a user's overall progress and star badges for a specific course.
    """
    user                = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_progress')
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='user_progress')
    topics_completed    = models.IntegerField(default=0)
    progress_percentage = models.FloatField(default=0.0)
    stars_earned        = models.IntegerField(default=0)
    last_updated        = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.progress_percentage}%)"


class Certificate(models.Model):
    """
    Generated PDF certificates for 100% course completion.
    """
    certificate_id  = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    course          = models.ForeignKey(Course, on_delete=models.CASCADE)
    issue_date      = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cert {self.certificate_id} - {self.user.username} - {self.course.title}"


class Achievement(models.Model):
    """
    Badges that users can earn (e.g., 'Python Pro', '7-Day Streak').
    """
    name            = models.CharField(max_length=100)
    description     = models.TextField()
    icon_url        = models.URLField(blank=True, help_text="Link to achievement icon (e.g., FontAwesome URL or static img)")
    requirement_type = models.CharField(max_length=50, choices=[
        ('points', 'PathPoints Threshold'),
        ('course', 'Course Completion'),
        ('challenge', 'Challenges Solved'),
    ], default='points')
    requirement_value = models.IntegerField(default=0, help_text="Value needed to unlock (e.g., 500 points)")

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    """
    Connects users to the achievements they have unlocked.
    """
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement     = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    unlocked_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f"{self.user.username} unlocked {self.achievement.name}"


class QuizAttempt(models.Model):
    """
    Records a user's attempt at an AI-generated topic quiz.
    """
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    topic           = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quiz_attempts')
    score           = models.IntegerField(default=0) # 0 to 5
    pathpoints_earned = models.IntegerField(default=0)
    attempted_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.topic.title} ({self.score}/5)"
