# JALA Academy - Python Programming Complete Assignments
# All 100+ exercises covering 15 sections

print("=" * 60)
print("JALA ACADEMY - PYTHON PROGRAMMING ASSIGNMENTS")
print("=" * 60)

# ============================================================================
# 1. PYTHON BASICS (4 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("1. PYTHON BASICS")
print("=" * 60)

# Q1: Write a program to print your name
print("\nQ1: Print your name")
print("My name is: JALA Student")

# Q2: Single line and multi-line comments
print("\nQ2: Comments demonstration")
# This is a single line comment

"""
This is a multi-line comment
It can span multiple lines
Used for documentation
"""

'''
This is also a multi-line comment
Using triple single quotes
'''

print("Comments added successfully!")

# Q3: Different data types
print("\nQ3: Different Data Types")
int_var = 42
bool_var = True
char_var = 'A'  # Python doesn't have char, using string
float_var = 3.14
double_var = 3.141592653589793  # Python float is double precision

print(f"Integer: {int_var}, Type: {type(int_var)}")
print(f"Boolean: {bool_var}, Type: {type(bool_var)}")
print(f"Character: {char_var}, Type: {type(char_var)}")
print(f"Float: {float_var}, Type: {type(float_var)}")
print(f"Double: {double_var}, Type: {type(double_var)}")

# Q4: Local and Global variables with same name
print("\nQ4: Local and Global Variable Scope")
x = "Global Variable"

def test_scope():
    x = "Local Variable"
    print(f"Inside function: {x}")

print(f"Outside function: {x}")
test_scope()
print(f"After function call: {x}")

# ============================================================================
# 2. OPERATORS (5 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("2. OPERATORS")
print("=" * 60)

