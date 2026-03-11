import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codecrafters.settings')
django.setup()

from courses.models import Topic

raw_text = """
### 1. Introduction to C

1. Who developed the C programming language?
   a) Dennis Ritchie
   b) Bjarne Stroustrup
   c) James Gosling
   d) Guido van Rossum
   **Answer:** a

2. C language was developed at:
   a) Microsoft
   b) Bell Labs
   c) IBM
   d) Google
   **Answer:** b

3. C is mainly a:
   a) High-level language
   b) Low-level language
   c) Middle-level language
   d) Assembly language
   **Answer:** c

4. Which extension is used for C source files?
   a) .cpp
   b) .c
   c) .java
   d) .py
   **Answer:** b

5. Which function is the entry point of a C program?
   a) start()
   b) run()
   c) main()
   d) begin()
   **Answer:** c

---

# 2. Variables

1. A variable is:
   a) Fixed value
   b) Memory location to store data
   c) Keyword
   d) Operator
   **Answer:** b

2. Which is a valid variable name?
   a) 2num
   b) num_1
   c) num-1
   d) int
   **Answer:** b

3. Variables must be declared before:
   a) compilation
   b) usage
   c) printing
   d) execution
   **Answer:** b

4. Which symbol ends a statement in C?
   a) :
   b) ;
   c) ,
   d) .
   **Answer:** b

5. Example

```
int x = 10;
```

10 is:
a) variable
b) identifier
c) value
d) operator
**Answer:** c

---

# 3. Data Types

1. Which is an integer data type?
   a) int
   b) float
   c) char
   d) double
   **Answer:** a

2. Which type stores decimal values?
   a) int
   b) char
   c) float
   d) void
   **Answer:** c

3. Which data type stores a single character?
   a) string
   b) char
   c) text
   d) character
   **Answer:** b

4. Which data type has double precision?
   a) float
   b) int
   c) double
   d) char
   **Answer:** c

5. sizeof() operator is used for:
   a) variable creation
   b) checking memory size
   c) printing values
   d) storing values
   **Answer:** b

---

# 4. Constants

1. A constant is:
   a) variable value
   b) fixed value
   c) operator
   d) function
   **Answer:** b

2. Which keyword defines constant variable?
   a) fixed
   b) constant
   c) const
   d) define
   **Answer:** c

3. Example of numeric constant:
   a) 25
   b) x
   c) sum
   d) value
   **Answer:** a

4. #define is used for:
   a) declaring variable
   b) defining constant
   c) printing value
   d) loop control
   **Answer:** b

5. Constants cannot be:
   a) stored
   b) modified
   c) declared
   d) printed
   **Answer:** b

---

# 5. C Operators

1. Which operator performs addition?
   a) +
   b) -
   c) *
   d) /
   **Answer:** a

2. Which operator checks equality?
   a) =
   b) ==
   c) !=
   d) >=
   **Answer:** b

3. Logical AND operator is:
   a) &&
   b) ||
   c) &
   d) !
   **Answer:** a

4. Which operator returns remainder?
   a) /
   b) %
   c) *
   d) +
   **Answer:** b

5. Assignment operator is:
   a) =
   b) ==
   c) :=
   d) =>
   **Answer:** a

---

# 6. Input Output

1. Which function prints output?
   a) input()
   b) printf()
   c) scanf()
   d) display()
   **Answer:** b

2. Which function reads input?
   a) printf()
   b) scanf()
   c) read()
   d) input()
   **Answer:** b

3. Header file for printf()?
   a) stdlib.h
   b) conio.h
   c) stdio.h
   d) math.h
   **Answer:** c

4. %d is used for:
   a) float
   b) character
   c) integer
   d) string
   **Answer:** c

5. %f is used for:
   a) integer
   b) float
   c) char
   d) string
   **Answer:** b

---

# 7. Conditional Flow Statements

1. Which statement checks condition?
   a) if
   b) loop
   c) for
   d) goto
   **Answer:** a

2. if statement syntax ends with:
   a) ;
   b) :
   c) ()
   d) {}
   **Answer:** d

3. else executes when:
   a) condition true
   b) condition false
   c) loop ends
   d) program ends
   **Answer:** b

4. Multiple conditions can be checked using:
   a) elif
   b) else if
   c) otherwise
   d) next
   **Answer:** b

5. Example

```
if(x>5)
```

This is:
a) loop
b) condition
c) function
d) array
**Answer:** b

---

# 8. Control Flow

1. Control flow determines:
   a) program execution order
   b) variable value
   c) memory allocation
   d) data type
   **Answer:** a

2. Which statement jumps to another location?
   a) goto
   b) break
   c) continue
   d) return
   **Answer:** a

3. break is used in:
   a) loops
   b) functions
   c) variables
   d) arrays
   **Answer:** a

4. continue does:
   a) stop program
   b) skip iteration
   c) exit loop
   d) restart program
   **Answer:** b

5. return is used to:
   a) repeat loop
   b) exit function
   c) skip code
   d) store value
   **Answer:** b

---

# 9. Control Flow – Directing Code

1. Which keyword exits loop immediately?
   a) continue
   b) break
   c) goto
   d) return
   **Answer:** b

2. continue sends control to:
   a) next iteration
   b) end program
   c) start program
   d) previous line
   **Answer:** a

3. goto transfers control to:
   a) variable
   b) label
   c) array
   d) function
   **Answer:** b

4. Label syntax uses:
   a) ;
   b) :
   c) {}
   d) ()
   **Answer:** b

5. return ends:
   a) loop
   b) function
   c) condition
   d) array
   **Answer:** b

---

# 10. The Switch Statement

1. switch is used for:
   a) multiple conditions
   b) loops
   c) arrays
   d) pointers
   **Answer:** a

2. case is used inside:
   a) if
   b) switch
   c) loop
   d) function
   **Answer:** b

3. default executes when:
   a) match found
   b) no match found
   c) first case
   d) last case
   **Answer:** b

4. break prevents:
   a) fall-through
   b) compilation
   c) execution
   d) loops
   **Answer:** a

5. switch expression must be:
   a) float
   b) string
   c) integer
   d) array
   **Answer:** c

---

# 11. The While Loop

1. while loop executes:
   a) once
   b) until condition false
   c) infinite only
   d) never
   **Answer:** b

2. Condition checked:
   a) before loop
   b) after loop
   c) inside loop
   d) none
   **Answer:** a

3. Infinite loop example:
   a) while(0)
   b) while(1)
   c) while(false)
   d) while(stop)
   **Answer:** b

4. while is used for:
   a) iteration
   b) variables
   c) arrays
   d) strings
   **Answer:** a

5. Loop stops when:
   a) condition false
   b) condition true
   c) break used
   d) both a and c
   **Answer:** d

---

# 12. For Loop

1. for loop contains:
   a) 2 parts
   b) 3 parts
   c) 4 parts
   d) 5 parts
   **Answer:** b

2. Syntax structure:
   a) initialization
   b) condition
   c) increment
   d) all of these
   **Answer:** d

3. for loop mainly used for:
   a) known iterations
   b) unknown iterations
   c) memory allocation
   d) pointer operations
   **Answer:** a

4. Loop variable increments using:
   a) ++
   b) --
   c) +=
   d) all of these
   **Answer:** d

5. Example

```
for(i=0;i<5;i++)
```

runs:
a) 4 times
b) 5 times
c) 6 times
d) infinite
**Answer:** b

---

# 13. Functions

1. Function is:
   a) block of code
   b) variable
   c) operator
   d) pointer
   **Answer:** a

2. Function declaration is called:
   a) prototype
   b) header
   c) signature
   d) reference
   **Answer:** a

3. return keyword:
   a) stops function
   b) prints value
   c) declares variable
   d) loops
   **Answer:** a

4. Functions improve:
   a) modularity
   b) readability
   c) reuse
   d) all of these
   **Answer:** d

5. main() is:
   a) user function
   b) library function
   c) starting function
   d) pointer
   **Answer:** c

---

# 14. Arrays

1. Array stores:
   a) single value
   b) multiple values of same type
   c) different types
   d) pointers only
   **Answer:** b

2. Array index starts from:
   a) 0
   b) 1
   c) 2
   d) -1
   **Answer:** a

3. Example

```
int a[5];
```

means:
a) 5 integers
b) 5 floats
c) 5 chars
d) 5 pointers
**Answer:** a

4. Access element using:
   a) ()
   b) []
   c) {}
   d) <>
   **Answer:** b

5. Array size is:
   a) fixed
   b) dynamic
   c) flexible
   d) unknown
   **Answer:** a

---

# 15. Pointers

1. Pointer stores:
   a) value
   b) address
   c) variable
   d) function
   **Answer:** b

2. Pointer declaration symbol:
   a) &
   b) *
   c) #
   d) %
   **Answer:** b

3. Address operator is:
   a) &
   b) *
   c) %
   d) #
   **Answer:** a

4. Dereferencing operator:
   a) &
   b) *
   c) %
   d) #
   **Answer:** b

5. Pointer improves:
   a) memory handling
   b) performance
   c) dynamic memory
   d) all of these
   **Answer:** d

---

# 16. String

1. String in C is:
   a) char array
   b) integer
   c) pointer
   d) float
   **Answer:** a

2. String ends with:
   a) \\0
   b) \\n
   c) \\t
   d) EOF
   **Answer:** a

3. Header for string functions:
   a) string.h
   b) stdio.h
   c) math.h
   d) stdlib.h
   **Answer:** a

4. strlen() returns:
   a) string size
   b) string length
   c) address
   d) index
   **Answer:** b

5. strcpy() is used to:
   a) compare
   b) copy
   c) concatenate
   d) delete
   **Answer:** b

---

# 17. Structures and Unions

1. Structure stores:
   a) same data types
   b) different data types
   c) single value
   d) pointer only
   **Answer:** b

2. Keyword for structure:
   a) struct
   b) structure
   c) record
   d) data
   **Answer:** a

3. Union shares:
   a) different memory
   b) same memory
   c) pointer memory
   d) array memory
   **Answer:** b

4. Structure access operator:
   a) .
   b) ->
   c) &
   d) *
   **Answer:** a

5. Union saves:
   a) memory
   b) variables
   c) pointers
   d) loops
   **Answer:** a

---

# 18. Dynamic Memory Allocation

1. malloc() is used for:
   a) memory allocation
   b) printing
   c) scanning
   d) looping
   **Answer:** a

2. free() is used to:
   a) allocate memory
   b) release memory
   c) copy memory
   d) print memory
   **Answer:** b

3. calloc() allocates:
   a) single block
   b) multiple blocks
   c) pointer
   d) string
   **Answer:** b

4. realloc() is used to:
   a) resize memory
   b) delete memory
   c) allocate new pointer
   d) loop memory
   **Answer:** a

5. Header file:
   a) stdlib.h
   b) stdio.h
   c) string.h
   d) math.h
   **Answer:** a

---

# 19. File Handling

1. File opening function:
   a) open()
   b) fopen()
   c) fileopen()
   d) read()
   **Answer:** b

2. File closing function:
   a) close()
   b) fclose()
   c) stop()
   d) end()
   **Answer:** b

3. Mode "r" means:
   a) read
   b) write
   c) append
   d) create
   **Answer:** a

4. fprintf() writes to:
   a) console
   b) file
   c) pointer
   d) variable
   **Answer:** b

5. fscanf() reads from:
   a) keyboard
   b) file
   c) pointer
   d) array
   **Answer:** b
"""

