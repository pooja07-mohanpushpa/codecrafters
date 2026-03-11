import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pathmind.settings')
django.setup()

from courses.models import Topic

data = [
    {
        "title": "Introduction",
        "questions": [
            {"question": "What is Python primarily known for?", "options": ["Low-level programming", "Readability and simplicity", "Hardware programming", "Mobile-only development"], "correct": 1},
            {"question": "Which of the following is used to run a Python script from the command line?", "options": ["run filename.py", "python filename.py", "execute filename.py", "start filename.py"], "correct": 1},
            {"question": "Python is an example of which type of programming language?", "options": ["Compiled only", "Interpreted", "Assembly", "Machine language"], "correct": 1},
            {"question": "Which file extension is used for Python files?", "options": [".pt", ".py", ".pyt", ".python"], "correct": 1},
            {"question": "Who created Python?", "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"], "correct": 1}
        ]
    },
    {
        "title": "Variables",
        "questions": [
            {"question": "What is a variable in Python?", "options": ["A constant value", "A storage location for data", "A keyword", "A loop"], "correct": 1},
            {"question": "Which of the following is a valid variable name?", "options": ["2value", "value_1", "value-1", "class"], "correct": 1},
            {"question": "Variables in Python are declared using:", "options": ["var keyword", "int keyword", "Assignment operator", "define keyword"], "correct": 2},
            {"question": "What will be the output?\nx = 5\nprint(x)", "options": ["x", "5", "error", "none"], "correct": 1},
            {"question": "Python variables are:", "options": ["Statically typed", "Dynamically typed", "Not typed", "Fixed typed"], "correct": 1}
        ]
    },
    {
        "title": "Data Types",
        "questions": [
            {"question": "Which of the following is a numeric data type?", "options": ["int", "list", "dict", "set"], "correct": 0},
            {"question": "Which data type is used for text?", "options": ["int", "float", "str", "bool"], "correct": 2},
            {"question": "Which function is used to check the data type of a variable?", "options": ["check()", "typeof()", "type()", "datatype()"], "correct": 2},
            {"question": "True or False values belong to which data type?", "options": ["bool", "str", "float", "list"], "correct": 0},
            {"question": "Which of these is a floating point number?", "options": ["10", "10.5", "\"10.5\"", "True"], "correct": 1}
        ]
    },
    {
        "title": "Type Casting",
        "questions": [
            {"question": "What is type casting?", "options": ["Converting one data type to another", "Creating variables", "Deleting variables", "Sorting data"], "correct": 0},
            {"question": "Which function converts a value to integer?", "options": ["str()", "int()", "float()", "bool()"], "correct": 1},
            {"question": "What will be the output?\nint(\"10\")", "options": ["\"10\"", "10", "error", "none"], "correct": 1},
            {"question": "Which function converts number to string?", "options": ["str()", "int()", "float()", "bool()"], "correct": 0},
            {"question": "Which conversion is valid?", "options": ["int(\"5\")", "int(\"hello\")", "int(\"5.5\")", "int(True, False)"], "correct": 0}
        ]
    },
    {
        "title": "Input and Output",
        "questions": [
            {"question": "Which function is used to take input from the user?", "options": ["print()", "scan()", "input()", "read()"], "correct": 2},
            {"question": "Which function displays output on the screen?", "options": ["display()", "show()", "print()", "output()"], "correct": 2},
            {"question": "What is the default data type returned by input()?", "options": ["int", "float", "string", "bool"], "correct": 2},
            {"question": "What will this code print?\nprint(\"Hello Python\")", "options": ["Error", "Hello Python", "python", "none"], "correct": 1},
            {"question": "Which is correct syntax?", "options": ["input \"Enter number\"", "input(\"Enter number\")", "scan(\"Enter number\")", "read(\"Enter number\")"], "correct": 1}
        ]
    },
    {
        "title": "Arithmetic and Comparison Operators",
        "questions": [
            {"question": "Which operator is used for addition?", "options": ["+", "-", "*", "/"], "correct": 0},
            {"question": "Which operator checks equality?", "options": ["=", "==", "!=", ">="], "correct": 1},
            {"question": "What is the result of 10 % 3?", "options": ["3", "1", "0", "2"], "correct": 1},
            {"question": "Which operator is used for exponentiation?", "options": ["^", "**", "^^", "exp"], "correct": 1},
            {"question": "Which operator means 'not equal'?", "options": ["!=", "<>", "==", "="], "correct": 0}
        ]
    },
    {
        "title": "Logical and Assignment Operators",
        "questions": [
            {"question": "Which operator represents logical AND?", "options": ["&&", "and", "&", "&&&"], "correct": 1},
            {"question": "Which operator represents logical OR?", "options": ["or", "||", "|", "both a and b"], "correct": 0},
            {"question": "What does += do?", "options": ["Subtracts value", "Adds and assigns value", "Divides value", "Multiplies value"], "correct": 1},
            {"question": "Which operator assigns value?", "options": ["==", "=", "!=", "<="], "correct": 1},
            {"question": "Which logical operator reverses a condition?", "options": ["not", "and", "or", "xor"], "correct": 0}
        ]
    },
    {
        "title": "Control Flow (if, elif, else)",
        "questions": [
            {"question": "Which keyword starts a conditional statement?", "options": ["for", "if", "switch", "loop"], "correct": 1},
            {"question": "Which keyword checks another condition if the first fails?", "options": ["elif", "else", "ifelse", "other"], "correct": 0},
            {"question": "Which block executes if all conditions fail?", "options": ["elif", "else", "if", "end"], "correct": 1},
            {"question": "What symbol ends the condition line?", "options": [";", ":", ".", ","], "correct": 1},
            {"question": "What will be printed?\nif 5 > 3:\n    print(\"Yes\")", "options": ["Yes", "No", "Error", "Nothing"], "correct": 0}
        ]
    },
    {
        "title": "Nested Conditions",
        "questions": [
            {"question": "What is a nested if statement?", "options": ["if inside another if", "loop inside loop", "function inside function", "variable inside variable"], "correct": 0},
            {"question": "Nested conditions are mainly used for:", "options": ["Multiple checks", "Printing values", "Declaring variables", "Input"], "correct": 0},
            {"question": "Which keyword can be nested?", "options": ["if", "elif", "else", "all of these"], "correct": 3},
            {"question": "What is the indentation used for?", "options": ["Styling", "Defining blocks", "Speed", "Variables"], "correct": 1},
            {"question": "Python uses how many spaces typically for indentation?", "options": ["1", "2", "4", "8"], "correct": 2}
        ]
    },
    {
        "title": "For Loops",
        "questions": [
            {"question": "Which keyword is used for iteration over a sequence?", "options": ["while", "for", "loop", "iterate"], "correct": 1},
            {"question": "Which function generates a sequence of numbers?", "options": ["list()", "range()", "seq()", "loop()"], "correct": 1},
            {"question": "What will this print?\nfor i in range(3):\n    print(i)", "options": ["0 1 2", "1 2 3", "0 1 2 3", "error"], "correct": 0},
            {"question": "A for loop is used for:", "options": ["Conditional execution", "Iteration", "Error handling", "File reading"], "correct": 1},
            {"question": "range(5) produces how many numbers?", "options": ["4", "5", "6", "infinite"], "correct": 1}
        ]
    },
    {
        "title": "While Loops",
        "questions": [
            {"question": "A while loop runs until:", "options": ["program ends", "condition becomes false", "user stops", "memory ends"], "correct": 1},
            {"question": "Which keyword starts a while loop?", "options": ["loop", "repeat", "while", "for"], "correct": 2},
            {"question": "What is needed to avoid infinite loops?", "options": ["indentation", "condition update", "print", "variable"], "correct": 1},
            {"question": "How many times will this loop run?\ni = 0\nwhile i < 3:\n    i += 1", "options": ["2", "3", "4", "infinite"], "correct": 1},
            {"question": "While loop checks condition:", "options": ["before execution", "after execution", "during execution", "none"], "correct": 0}
        ]
    },
    {
        "title": "Loop Control Statements (break, continue, pass)",
        "questions": [
            {"question": "Which statement exits a loop immediately?", "options": ["stop", "break", "continue", "pass"], "correct": 1},
            {"question": "Which statement skips current iteration?", "options": ["pass", "continue", "break", "stop"], "correct": 1},
            {"question": "What does pass do?", "options": ["stops program", "does nothing", "repeats loop", "deletes loop"], "correct": 1},
            {"question": "break is used inside:", "options": ["loops", "functions", "variables", "lists"], "correct": 0},
            {"question": "continue moves control to:", "options": ["next iteration", "previous iteration", "program start", "loop end"], "correct": 0}
        ]
    },
    {
        "title": "Lists",
        "questions": [
            {"question": "Which brackets define a list?", "options": ["()", "[]", "{}", "<>"], "correct": 1},
            {"question": "Lists are:", "options": ["immutable", "mutable", "fixed", "static"], "correct": 1},
            {"question": "Which method adds element to list?", "options": ["add()", "append()", "insertItem()", "push()"], "correct": 1},
            {"question": "Output?\na = [1,2,3]\nprint(a[0])", "options": ["0", "1", "2", "error"], "correct": 1},
            {"question": "Lists can store:", "options": ["single type only", "multiple types", "numbers only", "strings only"], "correct": 1}
        ]
    },
    {
        "title": "Tuples",
        "questions": [
            {"question": "Tuples are created using:", "options": ["[]", "{}", "()", "<>"], "correct": 2},
            {"question": "Tuples are:", "options": ["mutable", "immutable", "dynamic", "temporary"], "correct": 1},
            {"question": "Example: t = (1,2,3). This is:", "options": ["list", "tuple", "set", "dictionary"], "correct": 1},
            {"question": "Which is faster generally?", "options": ["list", "tuple", "dictionary", "set"], "correct": 1},
            {"question": "Can tuple elements be modified?", "options": ["yes", "no", "sometimes", "only integers"], "correct": 1}
        ]
    },
    {
        "title": "Sets",
        "questions": [
            {"question": "Sets are defined using:", "options": ["[]", "()", "{}", "<>"], "correct": 2},
            {"question": "Sets store:", "options": ["duplicate values", "unique values", "ordered values", "indexed values"], "correct": 1},
            {"question": "Which method adds element to set?", "options": ["append()", "add()", "insert()", "push()"], "correct": 1},
            {"question": "Sets are:", "options": ["ordered", "unordered", "indexed", "sorted"], "correct": 1},
            {"question": "Result of {1,1,2,2}?", "options": ["{1,1,2,2}", "{1,2}", "error", "none"], "correct": 1}
        ]
    },
    {
        "title": "Dictionaries",
        "questions": [
            {"question": "Dictionaries store data as:", "options": ["pairs", "keys and values", "arrays", "indexes"], "correct": 1},
            {"question": "Which syntax creates dictionary?", "options": ["[]", "{}", "()", "<>"], "correct": 1},
            {"question": "In d = {'a':1}, 'a' is:", "options": ["value", "key", "list", "index"], "correct": 1},
            {"question": "Access value using:", "options": ["key", "index", "number", "loop"], "correct": 0},
            {"question": "Which method gets all keys?", "options": ["keys()", "getkeys()", "keylist()", "allkeys()"], "correct": 0}
        ]
    },
    {
        "title": "Functions",
        "questions": [
            {"question": "Which keyword defines a function?", "options": ["func", "define", "def", "function"], "correct": 2},
            {"question": "Functions help in:", "options": ["repeating code", "organizing code", "reusability", "all of these"], "correct": 3},
            {"question": "Which statement returns value from function?", "options": ["output", "return", "break", "print"], "correct": 1},
            {"question": "def add(a,b): return a+b returns:", "options": ["subtraction", "multiplication", "addition", "division"], "correct": 2},
            {"question": "Functions are called using:", "options": ["name()", "call()", "run()", "exec()"], "correct": 0}
        ]
    },
    {
        "title": "Strings",
        "questions": [
            {"question": "Strings are enclosed in:", "options": ["quotes", "brackets", "braces", "none"], "correct": 0},
            {"question": "Strings are:", "options": ["mutable", "immutable", "dynamic", "flexible"], "correct": 1},
            {"question": "Which method converts string to lowercase?", "options": ["lower()", "small()", "case()", "down()"], "correct": 0},
            {"question": "Output of 'Hello'[0]?", "options": ["H", "e", "Hello", "error"], "correct": 0},
            {"question": "Strings support:", "options": ["indexing", "slicing", "concatenation", "all of these"], "correct": 3}
        ]
    },
    {
        "title": "File Handling",
        "questions": [
            {"question": "Which function opens a file?", "options": ["open()", "file()", "read()", "start()"], "correct": 0},
            {"question": "Which mode reads file?", "options": ["w", "r", "a", "x"], "correct": 1},
            {"question": "Which method reads entire file?", "options": ["read()", "readfile()", "get()", "load()"], "correct": 0},
            {"question": "Which mode appends data?", "options": ["r", "w", "a", "x"], "correct": 2},
            {"question": "After file operations, what should be done?", "options": ["close file", "delete file", "rename file", "print file"], "correct": 0}
        ]
    }
]

updated_count = 0
for topic_data in data:
    title_lookup = topic_data['title']
    
    # Precise query matching
    topic = Topic.objects.filter(title=title_lookup, course__title='Python Masterclass').first()
    
    if topic:
        # Give id field
        formatted = []
        for i, q in enumerate(topic_data['questions'], start=1):
            formatted.append({
                "id": i,
                "question": q['question'],
                "options": q['options'],
                "correct": q['correct']
            })
        
        topic.predefined_quiz = formatted
        topic.save()
        updated_count += 1
        print(f"Updated customized quiz for: {topic.title}")
    else:
        print(f"Topic not found: {title_lookup}")

print(f"\nSuccessfully overwrote {updated_count} topics with new custom user quizzes!")
