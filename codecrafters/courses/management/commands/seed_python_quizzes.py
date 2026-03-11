from django.core.management.base import BaseCommand
from courses.models import Topic

class Command(BaseCommand):
    help = 'Seeds 22 AI-Generated Quizzes for the Python Masterclass'

    def handle(self, *args, **options):
        quizzes = {
            "Introduction": [
    {
        "id": 1,
        "question": "What is Python primarily known for?",
        "options": [
            "Low-level programming",
            "Readability and simplicity",
            "Hardware programming",
            "Mobile-only development"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which of the following is used to run a Python script from the command line?",
        "options": [
            "run filename.py",
            "python filename.py",
            "execute filename.py",
            "start filename.py"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Python is an example of which type of programming language?",
        "options": [
            "Compiled only",
            "Interpreted",
            "Assembly",
            "Machine language"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Which file extension is used for Python files?",
        "options": [
            ".pt",
            ".py",
            ".pyt",
            ".python"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Who created Python?",
        "options": [
            "James Gosling",
            "Guido van Rossum",
            "Dennis Ritchie",
            "Bjarne Stroustrup"
        ],
        "correct": 1
    }
],
            "Variables": [
    {
        "id": 1,
        "question": "What is a variable in Python?",
        "options": [
            "A constant value",
            "A storage location for data",
            "A keyword",
            "A loop"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which of the following is a valid variable name?",
        "options": [
            "2value",
            "value_1",
            "value-1",
            "class"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Variables in Python are declared using:",
        "options": [
            "var keyword",
            "int keyword",
            "Assignment operator",
            "define keyword"
        ],
        "correct": 2
    },
    {
        "id": 4,
        "question": "What will be the output?\nx = 5\nprint(x)",
        "options": [
            "x",
            "5",
            "error",
            "none"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Python variables are:",
        "options": [
            "Statically typed",
            "Dynamically typed",
            "Not typed",
            "Fixed typed"
        ],
        "correct": 1
    }
],
            "Data Types": [
    {
        "id": 1,
        "question": "Which of the following is a numeric data type?",
        "options": [
            "int",
            "list",
            "dict",
            "set"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Which data type is used for text?",
        "options": [
            "int",
            "float",
            "str",
            "bool"
        ],
        "correct": 2
    },
    {
        "id": 3,
        "question": "Which function is used to check the data type of a variable?",
        "options": [
            "check()",
            "typeof()",
            "type()",
            "datatype()"
        ],
        "correct": 2
    },
    {
        "id": 4,
        "question": "True or False values belong to which data type?",
        "options": [
            "bool",
            "str",
            "float",
            "list"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "Which of these is a floating point number?",
        "options": [
            "10",
            "10.5",
            "\"10.5\"",
            "True"
        ],
        "correct": 1
    }
],
            "Type Casting": [
    {
        "id": 1,
        "question": "What is type casting?",
        "options": [
            "Converting one data type to another",
            "Creating variables",
            "Deleting variables",
            "Sorting data"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Which function converts a value to integer?",
        "options": [
            "str()",
            "int()",
            "float()",
            "bool()"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "What will be the output?\nint(\"10\")",
        "options": [
            "\"10\"",
            "10",
            "error",
            "none"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Which function converts number to string?",
        "options": [
            "str()",
            "int()",
            "float()",
            "bool()"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "Which conversion is valid?",
        "options": [
            "int(\"5\")",
            "int(\"hello\")",
            "int(\"5.5\")",
            "int(True, False)"
        ],
        "correct": 0
    }
],
            "Input and Output": [
    {
        "id": 1,
        "question": "Which function is used to take input from the user?",
        "options": [
            "print()",
            "scan()",
            "input()",
            "read()"
        ],
        "correct": 2
    },
    {
        "id": 2,
        "question": "Which function displays output on the screen?",
        "options": [
            "display()",
            "show()",
            "print()",
            "output()"
        ],
        "correct": 2
    },
    {
        "id": 3,
        "question": "What is the default data type returned by input()?",
        "options": [
            "int",
            "float",
            "string",
            "bool"
        ],
        "correct": 2
    },
    {
        "id": 4,
        "question": "What will this code print?\nprint(\"Hello Python\")",
        "options": [
            "Error",
            "Hello Python",
            "python",
            "none"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Which is correct syntax?",
        "options": [
            "input \"Enter number\"",
            "input(\"Enter number\")",
            "scan(\"Enter number\")",
            "read(\"Enter number\")"
        ],
        "correct": 1
    }
],
            "Arithmetic and Comparison Operators": [
    {
        "id": 1,
        "question": "Which operator is used for addition?",
        "options": [
            "+",
            "-",
            "*",
            "/"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Which operator checks equality?",
        "options": [
            "=",
            "==",
            "!=",
            ">="
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "What is the result of 10 % 3?",
        "options": [
            "3",
            "1",
            "0",
            "2"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Which operator is used for exponentiation?",
        "options": [
            "^",
            "**",
            "^^",
            "exp"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Which operator means 'not equal'?",
        "options": [
            "!=",
            "<>",
            "==",
            "="
        ],
        "correct": 0
    }
],
            "Logical and Assignment Operators": [
    {
        "id": 1,
        "question": "Which operator represents logical AND?",
        "options": [
            "&&",
            "and",
            "&",
            "&&&"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which operator represents logical OR?",
        "options": [
            "or",
            "||",
            "|",
            "both a and b"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "What does += do?",
        "options": [
            "Subtracts value",
            "Adds and assigns value",
            "Divides value",
            "Multiplies value"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Which operator assigns value?",
        "options": [
            "==",
            "=",
            "!=",
            "<="
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Which logical operator reverses a condition?",
        "options": [
            "not",
            "and",
            "or",
            "xor"
        ],
        "correct": 0
    }
],
            "Control Flow (if, elif, else)": [
    {
        "id": 1,
        "question": "Which keyword starts a conditional statement?",
        "options": [
            "for",
            "if",
            "switch",
            "loop"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which keyword checks another condition if the first fails?",
        "options": [
            "elif",
            "else",
            "ifelse",
            "other"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "Which block executes if all conditions fail?",
        "options": [
            "elif",
            "else",
            "if",
            "end"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "What symbol ends the condition line?",
        "options": [
            ";",
            ":",
            ".",
            ","
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "What will be printed?\nif 5 > 3:\n    print(\"Yes\")",
        "options": [
            "Yes",
            "No",
            "Error",
            "Nothing"
        ],
        "correct": 0
    }
],
            "Nested Conditions": [
    {
        "id": 1,
        "question": "What is a nested if statement?",
        "options": [
            "if inside another if",
            "loop inside loop",
            "function inside function",
            "variable inside variable"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Nested conditions are mainly used for:",
        "options": [
            "Multiple checks",
            "Printing values",
            "Declaring variables",
            "Input"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "Which keyword can be nested?",
        "options": [
            "if",
            "elif",
            "else",
            "all of these"
        ],
        "correct": 3
    },
    {
        "id": 4,
        "question": "What is the indentation used for?",
        "options": [
            "Styling",
            "Defining blocks",
            "Speed",
            "Variables"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Python uses how many spaces typically for indentation?",
        "options": [
            "1",
            "2",
            "4",
            "8"
        ],
        "correct": 2
    }
],
            "For Loops": [
    {
        "id": 1,
        "question": "Which keyword is used for iteration over a sequence?",
        "options": [
            "while",
            "for",
            "loop",
            "iterate"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which function generates a sequence of numbers?",
        "options": [
            "list()",
            "range()",
            "seq()",
            "loop()"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "What will this print?\nfor i in range(3):\n    print(i)",
        "options": [
            "0 1 2",
            "1 2 3",
            "0 1 2 3",
            "error"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "A for loop is used for:",
        "options": [
            "Conditional execution",
            "Iteration",
            "Error handling",
            "File reading"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "range(5) produces how many numbers?",
        "options": [
            "4",
            "5",
            "6",
            "infinite"
        ],
        "correct": 1
    }
],
            "While Loops": [
    {
        "id": 1,
        "question": "A while loop runs until:",
        "options": [
            "program ends",
            "condition becomes false",
            "user stops",
            "memory ends"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which keyword starts a while loop?",
        "options": [
            "loop",
            "repeat",
            "while",
            "for"
        ],
        "correct": 2
    },
    {
        "id": 3,
        "question": "What is needed to avoid infinite loops?",
        "options": [
            "indentation",
            "condition update",
            "print",
            "variable"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "How many times will this loop run?\ni = 0\nwhile i < 3:\n    i += 1",
        "options": [
            "2",
            "3",
            "4",
            "infinite"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "While loop checks condition:",
        "options": [
            "before execution",
            "after execution",
            "during execution",
            "none"
        ],
        "correct": 0
    }
],
            "Loop Control Statements (break, continue, pass)": [
    {
        "id": 1,
        "question": "Which statement exits a loop immediately?",
        "options": [
            "stop",
            "break",
            "continue",
            "pass"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which statement skips current iteration?",
        "options": [
            "pass",
            "continue",
            "break",
            "stop"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "What does pass do?",
        "options": [
            "stops program",
            "does nothing",
            "repeats loop",
            "deletes loop"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "break is used inside:",
        "options": [
            "loops",
            "functions",
            "variables",
            "lists"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "continue moves control to:",
        "options": [
            "next iteration",
            "previous iteration",
            "program start",
            "loop end"
        ],
        "correct": 0
    }
],
            "Lists": [
    {
        "id": 1,
        "question": "Which brackets define a list?",
        "options": [
            "()",
            "[]",
            "{}",
            "<>"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Lists are:",
        "options": [
            "immutable",
            "mutable",
            "fixed",
            "static"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Which method adds element to list?",
        "options": [
            "add()",
            "append()",
            "insertItem()",
            "push()"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Output?\na = [1,2,3]\nprint(a[0])",
        "options": [
            "0",
            "1",
            "2",
            "error"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Lists can store:",
        "options": [
            "single type only",
            "multiple types",
            "numbers only",
            "strings only"
        ],
        "correct": 1
    }
],
            "Tuples": [
    {
        "id": 1,
        "question": "Tuples are created using:",
        "options": [
            "[]",
            "{}",
            "()",
            "<>"
        ],
        "correct": 2
    },
    {
        "id": 2,
        "question": "Tuples are:",
        "options": [
            "mutable",
            "immutable",
            "dynamic",
            "temporary"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Example: t = (1,2,3). This is:",
        "options": [
            "list",
            "tuple",
            "set",
            "dictionary"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Which is faster generally?",
        "options": [
            "list",
            "tuple",
            "dictionary",
            "set"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Can tuple elements be modified?",
        "options": [
            "yes",
            "no",
            "sometimes",
            "only integers"
        ],
        "correct": 1
    }
],
            "Sets": [
    {
        "id": 1,
        "question": "Sets are defined using:",
        "options": [
            "[]",
            "()",
            "{}",
            "<>"
        ],
        "correct": 2
    },
    {
        "id": 2,
        "question": "Sets store:",
        "options": [
            "duplicate values",
            "unique values",
            "ordered values",
            "indexed values"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Which method adds element to set?",
        "options": [
            "append()",
            "add()",
            "insert()",
            "push()"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Sets are:",
        "options": [
            "ordered",
            "unordered",
            "indexed",
            "sorted"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Result of {1,1,2,2}?",
        "options": [
            "{1,1,2,2}",
            "{1,2}",
            "error",
            "none"
        ],
        "correct": 1
    }
],
            "Dictionaries": [
    {
        "id": 1,
        "question": "Dictionaries store data as:",
        "options": [
            "pairs",
            "keys and values",
            "arrays",
            "indexes"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which syntax creates dictionary?",
        "options": [
            "[]",
            "{}",
            "()",
            "<>"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "In d = {'a':1}, 'a' is:",
        "options": [
            "value",
            "key",
            "list",
            "index"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Access value using:",
        "options": [
            "key",
            "index",
            "number",
            "loop"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "Which method gets all keys?",
        "options": [
            "keys()",
            "getkeys()",
            "keylist()",
            "allkeys()"
        ],
        "correct": 0
    }
],
            "Functions": [
    {
        "id": 1,
        "question": "Which keyword defines a function?",
        "options": [
            "func",
            "define",
            "def",
            "function"
        ],
        "correct": 2
    },
    {
        "id": 2,
        "question": "Functions help in:",
        "options": [
            "repeating code",
            "organizing code",
            "reusability",
            "all of these"
        ],
        "correct": 3
    },
    {
        "id": 3,
        "question": "Which statement returns value from function?",
        "options": [
            "output",
            "return",
            "break",
            "print"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "def add(a,b): return a+b returns:",
        "options": [
            "subtraction",
            "multiplication",
            "addition",
            "division"
        ],
        "correct": 2
    },
    {
        "id": 5,
        "question": "Functions are called using:",
        "options": [
            "name()",
            "call()",
            "run()",
            "exec()"
        ],
        "correct": 0
    }
],
            "Strings": [
    {
        "id": 1,
        "question": "Strings are enclosed in:",
        "options": [
            "quotes",
            "brackets",
            "braces",
            "none"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Strings are:",
        "options": [
            "mutable",
            "immutable",
            "dynamic",
            "flexible"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Which method converts string to lowercase?",
        "options": [
            "lower()",
            "small()",
            "case()",
            "down()"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "Output of 'Hello'[0]?",
        "options": [
            "H",
            "e",
            "Hello",
            "error"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "Strings support:",
        "options": [
            "indexing",
            "slicing",
            "concatenation",
            "all of these"
        ],
        "correct": 3
    }
],
            "File Handling": [
    {
        "id": 1,
        "question": "Which function opens a file?",
        "options": [
            "open()",
            "file()",
            "read()",
            "start()"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Which mode reads file?",
        "options": [
            "w",
            "r",
            "a",
            "x"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Which method reads entire file?",
        "options": [
            "read()",
            "readfile()",
            "get()",
            "load()"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "Which mode appends data?",
        "options": [
            "r",
            "w",
            "a",
            "x"
        ],
        "correct": 2
    },
    {
        "id": 5,
        "question": "After file operations, what should be done?",
        "options": [
            "close file",
            "delete file",
            "rename file",
            "print file"
        ],
        "correct": 0
    }
],
            "Exeption Handling": [
    {
        "id": 1,
        "question": "Based on the video, what is the primary purpose of Exception Handling in Python?",
        "options": [
            "To prevent any errors from ever occurring in a program.",
            "To write cleaner, more elegant code by avoiding error checks.",
            "To catch and manage errors during program execution, preventing the application from crashing.",
            "To intentionally stop program execution when an error is detected."
        ],
        "correct": 2
    },
    {
        "id": 2,
        "question": "In a Python `try`/`except` block, where should you place the code that you suspect might fail?",
        "options": [
            "In the `except` block, as a fallback.",
            "After the `except` block, to continue execution.",
            "In the `try` block, to 'try out' the code.",
            "Only in a `finally` block."
        ],
        "correct": 2
    },
    {
        "id": 3,
        "question": "The video compares different ways of catching exceptions to using a net. What does a \"broad except statement with nothing after it\" (e.g., `except:`) represent?",
        "options": [
            "A specialized tool that only catches specific types of errors.",
            "A net that lets all errors fall through, causing the program to crash.",
            "A giant, clumsy net that catches anything but gives no information about what it caught.",
            "A perfectly sized net that catches only the errors you anticipate."
        ],
        "correct": 2
    },
    {
        "id": 4,
        "question": "According to the video, which specific Python exception type is raised when a program expects a number but the user inputs text (e.g., \"ten\")?",
        "options": [
            "TypeError",
            "IndexError",
            "ZeroDivisionError",
            "ValueError"
        ],
        "correct": 3
    },
    {
        "id": 5,
        "question": "How does the video demonstrate accessing the specific error message generated by Python after an exception is caught?",
        "options": [
            "By using the `as` keyword to store the exception object in a variable and then printing that variable.",
            "By calling a generic `get_error_message()` function provided by Python.",
            "By manually inspecting the traceback in the terminal without using the `except` block.",
            "By adding a comment in the `except` block describing the expected error."
        ],
        "correct": 0
    }
],
            "OOP1": [
    {
        "id": 1,
        "question": "According to the video, what is Object-Oriented Programming (OOP) primarily a paradigm for?",
        "options": [
            "Organizing software design around functions and logic.",
            "Developing machine learning algorithms.",
            "Organizing software design around data, or objects.",
            "Optimizing database queries."
        ],
        "correct": 2
    },
    {
        "id": 2,
        "question": "The video defines a 'Class' as which of the following?",
        "options": [
            "A specific instance of data.",
            "A blueprint or a template for creating objects.",
            "A self-contained bundle of instructions.",
            "A method for handling errors."
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Based on the car analogy used in the video, if 'Car' is a class, what would a 'Tesla Model 3' represent?",
        "options": [
            "A blueprint for a car.",
            "A constructor method.",
            "An object, which is an instance of the class.",
            "A programming function."
        ],
        "correct": 2
    },
    {
        "id": 4,
        "question": "In Python, what is the name of the special method used as a constructor to initialize an object's attributes when it's created?",
        "options": [
            "__start__",
            "__create__",
            "__build__",
            "__init__"
        ],
        "correct": 3
    },
    {
        "id": 5,
        "question": "What is the primary job of a constructor, as explained in the video?",
        "options": [
            "To destroy an object when it's no longer needed.",
            "To perform calculations within an object.",
            "To initialize an object's attributes when it's created.",
            "To define the object's methods."
        ],
        "correct": 2
    }
],
            "OOP2": [
    {
        "id": 1,
        "question": "According to the video, what does \"encapsulation\" in object-oriented programming refer to?",
        "options": [
            "The ability of an object to take on many forms.",
            "Hiding the complex internal details of an object.",
            "Bundling data and the methods that operate on that data into a single unit, or class.",
            "Allowing a new class to inherit properties from an existing class."
        ],
        "correct": 2
    },
    {
        "id": 2,
        "question": "The second pillar of OOP discussed, \"inheritance,\" is primarily used for what purpose?",
        "options": [
            "To create methods with the same name but different implementations across classes.",
            "To bundle an object's data and methods into a single, secure unit.",
            "To hide an object's internal complexity and expose only essential features.",
            "To allow a new class (child) to reuse attributes and methods from an existing class (parent)."
        ],
        "correct": 3
    },
    {
        "id": 3,
        "question": "How does \"polymorphism\" contribute to flexible and dynamic code, as explained in the video?",
        "options": [
            "It strictly enforces that all classes must have unique method names.",
            "It enables different classes to have methods with the same name but distinct implementations.",
            "It automatically organizes all variables and functions globally, making them universally accessible.",
            "It prevents any external part of the program from directly altering an object's data."
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "The video explains \"abstraction\" as analogous to a TV remote control. What is the core idea behind abstraction in this context?",
        "options": [
            "Exposing all internal circuits and signals for complete control.",
            "Allowing objects to take on multiple forms based on their type.",
            "Hiding complex internal logic and showing only the necessary parts of an object.",
            "Bundling an object's data with its related actions."
        ],
        "correct": 2
    },
    {
        "id": 5,
        "question": "Which of the following is NOT presented as a benefit of applying the four pillars of OOP in Python?",
        "options": [
            "Making code organized and maintainable.",
            "Enabling code reusability and scalability.",
            "Eliminating the need for any variables in a program.",
            "Creating flexible and dynamic software solutions."
        ],
        "correct": 2
    }
],
        }

        count = 0
        for title, quiz in quizzes.items():
            topic = Topic.objects.filter(title=title, course__title='Python Masterclass').first()
            if topic:
                topic.predefined_quiz = quiz
                topic.save()
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully re-seeded {count} Python Masterclass quizzes!'))