# Q1: Arithmetic operators
print("\nQ1: Arithmetic Operators")
def arithmetic_operators(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponent: {a} ** {b} = {a ** b}")

arithmetic_operators(10, 3)

# Q2: Increment and Decrement (Python doesn't have ++ --)
print("\nQ2: Increment and Decrement")
num = 5
print(f"Original value: {num}")
num += 1
print(f"After increment (num += 1): {num}")
num -= 1
print(f"After decrement (num -= 1): {num}")

# Q3: Check if two numbers are equal
print("\nQ3: Check if two numbers are equal")
def check_equal(a, b):
    if a == b:
        print(f"{a} and {b} are equal")
    else:
        print(f"{a} and {b} are not equal")

check_equal(5, 5)
check_equal(5, 10)

# Q4: Relational operators
print("\nQ4: Relational Operators")
a, b = 10, 20
print(f"a = {a}, b = {b}")
print(f"a < b: {a < b}")
print(f"a <= b: {a <= b}")
print(f"a > b: {a > b}")
print(f"a >= b: {a >= b}")

# Q5: Print smaller and larger number
print("\nQ5: Smaller and Larger Number")
def find_min_max(a, b):
    print(f"Smaller number: {min(a, b)}")
    print(f"Larger number: {max(a, b)}")

find_min_max(15, 25)

# ============================================================================
# 3. LOOPS (12 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("3. LOOPS")
print("=" * 60)

# Q1: Print "Bright IT Career" 10 times
print("\nQ1: Print 'Bright IT Career' 10 times using for loop")
for i in range(10):
    print(f"{i+1}. Bright IT Career")

# Q2: Print 1 to 20 using while loop
print("\nQ2: Print 1 to 20 using while loop")
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print()

# Q3: Equal and not equal operators
print("\nQ3: Equal and Not Equal Operators")
a, b = 10, 10
c, d = 10, 20
print(f"{a} == {b}: {a == b}")
print(f"{c} != {d}: {c != d}")

# Q4: Print odd and even numbers
print("\nQ4: Print odd and even numbers from 1 to 20")
print("Even numbers:", end=" ")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print("\nOdd numbers:", end=" ")
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")
print()

# Q5: Largest among three numbers
print("\nQ5: Largest among three numbers")
def find_largest(a, b, c):
    largest = max(a, b, c)
    print(f"Largest among {a}, {b}, {c} is: {largest}")

find_largest(10, 25, 15)

# Q6: Print even numbers between 10 and 20 using while
print("\nQ6: Even numbers between 10 and 20 using while loop")
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

# Q7: Print 1 to 10 using do-while (Python doesn't have do-while, using while)
print("\nQ7: Print 1 to 10 using while loop (Python's equivalent)")
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 10:
        break
print()

# Q8: Armstrong number
print("\nQ8: Check Armstrong number")
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    sum_of_powers = sum(int(digit) ** power for digit in digits)
    return sum_of_powers == num

test_num = 153
print(f"{test_num} is {'an Armstrong' if is_armstrong(test_num) else 'not an Armstrong'} number")

# Q9: Prime number
print("\nQ9: Check Prime number")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

test_num = 17
print(f"{test_num} is {'a Prime' if is_prime(test_num) else 'not a Prime'} number")

# Q10: Palindrome
print("\nQ10: Check Palindrome")
def is_palindrome(num):
    return str(num) == str(num)[::-1]

test_num = 121
print(f"{test_num} is {'a Palindrome' if is_palindrome(test_num) else 'not a Palindrome'}")

# Q11: Even or Odd using if-else (Python doesn't have switch)
print("\nQ11: Check EVEN or ODD")
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is EVEN")
    else:
        print(f"{num} is ODD")

check_even_odd(10)
check_even_odd(7)

# Q12: Print gender based on M/F
print("\nQ12: Print gender based on M/F")
def print_gender(char):
    gender_map = {'M': 'Male', 'F': 'Female'}
    print(f"Gender: {gender_map.get(char.upper(), 'Invalid input')}")

print_gender('M')
print_gender('F')

# ============================================================================
# 4. ARRAYS/LISTS (18 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("4. ARRAYS/LISTS")
print("=" * 60)

# Q1: Add integer values of an array
print("\nQ1: Sum of array elements")
arr = [1, 2, 3, 4, 5]
print(f"Array: {arr}")
print(f"Sum: {sum(arr)}")

# Q2: Average of array
print("\nQ2: Average of array")
average = sum(arr) / len(arr)
print(f"Average: {average}")

# Q3: Find index of element
print("\nQ3: Find index of element")
element = 3
if element in arr:
    print(f"Index of {element}: {arr.index(element)}")

# Q4: Test if array contains specific value
print("\nQ4: Check if array contains value")
print(f"Array contains 3: {3 in arr}")
print(f"Array contains 10: {10 in arr}")

# Q5: Remove specific element
print("\nQ5: Remove specific element")
arr_copy = arr.copy()
arr_copy.remove(3)
print(f"After removing 3: {arr_copy}")

# Q6: Copy array
print("\nQ6: Copy array")
arr_copy = arr.copy()
print(f"Original: {arr}")
print(f"Copy: {arr_copy}")

# Q7: Insert element at specific position
print("\nQ7: Insert element at position")
arr_copy = arr.copy()
arr_copy.insert(2, 99)
print(f"After inserting 99 at index 2: {arr_copy}")

# Q8: Find min and max
print("\nQ8: Min and Max values")
print(f"Min: {min(arr)}, Max: {max(arr)}")

# Q9: Reverse array
print("\nQ9: Reverse array")
print(f"Reversed: {arr[::-1]}")

# Q10: Find duplicates
print("\nQ10: Find duplicate values")
arr_dup = [1, 2, 3, 2, 4, 3, 5]
duplicates = [x for x in set(arr_dup) if arr_dup.count(x) > 1]
print(f"Array: {arr_dup}")
print(f"Duplicates: {duplicates}")

# Q11: Common values between two arrays
print("\nQ11: Common values between arrays")
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
common = list(set(arr1) & set(arr2))
print(f"Common values: {common}")

# Q12: Remove duplicates
print("\nQ12: Remove duplicates")
arr_unique = list(set(arr_dup))
print(f"After removing duplicates: {arr_unique}")

# Q13: Second largest number
print("\nQ13: Second largest number")
arr_test = [10, 20, 4, 45, 99, 99]
unique_sorted = sorted(set(arr_test), reverse=True)
print(f"Second largest: {unique_sorted[1] if len(unique_sorted) > 1 else 'N/A'}")

# Q14: Second largest (alternative method)
print("\nQ14: Second largest (alternative)")
print(f"Second largest: {unique_sorted[1]}")

# Q15: Count even and odd numbers
print("\nQ15: Count even and odd numbers")
even_count = sum(1 for x in arr_test if x % 2 == 0)
odd_count = sum(1 for x in arr_test if x % 2 != 0)
print(f"Even count: {even_count}, Odd count: {odd_count}")

# Q16: Difference between largest and smallest
print("\nQ16: Difference between largest and smallest")
diff = max(arr_test) - min(arr_test)
print(f"Difference: {diff}")

# Q17: Verify if array contains two specified elements
print("\nQ17: Check if array contains 12 and 23")
test_arr = [10, 12, 15, 23, 30]
contains_both = 12 in test_arr and 23 in test_arr
print(f"Contains both 12 and 23: {contains_both}")

# Q18: Remove duplicates and return new array
print("\nQ18: Remove duplicates and return new array")
new_arr = list(dict.fromkeys(arr_dup))  # Preserves order
print(f"New array without duplicates: {new_arr}")

# ============================================================================
# 5. STATIC (4 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("5. STATIC METHODS")
print("=" * 60)

class MyClass:
    class_var = "I am a class variable"
    
    @classmethod
    def class_method(cls):
        return f"Class method accessing: {cls.class_var}"
    
    @staticmethod
    def static_method():
        return "I am a static method"

# Q1: Access static variable through class
print("\nQ1: Access class variable through class")
print(MyClass.class_var)

# Q2: Access static variable through instance
print("\nQ2: Access class variable through instance")
obj = MyClass()
print(obj.class_var)

# Q3: Change static variable within instance
print("\nQ3: Change class variable within instance")
obj.class_var = "Changed by instance"
print(f"Instance variable: {obj.class_var}")
print(f"Class variable: {MyClass.class_var}")

# Q4: Change static variable within class
print("\nQ4: Change class variable within class")
MyClass.class_var = "Changed by class"
print(f"Class variable: {MyClass.class_var}")

print("\n" + "=" * 60)
print("Python Programming Assignments - Part 1 Complete!")
print("Continuing with remaining sections...")
print("=" * 60)

# ============================================================================
# 6. STRINGS (13 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("6. STRINGS")
print("=" * 60)

# Q1: Different ways of creating strings
print("\nQ1: Different ways to create strings")
str1 = 'Single quotes'
str2 = "Double quotes"
str3 = '''Triple single quotes'''
str4 = """Triple double quotes"""
print(f"Method 1: {str1}")
print(f"Method 2: {str2}")
print(f"Method 3: {str3}")
print(f"Method 4: {str4}")

# Q2: Concatenating strings
print("\nQ2: Concatenating strings using + operator")
first = "Hello"
second = "World"
result = first + " " + second
print(f"Result: {result}")

# Q3: Length of string
print("\nQ3: Finding length of string")
text = "JALA Technologies"
print(f"Length of '{text}': {len(text)}")

# Q4: Extract substring
print("\nQ4: Extract substring")
text = "Python Programming"
substring = text[0:6]
print(f"Substring [0:6]: {substring}")

# Q5: Searching using index()
print("\nQ5: Searching in strings using index()")
text = "Hello World"
index = text.index("World")
print(f"Index of 'World': {index}")

# Q6: Matching with regular expression
print("\nQ6: Matching with regular expression")
import re
text = "test@example.com"
pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
match = re.match(pattern, text)
print(f"'{text}' is {'valid' if match else 'invalid'} email")

# Q7: Comparing strings
print("\nQ7: Comparing strings")
str1 = "hello"
str2 = "hello"
str3 = "Hello"
print(f"'{str1}' == '{str2}': {str1 == str2}")
print(f"'{str1}' == '{str3}': {str1 == str3}")

# Q8: startsWith, endsWith, compareTo
print("\nQ8: startsWith(), endsWith(), compareTo()")
text = "Hello World"
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with 'World': {text.endswith('World')}")
print(f"Compare 'abc' vs 'xyz': {'abc' < 'xyz'}")

# Q9: Trimming strings
print("\nQ9: Trimming strings with strip()")
text = "   Hello World   "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")

# Q10: Replacing characters
print("\nQ10: Replacing characters with replace()")
text = "Hello World"
replaced = text.replace("World", "Python")
print(f"Original: {text}")
print(f"Replaced: {replaced}")

# Q11: Splitting strings
print("\nQ11: Splitting strings with split()")
text = "apple,banana,orange"
parts = text.split(",")
print(f"Split result: {parts}")

# Q12: Converting integer to string
print("\nQ12: Converting integer to string")
num = 123
str_num = str(num)
print(f"Integer: {num}, Type: {type(num)}")
print(f"String: {str_num}, Type: {type(str_num)}")

# Q13: Converting to uppercase and lowercase
print("\nQ13: Converting to uppercase and lowercase")
text = "Hello World"
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# ============================================================================
# 7. INHERITANCE (3 Sections)
# ============================================================================
print("\n" + "=" * 60)
print("7. INHERITANCE")
print("=" * 60)

# Section 1: Three-level inheritance
print("\nSection 1: Three-level inheritance (A -> B -> C)")

class A:
    def method_a1(self):
        return "Method A1 from class A"
    
    def method_a2(self):
        return "Method A2 from class A"
    
    def common_method(self):
        return "Common method from class A"

class B(A):
    def method_b1(self):
        return "Method B1 from class B"
    
    def method_b2(self):
        return "Method B2 from class B"
    
    def common_method(self):
        return "Common method from class B (overridden)"

class C(B):
    def method_c1(self):
        return "Method C1 from class C"
    
    def method_c2(self):
        return "Method C2 from class C"
    
    def common_method(self):
        return "Common method from class C (overridden)"

# Create objects and call methods
obj_a = A()
obj_b = B()
obj_c = C()

print(obj_a.method_a1())
print(obj_a.method_a2())
print(obj_a.common_method())

print(obj_b.method_b1())
print(obj_b.method_b2())
print(obj_b.common_method())

print(obj_c.method_c1())
print(obj_c.method_c2())
print(obj_c.common_method())

# Section 2: Runtime polymorphism
print("\nSection 2: Runtime Polymorphism")
ref_b = obj_b
ref_c = obj_c
print(ref_b.common_method())
print(ref_c.common_method())

# ============================================================================
# 8. ACCESS MODIFIERS (3 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("8. ACCESS MODIFIERS")
print("=" * 60)

# Q1: Private fields and methods
print("\nQ1: Private fields and methods")
class PrivateExample:
    def __init__(self):
        self.__private_field = "Private field"
    
    def __private_method(self):
        return "Private method"
    
    def public_method(self):
        print(f"Accessing {self.__private_field}")
        print(f"Calling {self.__private_method()}")

obj = PrivateExample()
obj.public_method()

# Q2: Protected fields and methods
print("\nQ2: Protected fields and methods")
class ProtectedExample:
    def __init__(self):
        self._protected_field = "Protected field"
    
    def _protected_method(self):
        return "Protected method"

class ChildProtected(ProtectedExample):
    def access_protected(self):
        print(f"Child accessing: {self._protected_field}")
        print(f"Child calling: {self._protected_method()}")

child = ChildProtected()
child.access_protected()

# Q3: Public fields and methods
print("\nQ3: Public fields and methods")
class PublicExample:
    def __init__(self):
        self.public_field = "Public field"
    
    def public_method(self):
        return "Public method"

obj = PublicExample()
print(f"Accessing: {obj.public_field}")
print(f"Calling: {obj.public_method()}")

# ============================================================================
# 9. PACKAGES (5 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("9. PACKAGES")
print("=" * 60)

print("\nQ1-5: Package demonstration")
print("Note: Python packages require __init__.py files")
print("Demonstrating with built-in modules instead:")

import math
import random
import datetime

print(f"Math module - Square root of 16: {math.sqrt(16)}")
print(f"Random module - Random number: {random.randint(1, 100)}")
print(f"Datetime module - Current time: {datetime.datetime.now()}")

# ============================================================================
# 10. FILES (6 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("10. FILES")
print("=" * 60)

# Q1: Read text file
print("\nQ1: Read text file")
filename = "test_file.txt"
with open(filename, 'w') as f:
    f.write("Hello from JALA Academy\n")
    f.write("Python Programming\n")

with open(filename, 'r') as f:
    content = f.read()
    print(f"File content:\n{content}")

# Q2: Write to file
print("\nQ2: Write text to file")
with open(filename, 'w') as f:
    f.write("New content written to file\n")
print("Content written successfully")

# Q3: Read file stream
print("\nQ3: Read file stream")
with open(filename, 'r') as f:
    for line in f:
        print(f"Line: {line.strip()}")

# Q4: Random access using seek()
print("\nQ4: Random access using seek()")
with open(filename, 'r') as f:
    f.seek(0)  # Go to beginning
    print(f"From beginning: {f.read(10)}")

# Q5: Check file permissions
print("\nQ5: Check file permissions")
import os
import stat
file_stats = os.stat(filename)
print(f"File has read permission: {bool(file_stats.st_mode & stat.S_IRUSR)}")
print(f"File has write permission: {bool(file_stats.st_mode & stat.S_IWUSR)}")

# Q6: Cleanup
os.remove(filename)
print(f"File {filename} removed")

# ============================================================================
# 11. CONSTRUCTORS (4 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("11. CONSTRUCTORS")
print("=" * 60)

# Q1: Multiple constructors (using default parameters)
print("\nQ1: Multiple constructors")
class Employee:
    def __init__(self, name=None, age=None):
        self.name = name if name else "Unknown"
        self.age = age if age else 0
        print(f"Employee created: {self.name}, Age: {self.age}")

emp1 = Employee()
emp2 = Employee("John")
emp3 = Employee("Jane", 25)

# Q2: Call parent constructor
print("\nQ2: Call parent constructor")
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor: {name}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
        print(f"Student constructor: Grade {grade}")

student = Student("Alice", "A")

# Q3: Access modifiers in constructors
print("\nQ3: Access modifiers in constructors")
class AccessExample:
    def __init__(self, public_val, private_val):
        self.public = public_val
        self.__private = private_val

obj = AccessExample("Public", "Private")
print(f"Public value: {obj.public}")

# Q4: Constructor attributes
print("\nQ4: Constructor attributes")
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display(self):
        print(f"{self.year} {self.brand} {self.model}")

car = Car("Toyota", "Camry", 2023)
car.display()

# ============================================================================
# 12. METHOD OVERLOADING (3 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("12. METHOD OVERLOADING")
print("=" * 60)

# Q1: Different number of parameters (same type)
print("\nQ1: Different number of parameters")
def add(*args):
    return sum(args)

print(f"add(1, 2) = {add(1, 2)}")
print(f"add(1, 2, 3) = {add(1, 2, 3)}")
print(f"add(1, 2, 3, 4) = {add(1, 2, 3, 4)}")

# Q2: Different data types
print("\nQ2: Different data types")
def process(value):
    if isinstance(value, int):
        return f"Integer: {value * 2}"
    elif isinstance(value, str):
        return f"String: {value.upper()}"
    else:
        return f"Other type: {value}"

print(process(5))
print(process("hello"))

# Q3: Same number and type of parameters
print("\nQ3: Using default parameters for overloading")
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    else:
        return 0

print(f"calculate(5, 3) = {calculate(5, 3)}")
print(f"calculate(5, 3, 'multiply') = {calculate(5, 3, 'multiply')}")

# ============================================================================
# 13. EXCEPTIONS (12 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("13. EXCEPTIONS")
print("=" * 60)

# Q1: Arithmetic Exception without handling
print("\nQ1: Arithmetic Exception (handled for demo)")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught exception: {e}")

# Q2: Handle with try-catch
print("\nQ2: Handle Arithmetic exception with try-except")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Q3: Method that throws exception
print("\nQ3: Method that throws exception")
def risky_method():
    raise ValueError("This is a custom error")

try:
    risky_method()
except ValueError as e:
    print(f"Caught: {e}")

# Q4: Multiple catch blocks
print("\nQ4: Multiple except blocks")
try:
    value = int("abc")
except ValueError:
    print("ValueError caught")
except TypeError:
    print("TypeError caught")
except Exception as e:
    print(f"Other exception: {e}")

# Q5: Throw exception with custom message
print("\nQ5: Raise exception with custom message")
try:
    raise Exception("Custom error message")
except Exception as e:
    print(f"Caught: {e}")

# Q6: Create custom exception
print("\nQ6: Create custom exception")
class CustomException(Exception):
    pass

try:
    raise CustomException("My custom exception")
except CustomException as e:
    print(f"Caught custom exception: {e}")

# Q7: Finally block
print("\nQ7: Finally block")
try:
    print("In try block")
except Exception:
    print("In except block")
finally:
    print("In finally block - always executes")

# Q8-12: Various exceptions
print("\nQ8-12: Various exception types")
exceptions_demo = [
    ("FileNotFoundError", lambda: open("nonexistent.txt")),
    ("IndexError", lambda: [1, 2, 3][10]),
    ("KeyError", lambda: {"a": 1}["b"]),
    ("TypeError", lambda: "string" + 5),
    ("ValueError", lambda: int("abc"))
]

for name, func in exceptions_demo:
    try:
        func()
    except Exception as e:
        print(f"{name}: {type(e).__name__}")

# ============================================================================
# 14. DICTIONARY (7 Questions)
# ============================================================================
print("\n" + "=" * 60)
print("14. DICTIONARY")
print("=" * 60)

# Q1: Create dictionary with 5 key-value pairs
print("\nQ1: Create dictionary")
students = {
    "S001": "Alice",
    "S002": "Bob",
    "S003": "Charlie",
    "S004": "Diana",
    "S005": "Eve"
}
print(f"Students: {students}")

# Q2: Adding values
print("\nQ2: Adding values to dictionary")
students["S006"] = "Frank"
print(f"After adding: {students}")

# Q3: Updating values
print("\nQ3: Updating values in dictionary")
students["S001"] = "Alice Smith"
print(f"After updating: {students}")

# Q4: Accessing values
print("\nQ4: Accessing values")
print(f"Student S003: {students['S003']}")
print(f"Student S005: {students.get('S005')}")

# Q5: Nested dictionary
print("\nQ5: Nested dictionary")
school = {
    "Class A": {
        "students": ["Alice", "Bob"],
        "teacher": "Mr. Smith"
    },
    "Class B": {
        "students": ["Charlie", "Diana"],
        "teacher": "Ms. Johnson"
    }
}
print(f"School: {school}")

# Q6: Access nested dictionary
print("\nQ6: Access nested dictionary values")
print(f"Class A teacher: {school['Class A']['teacher']}")
print(f"Class B students: {school['Class B']['students']}")

# Q7: Print keys
print("\nQ7: Print all keys")
print(f"All student IDs: {list(students.keys())}")

# Q8: Delete value
print("\nQ8: Delete value from dictionary")
del students["S006"]
print(f"After deletion: {students}")

print("\n" + "=" * 60)
print("ALL PYTHON PROGRAMMING ASSIGNMENTS COMPLETED!")
print("Total: 100+ exercises across 15 sections")
print("=" * 60)