ans_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

# Splitting by topic headers
topic_blocks = re.split(r'#+\s*\d+\.\s*(.+)', raw_text)

updated_count = 0

# topic_blocks[0] is empty, then pairs of title/content
for i in range(1, len(topic_blocks), 2):
    title = topic_blocks[i].strip()
    content = topic_blocks[i+1]
    
    # Strict mapping dictionary to handle discrepancies
    title_map = {
        "Introduction to C": "Introduction to C",
        "Variables": "Variables",
        "Data Types": "Data Types",
        "Constants": "Constants",
        "C Operators": "C Operators",
        "Input Output": "Input output",
        "Conditional Flow Statements": "conditional_flow_statements1",
        "Control Flow": "Control Flow",
        "Control Flow – Directing Code": "Control_Flow__Directing_Code",
        "The Switch Statement": "The Switch Statement",
        "The While Loop": "The While Loop",
        "For Loop": "For Loop",
        "Functions": "Functions",
        "Arrays": "Arrays",
        "Pointers": "Pointers",
        "String": "String",
        "Structures and Unions": "Structures and Unions",
        "Dynamic Memory Allocation": "Dynamic Memory Allocation",
        "File Handling": "File Handling"
    }
    
    db_title = title_map.get(title)
    topic = None
    if db_title:
        topic = Topic.objects.filter(title=db_title, course__title='C Programming').first()
        
    if topic:
        quiz = []
        q_blocks = re.split(r'\n\d+\.\s+', '\n' + content.strip())[1:] # get rid of first empty
        
        for idx, q_text in enumerate(q_blocks, start=1):
            lines = q_text.strip().split('\n')
            question_body = []
            options = []
            answer_idx = 0
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                if line.startswith('a)') or line.startswith('b)') or line.startswith('c)') or line.startswith('d)'):
                    options.append(line[2:].strip())
                elif line.startswith('**Answer:**'):
                    char = line.split('**Answer:**')[1].strip().lower()
                    answer_idx = ans_map.get(char, 0)
                else:
                    if not line.startswith('```'):
                        question_body.append(line)
                    
            quiz.append({
                "id": idx,
                "question": '\n'.join(question_body),
                "options": options,
                "correct": answer_idx
            })
            
        topic.predefined_quiz = quiz
        topic.save()
        updated_count += 1
        print(f"Success: Appended custom C quiz: {topic.title} ({len(quiz)} qs)")
    else:
        print(f"Failed: Could not find C Programming topic matching '{title}'")

print(f"\nSuccessfully overwrote {updated_count} topics with custom C quizzes!")
