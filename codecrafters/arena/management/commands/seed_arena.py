from django.core.management.base import BaseCommand
from arena.models import CodingProblem, TestCase
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds initial coding problems into the database.'

    def handle(self, *args, **kwargs):
        problems = [
            {
                'title': 'Two Sum',
                'difficulty': 'Easy',
                'description': 'Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution.',
                'example_input': 'nums = [2,7,11,15], target = 9',
                'example_output': '[0, 1]',
                'constraints': '2 <= nums.length <= 10^4\n-10^9 <= nums[i] <= 10^9',
                'points_reward': 100,
                'test_cases': [
                    {'input': '[2,7,11,15]\n9', 'output': '[0, 1]'},
                    {'input': '[3,2,4]\n6', 'output': '[1, 2]'},
                    {'input': '[3,3]\n6', 'output': '[0, 1]'},
                ]
            },
            {
                'title': 'Palindrome Number',
                'difficulty': 'Easy',
                'description': 'Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.',
                'example_input': 'x = 121',
                'example_output': 'true',
                'constraints': '-2^31 <= x <= 2^31 - 1',
                'points_reward': 80,
                'test_cases': [
                    {'input': '121', 'output': 'true'},
                    {'input': '-121', 'output': 'false'},
                    {'input': '10', 'output': 'false'},
                ]
            },
            {
                'title': 'Reverse String',
                'difficulty': 'Easy',
                'description': 'Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.',
                'example_input': 's = ["h","e","l","l","o"]',
                'example_output': '["o","l","l","e","h"]',
                'constraints': '1 <= s.length <= 10^5',
                'points_reward': 50,
                'test_cases': [
                    {'input': '["h","e","l","l","o"]', 'output': '["o","l","l","e","h"]'},
                    {'input': '["H","a","n","n","a","h"]', 'output': '["h","a","n","n","a","H"]'},
                ]
            }
        ]

        self.stdout.write('Seeding problems...')
        for p_data in problems:
            prob, created = CodingProblem.objects.get_or_create(
                slug=slugify(p_data['title']),
                defaults={
                    'title': p_data['title'],
                    'difficulty': p_data['difficulty'],
                    'description': p_data['description'],
                    'example_input': p_data['example_input'],
                    'example_output': p_data['example_output'],
                    'constraints': p_data['constraints'],
                    'points_reward': p_data['points_reward'],
                }
            )
            if created:
                self.stdout.write(f"Created problem: {prob.title}")
                for tc in p_data['test_cases']:
                    TestCase.objects.create(
                        problem=prob,
                        input_data=tc['input'],
                        expected_output=tc['output']
                    )
            else:
                self.stdout.write(f"Problem already exists: {prob.title}")

        self.stdout.write(self.style.SUCCESS('Successfully seeded arena problems.'))
