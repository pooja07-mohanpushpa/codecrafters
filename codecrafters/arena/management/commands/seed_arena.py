from django.core.management.base import BaseCommand
from arena.models import CodingProblem, TestCase
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seed the database with 19 Python-specific coding problems matching the Masterclass.'

    def handle(self, *args, **options):
        # Clear existing problems for a clean slate
        CodingProblem.objects.all().delete()
        self.stdout.write('Cleared existing arena challenges.')

        # 19 Problems mapped to the 19 Python Masterclass topics
        problems_data = [
            {
                "title": "1. Hello World (Introduction)",
                "difficulty": "Easy",
                "description": "Welcome to Python! To begin, simply print the exact phrase `Hello, World!` to the console. This verifies that you understand the basic syntax of outputting strings.",
                "example_input": "None",
                "example_output": "Hello, World!",
                "constraints": "Output must match exactly.\nCase-sensitive.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "", "out": "Hello, World!"}
                ]
            },
            {
                "title": "2. Swap Two Variables (Variables)",
                "difficulty": "Easy",
                "description": "Given two input strings on separate lines (e.g. `a` and `b`), print them in reverse order, each on a new line.\n\nInput format:\nLine 1: first string\nLine 2: second string",
                "example_input": "Apple\nBanana",
                "example_output": "Banana\nApple",
                "constraints": "No leading or trailing extra spaces.\nMust be exactly 2 lines of output.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "Apple\nBanana", "out": "Banana\nApple"},
                    {"in": "10\n20", "out": "20\n10"},
                    {"in": "Cat\nDog", "out": "Dog\nCat"}
                ]
            },
            {
                "title": "3. String to Integer Sum (Data Types & Type Casting)",
                "difficulty": "Easy",
                "description": "You are given two numbers, but they are provided as strings on two separate lines. Cast them to integers, add them together, and print the resulting integer.",
                "example_input": "25\n15",
                "example_output": "40",
                "constraints": "The inputs will always be valid integer strings.\nResult must be printed as an integer.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "25\n15", "out": "40"},
                    {"in": "100\n200", "out": "300"},
                    {"in": "-50\n50", "out": "0"}
                ]
            },
            {
                "title": "4. Area of a Rectangle (Input and Operators)",
                "difficulty": "Easy",
                "description": "Given two numbers on separate lines representing the length and width of a rectangle, calculate and print the area.",
                "example_input": "5\n4",
                "example_output": "20",
                "constraints": "Inputs can be floats or integers.\nPrint the result as a number.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "5\n4", "out": "20"},
                    {"in": "10\n10", "out": "100"},
                    {"in": "2.5\n4", "out": "10.0"}
                ]
            },
            {
                "title": "5. Odd or Even (Arithmetic & Comparison)",
                "difficulty": "Easy",
                "description": "Given a single integer, determine if it is Odd or Even. Print `Even` if it is divisible by 2, otherwise print `Odd`.",
                "example_input": "14",
                "example_output": "Even",
                "constraints": "Input is a single valid integer.\nOutput strictly 'Odd' or 'Even'.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "14", "out": "Even"},
                    {"in": "7", "out": "Odd"},
                    {"in": "0", "out": "Even"}
                ]
            },
            {
                "title": "6. Leap Year Checker (Logical & Assignment)",
                "difficulty": "Medium",
                "description": "Given a year (integer), determine if it is a leap year. Print `True` if it is, `False` otherwise.\n\nA year is a leap year if it is divisible by 4, EXCEPT if it is a century year (divisible by 100). However, if the century year is divisible by 400, it IS a leap year.",
                "example_input": "2024",
                "example_output": "True",
                "constraints": "Year >= 1000\nYear <= 9999",
                "points_reward": 100,
                "test_cases": [
                    {"in": "2024", "out": "True"},
                    {"in": "1900", "out": "False"},
                    {"in": "2000", "out": "True"},
                    {"in": "2023", "out": "False"}
                ]
            },
            {
                "title": "7. Grade Calculator (Control Flow)",
                "difficulty": "Medium",
                "description": "Given a student's score (0-100), print their letter grade based on the following scale:\n90-100: A\n80-89: B\n70-79: C\n60-69: D\nBelow 60: F",
                "example_input": "85",
                "example_output": "B",
                "constraints": "Score will be an integer between 0 and 100.",
                "points_reward": 100,
                "test_cases": [
                    {"in": "85", "out": "B"},
                    {"in": "92", "out": "A"},
                    {"in": "79", "out": "C"},
                    {"in": "59", "out": "F"}
                ]
            },
            {
                "title": "8. Largest of Three (Nested Conditions)",
                "difficulty": "Medium",
                "description": "Given three integers separated by commas on a single line, find and print the largest of the three numbers.",
                "example_input": "10,50,25",
                "example_output": "50",
                "constraints": "Input is a comma-separated string of 3 integers.\nOutput the max integer.",
                "points_reward": 100,
                "test_cases": [
                    {"in": "10,50,25", "out": "50"},
                    {"in": "-10,-5,-20", "out": "-5"},
                    {"in": "100,100,100", "out": "100"}
                ]
            },
            {
                "title": "9. Factorial Print (For Loops)",
                "difficulty": "Medium",
                "description": "Given a positive integer N, calculate its factorial (N!) using a loop, and print the result.",
                "example_input": "5",
                "example_output": "120",
                "constraints": "1 <= N <= 20",
                "points_reward": 100,
                "test_cases": [
                    {"in": "5", "out": "120"},
                    {"in": "3", "out": "6"},
                    {"in": "1", "out": "1"}
                ]
            },
            {
                "title": "10. Reverse a String (While Loops)",
                "difficulty": "Easy",
                "description": "Given a string as input, print the exact string reversed.",
                "example_input": "hello",
                "example_output": "olleh",
                "constraints": "String length < 100 characters.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "hello", "out": "olleh"},
                    {"in": "Python", "out": "nohtyP"},
                    {"in": "a", "out": "a"}
                ]
            },
            {
                "title": "11. Find First Prime (Loop Control)",
                "difficulty": "Hard",
                "description": "Given a list of comma-separated integers, iterate through them and print the FIRST prime number you encounter. If there are no prime numbers, print `None`.",
                "example_input": "4,6,8,9,11,15",
                "example_output": "11",
                "constraints": "Numbers > 1\nMax 50 numbers in list.",
                "points_reward": 150,
                "test_cases": [
                    {"in": "4,6,8,9,11,15", "out": "11"},
                    {"in": "4,6,8,10", "out": "None"},
                    {"in": "2,4,6", "out": "2"}
                ]
            },
            {
                "title": "12. Sum of Evens (Lists)",
                "difficulty": "Medium",
                "description": "Given a comma-separated list of integers, find the sum of all EVEN numbers in the list and print the total.",
                "example_input": "1,2,3,4,5,6",
                "example_output": "12",
                "constraints": "List length < 100.",
                "points_reward": 100,
                "test_cases": [
                    {"in": "1,2,3,4,5,6", "out": "12"},
                    {"in": "1,3,5", "out": "0"},
                    {"in": "2,2,2", "out": "6"}
                ]
            },
            {
                "title": "13. Tuple Unpacking (Tuples)",
                "difficulty": "Easy",
                "description": "Given a comma-separated string representing a 3-element tuple (Name, Age, City), extract the Age and City and print them in the format: `[Name] is from [City]`",
                "example_input": "Alice,25,Paris",
                "example_output": "Alice is from Paris",
                "constraints": "Input exactly 3 comma-separated values.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "Alice,25,Paris", "out": "Alice is from Paris"},
                    {"in": "Bob,30,New York", "out": "Bob is from New York"}
                ]
            },
            {
                "title": "14. Unique Visitors (Sets)",
                "difficulty": "Medium",
                "description": "Given a comma-separated list of visitor IDs, find the total number of UNIQUE visitors using a Set. Print the integer count.",
                "example_input": "100,101,100,102,101",
                "example_output": "3",
                "constraints": "List length < 1000.",
                "points_reward": 100,
                "test_cases": [
                    {"in": "100,101,100,102,101", "out": "3"},
                    {"in": "1,1,1,1", "out": "1"},
                    {"in": "1,2,3", "out": "3"}
                ]
            },
            {
                "title": "15. Word Frequency (Dictionaries)",
                "difficulty": "Hard",
                "description": "Given a single string of lowercase words separated by spaces, count the frequency of each unique word. Print the MAXIMUM frequency found (just the integer).",
                "example_input": "apple banana apple orange banana apple",
                "example_output": "3",
                "constraints": "All lowercase, no punctuation.",
                "points_reward": 150,
                "test_cases": [
                    {"in": "apple banana apple orange banana apple", "out": "3"},
                    {"in": "cat dog bird", "out": "1"},
                    {"in": "a a a a b b", "out": "4"}
                ]
            },
            {
                "title": "16. Valid Palindrome (Functions)",
                "difficulty": "Medium",
                "description": "Write a logic to determine if the given string is a palindrome (reads the same forwards and backwards). Print `True` or `False`. Ignore spaces and case.",
                "example_input": "race car",
                "example_output": "True",
                "constraints": "String length < 100.",
                "points_reward": 100,
                "test_cases": [
                    {"in": "race car", "out": "True"},
                    {"in": "Hello", "out": "False"},
                    {"in": "A man a plan a canal Panama", "out": "True"}
                ]
            },
            {
                "title": "17. Vowel Counter (Strings)",
                "difficulty": "Easy",
                "description": "Given a string, count and print the total number of vowels (a, e, i, o, u) present in it. Ignore case.",
                "example_input": "PathMind",
                "example_output": "4",
                "constraints": "Print the integer count.",
                "points_reward": 50,
                "test_cases": [
                    {"in": "PathMind", "out": "4"},
                    {"in": "Python", "out": "1"},
                    {"in": "bcdfg", "out": "0"}
                ]
            },
            {
                "title": "18. Two Sum (Algorithms)",
                "difficulty": "Hard",
                "description": "Given a comma-separated list of integers on line 1, and a target integer on line 2, find the INDICES of the two numbers that add up to the target. Print them as `index1,index2`.",
                "example_input": "2,7,11,15\n9",
                "example_output": "0,1",
                "constraints": "Exactly one valid solution exists.",
                "points_reward": 200,
                "test_cases": [
                    {"in": "2,7,11,15\n9", "out": "0,1"},
                    {"in": "3,2,4\n6", "out": "1,2"},
                    {"in": "3,3\n6", "out": "0,1"}
                ]
            },
            {
                "title": "19. FizzBuzz (Final Challenge)",
                "difficulty": "Medium",
                "description": "Given a single integer N. Iterate from 1 to N. For each number, if it is divisible by 3 and 5 print `FizzBuzz`, if divisible by 3 print `Fizz`, if divisible by 5 print `Buzz`, otherwise print the number. Print everything joined by commas on a single line.",
                "example_input": "15",
                "example_output": "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz",
                "constraints": "1 <= N <= 100",
                "points_reward": 150,
                "test_cases": [
                    {"in": "5", "out": "1,2,Fizz,4,Buzz"},
                    {"in": "15", "out": "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz"}
                ]
            },
            {
                "title": "20. Capstone: Inventory Manager",
                "difficulty": "Hard",
                "description": "Your final Python Masterclass project!\n\nYou must process a set of inventory commands to manage a store's stock. Commands are provided line-by-line until the word `END` is encountered.\n\nCommands:\n- `ADD [Item] [Qty]` (Add to inventory or create it)\n- `SELL [Item] [Qty]` (Subtract from inventory. If Qty exceeds stock, ignore the command and do nothing)\n\nAt the `END` command, print the final inventory alphabetically by item name in the format:\n`[Item]: [Qty]`",
                "example_input": "ADD Apple 50\nADD Banana 20\nSELL Apple 10\nADD Apple 5\nSELL Banana 25\nEND",
                "example_output": "Apple: 45\nBanana: 20",
                "constraints": "Input ends with `END`.\nItem names are single words.\nDo NOT print items with a quantity of 0 (if any reach 0, they should still be printed as generic 0).\nThe Banana sell of 25 in the example is ignored because stock is 20.",
                "points_reward": 500,
                "test_cases": [
                    {
                        "in": "ADD Apple 50\nADD Banana 20\nSELL Apple 10\nADD Apple 5\nSELL Banana 25\nEND",
                        "out": "Apple: 45\nBanana: 20"
                    },
                    {
                        "in": "ADD Sword 1\nADD Shield 1\nSELL Potion 5\nADD Potion 10\nSELL Sword 1\nEND",
                        "out": "Potion: 10\nShield: 1\nSword: 0"
                    },
                    {
                        "in": "ADD Gold 100\nADD Silver 50\nSELL Gold 100\nEND",
                        "out": "Gold: 0\nSilver: 50"
                    }
                ]
            }
        ]

        for i, data in enumerate(problems_data):
            prob = CodingProblem.objects.create(
                title=data['title'],
                slug=slugify(data['title']),
                difficulty=data['difficulty'],
                description=data['description'],
                example_input=data['example_input'],
                example_output=data['example_output'],
                constraints=data['constraints'],
                points_reward=data['points_reward'],
                order=i+1
            )
            for tc in data['test_cases']:
                TestCase.objects.create(
                    problem=prob,
                    input_data=tc['in'],
                    expected_output=tc['out'],
                    is_hidden=True  # Ensure users can't see the exact outputs via client side tests easily
                )
            
        self.stdout.write(self.style.SUCCESS('Successfully seeded 19 Masterclass Arena topics with TestCases!'))

