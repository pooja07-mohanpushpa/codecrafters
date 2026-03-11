from django.core.management.base import BaseCommand
from courses.models import Topic

class Command(BaseCommand):
    help = 'Seeds 19 Quizzes for the C Programming Course'

    def handle(self, *args, **options):
        quizzes = {
            "Introduction to C": [
    {
        "id": 1,
        "question": "Who developed the C programming language?",
        "options": [
            "Dennis Ritchie",
            "Bjarne Stroustrup",
            "James Gosling",
            "Guido van Rossum"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "C language was developed at:",
        "options": [
            "Microsoft",
            "Bell Labs",
            "IBM",
            "Google"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "C is mainly a:",
        "options": [
            "High-level language",
            "Low-level language",
            "Middle-level language",
            "Assembly language"
        ],
        "correct": 2
    },
    {
        "id": 4,
        "question": "Which extension is used for C source files?",
        "options": [
            ".cpp",
            ".c",
            ".java",
            ".py"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Which function is the entry point of a C program?\n---",
        "options": [
            "start()",
            "run()",
            "main()",
            "begin()"
        ],
        "correct": 2
    }
],
            "Variables": [
    {
        "id": 1,
        "question": "A variable is:",
        "options": [
            "Fixed value",
            "Memory location to store data",
            "Keyword",
            "Operator"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which is a valid variable name?",
        "options": [
            "2num",
            "num_1",
            "num-1",
            "int"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Variables must be declared before:",
        "options": [
            "compilation",
            "usage",
            "printing",
            "execution"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Which symbol ends a statement in C?",
        "options": [
            ":",
            ";",
            ",",
            "."
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Example\nint x = 10;\n10 is:\n---",
        "options": [
            "variable",
            "identifier",
            "value",
            "operator"
        ],
        "correct": 2
    }
],
            "Data Types": [
    {
        "id": 1,
        "question": "Which is an integer data type?",
        "options": [
            "int",
            "float",
            "char",
            "double"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Which type stores decimal values?",
        "options": [
            "int",
            "char",
            "float",
            "void"
        ],
        "correct": 2
    },
    {
        "id": 3,
        "question": "Which data type stores a single character?",
        "options": [
            "string",
            "char",
            "text",
            "character"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Which data type has double precision?",
        "options": [
            "float",
            "int",
            "double",
            "char"
        ],
        "correct": 2
    },
    {
        "id": 5,
        "question": "sizeof() operator is used for:\n---",
        "options": [
            "variable creation",
            "checking memory size",
            "printing values",
            "storing values"
        ],
        "correct": 1
    }
],
            "Constants": [
    {
        "id": 1,
        "question": "A constant is:",
        "options": [
            "variable value",
            "fixed value",
            "operator",
            "function"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which keyword defines constant variable?",
        "options": [
            "fixed",
            "constant",
            "const",
            "define"
        ],
        "correct": 2
    },
    {
        "id": 3,
        "question": "Example of numeric constant:",
        "options": [
            "25",
            "x",
            "sum",
            "value"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "#define is used for:",
        "options": [
            "declaring variable",
            "defining constant",
            "printing value",
            "loop control"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Constants cannot be:\n---",
        "options": [
            "stored",
            "modified",
            "declared",
            "printed"
        ],
        "correct": 1
    }
],
            "C Operators": [
    {
        "id": 1,
        "question": "Which operator performs addition?",
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
        "question": "Logical AND operator is:",
        "options": [
            "&&",
            "||",
            "&",
            "!"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "Which operator returns remainder?",
        "options": [
            "/",
            "%",
            "*",
            "+"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Assignment operator is:\n---",
        "options": [
            "=",
            "==",
            ":=",
            "=>"
        ],
        "correct": 0
    }
],
            "Input output": [
    {
        "id": 1,
        "question": "Which function prints output?",
        "options": [
            "input()",
            "printf()",
            "scanf()",
            "display()"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Which function reads input?",
        "options": [
            "printf()",
            "scanf()",
            "read()",
            "input()"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Header file for printf()?",
        "options": [
            "stdlib.h",
            "conio.h",
            "stdio.h",
            "math.h"
        ],
        "correct": 2
    },
    {
        "id": 4,
        "question": "%d is used for:",
        "options": [
            "float",
            "character",
            "integer",
            "string"
        ],
        "correct": 2
    },
    {
        "id": 5,
        "question": "%f is used for:\n---",
        "options": [
            "integer",
            "float",
            "char",
            "string"
        ],
        "correct": 1
    }
],
            "conditional_flow_statements1": [
    {
        "id": 1,
        "question": "Which statement checks condition?",
        "options": [
            "if",
            "loop",
            "for",
            "goto"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "if statement syntax ends with:",
        "options": [
            ";",
            ":",
            "()",
            "{}"
        ],
        "correct": 3
    },
    {
        "id": 3,
        "question": "else executes when:",
        "options": [
            "condition true",
            "condition false",
            "loop ends",
            "program ends"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Multiple conditions can be checked using:",
        "options": [
            "elif",
            "else if",
            "otherwise",
            "next"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Example\nif(x>5)\nThis is:\n---",
        "options": [
            "loop",
            "condition",
            "function",
            "array"
        ],
        "correct": 1
    }
],
            "Control Flow": [
    {
        "id": 1,
        "question": "Control flow determines:",
        "options": [
            "program execution order",
            "variable value",
            "memory allocation",
            "data type"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Which statement jumps to another location?",
        "options": [
            "goto",
            "break",
            "continue",
            "return"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "break is used in:",
        "options": [
            "loops",
            "functions",
            "variables",
            "arrays"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "continue does:",
        "options": [
            "stop program",
            "skip iteration",
            "exit loop",
            "restart program"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "return is used to:\n---",
        "options": [
            "repeat loop",
            "exit function",
            "skip code",
            "store value"
        ],
        "correct": 1
    }
],
            "Control_Flow__Directing_Code": [
    {
        "id": 1,
        "question": "Which keyword exits loop immediately?",
        "options": [
            "continue",
            "break",
            "goto",
            "return"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "continue sends control to:",
        "options": [
            "next iteration",
            "end program",
            "start program",
            "previous line"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "goto transfers control to:",
        "options": [
            "variable",
            "label",
            "array",
            "function"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Label syntax uses:",
        "options": [
            ";",
            ":",
            "{}",
            "()"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "return ends:\n---",
        "options": [
            "loop",
            "function",
            "condition",
            "array"
        ],
        "correct": 1
    }
],
            "The Switch Statement": [
    {
        "id": 1,
        "question": "switch is used for:",
        "options": [
            "multiple conditions",
            "loops",
            "arrays",
            "pointers"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "case is used inside:",
        "options": [
            "if",
            "switch",
            "loop",
            "function"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "default executes when:",
        "options": [
            "match found",
            "no match found",
            "first case",
            "last case"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "break prevents:",
        "options": [
            "fall-through",
            "compilation",
            "execution",
            "loops"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "switch expression must be:\n---",
        "options": [
            "float",
            "string",
            "integer",
            "array"
        ],
        "correct": 2
    }
],
            "The While Loop": [
    {
        "id": 1,
        "question": "while loop executes:",
        "options": [
            "once",
            "until condition false",
            "infinite only",
            "never"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Condition checked:",
        "options": [
            "before loop",
            "after loop",
            "inside loop",
            "none"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "Infinite loop example:",
        "options": [
            "while(0)",
            "while(1)",
            "while(false)",
            "while(stop)"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "while is used for:",
        "options": [
            "iteration",
            "variables",
            "arrays",
            "strings"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "Loop stops when:\n---",
        "options": [
            "condition false",
            "condition true",
            "break used",
            "both a and c"
        ],
        "correct": 3
    }
],
            "For Loop": [
    {
        "id": 1,
        "question": "for loop contains:",
        "options": [
            "2 parts",
            "3 parts",
            "4 parts",
            "5 parts"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Syntax structure:",
        "options": [
            "initialization",
            "condition",
            "increment",
            "all of these"
        ],
        "correct": 3
    },
    {
        "id": 3,
        "question": "for loop mainly used for:",
        "options": [
            "known iterations",
            "unknown iterations",
            "memory allocation",
            "pointer operations"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "Loop variable increments using:",
        "options": [
            "++",
            "--",
            "+=",
            "all of these"
        ],
        "correct": 3
    },
    {
        "id": 5,
        "question": "Example\nfor(i=0;i<5;i++)\nruns:\n---",
        "options": [
            "4 times",
            "5 times",
            "6 times",
            "infinite"
        ],
        "correct": 1
    }
],
            "Functions": [
    {
        "id": 1,
        "question": "Function is:",
        "options": [
            "block of code",
            "variable",
            "operator",
            "pointer"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "Function declaration is called:",
        "options": [
            "prototype",
            "header",
            "signature",
            "reference"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "return keyword:",
        "options": [
            "stops function",
            "prints value",
            "declares variable",
            "loops"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "Functions improve:",
        "options": [
            "modularity",
            "readability",
            "reuse",
            "all of these"
        ],
        "correct": 3
    },
    {
        "id": 5,
        "question": "main() is:\n---",
        "options": [
            "user function",
            "library function",
            "starting function",
            "pointer"
        ],
        "correct": 2
    }
],
            "Arrays": [
    {
        "id": 1,
        "question": "Array stores:",
        "options": [
            "single value",
            "multiple values of same type",
            "different types",
            "pointers only"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Array index starts from:",
        "options": [
            "0",
            "1",
            "2",
            "-1"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "Example\nint a[5];\nmeans:",
        "options": [
            "5 integers",
            "5 floats",
            "5 chars",
            "5 pointers"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "Access element using:",
        "options": [
            "()",
            "[]",
            "{}",
            "<>"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Array size is:\n---",
        "options": [
            "fixed",
            "dynamic",
            "flexible",
            "unknown"
        ],
        "correct": 0
    }
],
            "Pointers": [
    {
        "id": 1,
        "question": "Pointer stores:",
        "options": [
            "value",
            "address",
            "variable",
            "function"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Pointer declaration symbol:",
        "options": [
            "&",
            "*",
            "#",
            "%"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Address operator is:",
        "options": [
            "&",
            "*",
            "%",
            "#"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "Dereferencing operator:",
        "options": [
            "&",
            "*",
            "%",
            "#"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "Pointer improves:\n---",
        "options": [
            "memory handling",
            "performance",
            "dynamic memory",
            "all of these"
        ],
        "correct": 3
    }
],
            "String": [
    {
        "id": 1,
        "question": "String in C is:",
        "options": [
            "char array",
            "integer",
            "pointer",
            "float"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "String ends with:",
        "options": [
            "\\0",
            "\\n",
            "\\t",
            "EOF"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "Header for string functions:",
        "options": [
            "string.h",
            "stdio.h",
            "math.h",
            "stdlib.h"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "strlen() returns:",
        "options": [
            "string size",
            "string length",
            "address",
            "index"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "strcpy() is used to:\n---",
        "options": [
            "compare",
            "copy",
            "concatenate",
            "delete"
        ],
        "correct": 1
    }
],
            "Structures and Unions": [
    {
        "id": 1,
        "question": "Structure stores:",
        "options": [
            "same data types",
            "different data types",
            "single value",
            "pointer only"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "Keyword for structure:",
        "options": [
            "struct",
            "structure",
            "record",
            "data"
        ],
        "correct": 0
    },
    {
        "id": 3,
        "question": "Union shares:",
        "options": [
            "different memory",
            "same memory",
            "pointer memory",
            "array memory"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "Structure access operator:",
        "options": [
            ".",
            "->",
            "&",
            "*"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "Union saves:\n---",
        "options": [
            "memory",
            "variables",
            "pointers",
            "loops"
        ],
        "correct": 0
    }
],
            "Dynamic Memory Allocation": [
    {
        "id": 1,
        "question": "malloc() is used for:",
        "options": [
            "memory allocation",
            "printing",
            "scanning",
            "looping"
        ],
        "correct": 0
    },
    {
        "id": 2,
        "question": "free() is used to:",
        "options": [
            "allocate memory",
            "release memory",
            "copy memory",
            "print memory"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "calloc() allocates:",
        "options": [
            "single block",
            "multiple blocks",
            "pointer",
            "string"
        ],
        "correct": 1
    },
    {
        "id": 4,
        "question": "realloc() is used to:",
        "options": [
            "resize memory",
            "delete memory",
            "allocate new pointer",
            "loop memory"
        ],
        "correct": 0
    },
    {
        "id": 5,
        "question": "Header file:\n---",
        "options": [
            "stdlib.h",
            "stdio.h",
            "string.h",
            "math.h"
        ],
        "correct": 0
    }
],
            "File Handling": [
    {
        "id": 1,
        "question": "File opening function:",
        "options": [
            "open()",
            "fopen()",
            "fileopen()",
            "read()"
        ],
        "correct": 1
    },
    {
        "id": 2,
        "question": "File closing function:",
        "options": [
            "close()",
            "fclose()",
            "stop()",
            "end()"
        ],
        "correct": 1
    },
    {
        "id": 3,
        "question": "Mode \"r\" means:",
        "options": [
            "read",
            "write",
            "append",
            "create"
        ],
        "correct": 0
    },
    {
        "id": 4,
        "question": "fprintf() writes to:",
        "options": [
            "console",
            "file",
            "pointer",
            "variable"
        ],
        "correct": 1
    },
    {
        "id": 5,
        "question": "fscanf() reads from:",
        "options": [
            "keyboard",
            "file",
            "pointer",
            "array"
        ],
        "correct": 1
    }
],
        }

        count = 0
        for title, quiz in quizzes.items():
            topic = Topic.objects.filter(title=title, course__title='C Programming').first()
            if topic:
                topic.predefined_quiz = quiz
                topic.save()
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully re-seeded {count} C Programming quizzes!'))
