import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pathmind.settings')
django.setup()

from courses.models import Topic

summaries = {
    "Introduction to C": "## Introduction to C Programming\n\nWelcome to C! This lesson covers the origins of the language, created by Dennis Ritchie at Bell Labs. We'll explore why C is considered a 'middle-level' language, its role in modern computing, and the typical structure of a C source file (`.c`), culminating in your first `main()` function.",
    "Variables": "## Variables in C\n\nVariables are named memory locations used to store data. In this lesson, we learn the rules for naming identifiers, how to declare variables, and the crucial step of initializing them before use. We'll also cover statement terminators (`;`) and basic memory concepts.",
    "Data Types": "## C Data Types\n\nEvery variable in C must have a defined data type. We dive into the primary types: `int` for whole numbers, `float` and `double` for decimal precision, and `char` for single characters. You will also learn how to use the `sizeof()` operator to check memory footprints.",
    "Constants": "## Working with Constants\n\nConstants are fixed values that cannot be altered by the program during its execution. We explore literal constants, the `const` keyword, and preprocessor directives like `#define` to create robust, hardcoded configuration values.",
    "C Operators": "## Operators and Expressions\n\nC provides a rich set of built-in operators. This module covers arithmetic operators (`+`, `-`, `*`, `/`, `%`), relational operators for comparisons (`==`, `!=`, `<`, `>`), and logical operators (`&&`, `||`, `!`) to build complex mathematical expressions.",
    "Input output": "## Standard I/O in C\n\nLearn how to interact with the user via standard input and output streams. We heavily utilize the `<stdio.h>` library, diving into `printf()` for formatted output using format specifiers (`%d`, `%f`, `%c`), and `scanf()` to safely read user input into memory addresses.",
    "conditional_flow_statements1": "## Conditional Flow: If/Else\n\nPrograms need to make decisions. Here we introduce the `if` statement for basic branching logic, `else` for default fallbacks, and `else if` chains for evaluating multiple sequential conditions based on boolean evaluations.",
    "Control Flow": "## Core Control Flow Concepts\n\nControl flow dictates the exact order in which individual statements and instructions are executed. We introduce the concept of jumps, blocks of code, and how the CPU processes instructions sequentially unless interrupted by a control statement.",
    "Control_Flow__Directing_Code": "## Unconditional Branching\n\nTake deep control over execution paths by using unconditional jump statements. We cover the controversial `goto` statement and labels, understand how `return` passes execution back to the caller, and look at breaking out of standard flow blocks.",
    "The Switch Statement": "## The Switch Statement\n\nA cleaner alternative to massive `else if` chains when checking a single integer or character variable against distinct, hardcoded cases. We explore the `switch`, `case`, `default`, and why the `break` keyword is absolutely critical to prevent fall-through bugs.",
    "The While Loop": "## The While Loop\n\nLoops allow us to repeat blocks of code. The `while` loop checks a condition *before* executing the block, repeating until the condition evaluates to false. We also examine infinite loops (`while(1)`) and how to properly update loop control variables.",
    "For Loop": "## The For Loop\n\nThe `for` loop condenses initialization, condition checking, and incrementing into a single, clean line of syntax. We'll learn why this is the preferred loop for known, finite iterations, like stepping through indices.",
    "Functions": "## Functions and Modularity\n\nFunctions are reusable blocks of code that perform specific tasks. This lesson covers function prototypes, defining parameters, return types, calling functions, and how modular design makes C code dramatically easier to read, test, and maintain.",
    "Arrays": "## Arrays: Contiguous Memory\n\nAn array is a collection of contiguous memory locations storing multiple items of the exact same data type. We learn how to declare arrays, configure sizes, and access elements safely using zero-based indexing (`arr[0]`).",
    "Pointers": "## Pointers in C\n\nThe definitive feature of C programming. A pointer is simply a variable that stores the raw memory address of another variable. We master the address-of operator (`&`), dereferencing (`*`), and how pointers enable massive performance optimizations.",
    "String": "## Strings (Character Arrays)\n\nUnlike Python or Java, C does not have a native String object type. Instead, strings are simply contiguous arrays of `char` types, terminated by a null character (`\\0`). We explore the `<string.h>` library to copy (`strcpy`), measure (`strlen`), and manipulate text.",
    "Structures and Unions": "## Custom Data: Structs & Unions\n\nSometimes primitive types aren't enough. A `struct` allows you to group different data types (like an int, a string, and a float) under a single logical entity (e.g., a `Student`). We also briefly touch on `union` types for memory sharing.",
    "Dynamic Memory Allocation": "## Dynamic Memory Allocation\n\nBreak free from fixed-size arrays! Learn to request heap memory on the fly during runtime. We utilize `<stdlib.h>` to explore `malloc()`, `calloc()`, memory resizing with `realloc()`, and the critical importance of preventing memory leaks via `free()`.",
    "File Handling": "## File I/O Operations\n\nFinally, we persist data to the hard drive. We learn how to use file pointers (`FILE *`) to open files with `fopen()` in various modes (read, write, append). We cover writing data with `fprintf()`, reading with `fscanf()`, and always securing handles via `fclose()`."
}

credits_text = """\n\nCredits & Citation:\nThe audio and video content for this lesson was generated using Google's NotebookLM. We thank Google and the NotebookLM team for providing the AI tools used to create these interactive learning experiences."""

updated_count = 0
for title, text in summaries.items():
    topic = Topic.objects.filter(title=title, course__title='C Programming').first()
    if topic:
        topic.content = text.strip() + credits_text
        topic.save()
        updated_count += 1
        print(f"Updated content for: {topic.title}")
    else:
        print(f"Warning: Could not find topic for title: {title}")

print(f"\nSuccessfully populated lesson contents for {updated_count} topics!")
