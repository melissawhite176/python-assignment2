# Questions
# Basics
# 1. What is an expression?
  # An expression is a construct made up of variables, operators, and method invocations, which are constructed according to the syntax of the language, that evaluates to a single value. 
# 2. What is a syntax error?
  # When the interpreter encounters invalid syntax in Python code, it will raise a SyntaxError exception. Examples: missing a comma, closing parentheses, closing quotation, etc.
# 3. What is PEP8?
  # PEP stands for Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.
# 4. What does a linter do?
  # lint, or a linter, is a tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs. https://en.wikipedia.org/wiki/Lint(software)
# 5. What is the result of this expression: “*” * 10
  # asterisk printed 10 times as a string
print("*" * 10)

# 6. What is CPython?
  # CPython is the reference implementation of the Python programming language. Written in C and Python, CPython is the default and most widely used implementation of the language. CPython can be defined as both an interpreter and a compiler as it compiles Python code into bytecode before interpreting it. (https://en.wikipedia.org/wiki/CPython)

# 7. How is CPython different from Jython?
  # Jython is an implementation of the Python programming language designed to run on the Java platform. The implementation was formerly known as JPython until 1999.(https://en.wikipedia.org/wiki/Jython). JPython runs on the Java platform. CPython uses C and Python.

# 8. How is CPython different from IronPython?
  # IronPython is an implementation of the Python programming language targeting the .NET Framework and Mono. Jim Hugunin created the project and actively contributed to it up until Version 1.0 which was released on September 5, 2006. IronPython 2.0 was released on December 10, 2008. (https://en.wikipedia.org/wiki/IronPython)

# Primitive Types
# 1. What is a variable?
  # A Python variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name. But the data itself is still contained within the object. (https://realpython.com/python-variables/)
# 2. What are the primitive built-in types in Python?
  # The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions. (https://docs.python.org/3/library/stdtypes.html)
# 3. When should we use “”” (triple quotes) to define strings?
  # When creating a strings that spans multiple lines
# 4. Assuming (name = “John Smith”), what does name[1] return? "o"
name = "John Smith"
print(name[1])
# 5. What about name[-2]? "t"
print(name[-2])
# 6. What about name[1:-1]? "ohn Smit"
print(name[1:-1])
# 7. How to get the length of name?
print(len(name))
# 8. What are the escape sequences in Python?
  # They are usually used to insert a quote character within a string. Other uses:
  # \'	Single Quote	
  # \\	Backslash	
  # \n	New Line	
  # \r	Carriage Return	
  # \t	Tab	
  # \b	Backspace	
  # \f	Form Feed	
  # \ooo	Octal value	
  # \xhh	Hex value

# 9. What is the result of f“{2+2}+{10%3}”? 4+1
print(f"{2+2}+{10%3}")
# 10. Given (name = “john smith”), what will name.title() return? Returns "titlecased" version, uppercase for the first letter of each word
name = "john smith"
print('name.title():', name.title())
# 11. What does name.strip() do? Removes trailing spaces
nameWithSpaces = "    john smith           "
print('name.strip():', name.strip())
print('nameWithSpaces.strip():', nameWithSpaces.strip())
# 12. What will name.find(“Smith”) return? -1 
print('name.find("Smith"):', name.find("Smith"))
# 13. What will be the value of name after we call name.replace(“j”, “k”)? kohn smith
newName = name.replace("j", "k")
print(newName)
# 14. How can we check to see if name contains “John”?
print(name.find("John"))
if "John" in name:
  print("Found")
else:
  print("Not Found")
# 15. What are the 3 types of numbers in Python?
  # There are three distinct numeric types: integers, floating point numbers, and complex numbers.

# Control Flow
# 1. What is the difference between 10 / 3 and 10 // 3?
print(10/3) #quotient of 10 and 3
print(10//3) #floored quotient of 10 and 3
# 2. What is the result of 10 ** 3? 1000
print('10 ** 3 =', 10 ** 3)
# 3. Given (x = 1), what will be the value of after we run (x += 2)? 2
x = 1
x += 2
print(x)
# 4. How can we round a number?
a = 2.3
print(round(a))
# 5. What is the result of float(1)? 1.0
print(float(1))
# 6. What is the result of bool(“False”)?
print(bool("False")) #truthy
print(bool(False)) #False
# 7. What are the falsy values in Python?
  # Falsy Values are the following...
    # Sequences and Collections:
      # Empty lists []
      # Empty tuples ()
      # Empty dictionaries {}
      # Empty sets set()
      # Empty strings ""
      # Empty ranges range(0)
      
    # Numbers:
      # Zero of any numeric type
      # Integer: 0
      # Float: 0.0
      # Complex: 0j
      
    # Constants:
      # None
      # False
    #(https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/)

# 8. What is the result of 10 == “10”? False
print(10 == "10")
# 9. What is the result of “bag” > “apple”? True
print("bag" > "apple")
# 10. What is the result of not(True or False)?
print(not(True or False))
print(not(True))
print(not(False))
# 11. Under what circumstances does the expression 18 <= age < 65 evaluate to True? Age between 18 and 65 (18 inclusive)
age = 30
print(18 <= age < 65)
# 12. What does range(1, 10, 2) return? Prints the same range(1, 10, 2). By implementing range with a list, a list of odd numbers between 1 and 10 will print out: [1, 3, 5, 7, 9]
print(range(1, 10, 2))
print(list(range(1, 10, 2)))

# 13. Name 3 iterable objects in Python.
  #Lists, tuples, dictionaries, (and sets) are iterable objects (https://www.w3schools.com/python/python_iterators.asp#:~:text=Lists%2C%20tuples%2C%20dictionaries%2C%20and,can%20get%20an%20iterator%20from.)

# Functions
# 1. What is the difference between a parameter and an argument?
# 2. All functions in Python by default return ...?
# 3. What are keyword arguments and when should we use them?
# 4. How can we make a parameter of a function optional?
# 5. What happens when we prefix a parameter with an asterisk (*)?
# 6. What about two asterisks (**)?
# 7. What is scope?
# 8. What is the difference between local and global variables?
# 9. Why is using the global statement a bad practice?

# Coding Exercises
# 1. Write a function that returns the maximum of two numbers.
# 2. Write a function called fizz_buzz that takes a number.
# 1. If the number is divisible by 3, it should return “Fizz”.
# 2. If it is divisible by 5, it should return “Buzz”.
# 3. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# 4. Otherwise, it should return the same number.
# 3. Write a function for checking the speed of drivers. This function should have one parameter:
# speed.
# 1. If speed is less than 70, it should print “Ok”.
# 2. Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit
# point and print the total number of demerit points. For example, if the speed is 80, it
# should print: “Points: 2”.
# 3. If the driver gets more than 12 points, the function should print: “License suspended”
# 4. Write a function called showNumbers that takes a parameter called limit. It should print all
# the numbers between 0 and limit with a label to identify the even and odd numbers. For
# example, if the limit is 3, it should print:
# o 0 EVEN
# o 1 ODD
# o 2 EVEN
# o 3 ODD
# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
# 6. Write a function called show_stars(rows). If rows is 5, it should print the following:
# o *
# o **
# o ***
# o ****
# o *****
# 7. Write a function that prints all the prime numbers between 0 and limit where limit is a
# parameter.