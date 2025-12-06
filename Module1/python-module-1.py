
# --- Python Syntax ---
print("=== PYTHON SYNTAX ===")
print("Hello, World!")  # Simple print statement
x = 5  # Integer assignment
y = "Hello"  # String assignment
print(x, y)  # Print multiple variables

# --- Python Output ---
print("\n=== PYTHON OUTPUT ===")
print("This is output to console")  # Standard output
print("Multiple", "items", "separated", "by commas")  # Print with commas
print("Item with end character", end="!\n")  # Custom end character

# --- Python Comments ---
print("\n=== PYTHON COMMENTS ===")
# This is a single line comment
"""
This is a multi-line comment
or docstring
"""
x = 5  # Inline comment

# --- Python Variables ---
print("\n=== PYTHON VARIABLES ===")
# Variable assignment
name = "John"  # String
age = 25  # Integer
height = 5.11  # Float
is_student = True  # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Multiple assignment in one line
a, b, c = 1, 2, "three"
print(a, b, c)

# --- Python Data Types ---
print("\n=== PYTHON DATA TYPES ===")
# Numeric types
int_num = 10  # Integer
float_num = 10.5  # Float
complex_num = 3 + 4j  # Complex number

# Text type
text = "Hello Python"  # String

# Boolean type
is_true = True
is_false = False

# Sequence types
my_list = [1, 2, 3]  # List
my_tuple = (1, 2, 3)  # Tuple
my_range = range(5)  # Range

# Mapping type
my_dict = {"name": "John", "age": 30}  # Dictionary

# Set types
my_set = {1, 2, 3}  # Set
my_frozenset = frozenset([1, 2, 3])  # Frozenset

# Binary types
bytes_data = b"hello"  # Bytes
bytearray_data = bytearray(5)  # Bytearray
memoryview_data = memoryview(bytes_data)  # Memoryview

print("Integer:", int_num, type(int_num))
print("Float:", float_num, type(float_num))
print("String:", text, type(text))
print("List:", my_list, type(my_list))

# --- Python Numbers ---
print("\n=== PYTHON NUMBERS ===")
# Integer operations
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)  # Floating point division
print("Floor Division:", x // y)  # Integer division
print("Modulus:", x % y)  # Remainder
print("Exponent:", x ** y)  # Power

# Float operations
pi = 3.14159
radius = 5.0
area = pi * (radius ** 2)  # Area of a circle
print("Area of circle:", area)

# Complex numbers
c1 = 2 + 3j
c2 = 1 - 2j
print("Complex addition:", c1 + c2)
print("Complex multiplication:", c1 * c2)

# Python Casting
print("\n=== PYTHON CASTING ===")
# Convert between types
x = 10
y = "20"
z = 3.14

# String to integer
str_to_int = int(y)
print("String to int:", str_to_int, type(str_to_int))

# Integer to string
int_to_str = str(x)
print("Int to string:", int_to_str, type(int_to_str))

# Float to integer
float_to_int = int(z)
print("Float to int:", float_to_int, type(float_to_int))

# Integer to float
int_to_float = float(x)
print("Int to float:", int_to_float, type(int_to_float))

# Python Strings
print("\n=== PYTHON STRINGS ===")
# String creation
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a 
multi-line string"""

print(single_quote)
print(double_quote)
print(triple_quote)

# String operations
text = "Python Programming"
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Slicing:", text[0:6])
print("Contains 'Python':", "Python" in text)
print("Replace:", text.replace("Python", "Java"))

# String formatting
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")  # f-string (Python 3.6+)

# Python Booleans
print("\n=== PYTHON BOOLEANS ===")
# Boolean values
true_value = True
false_value = False

print("True:", true_value)
print("False:", false_value)

# Boolean operations
print("AND:", True and False)
print("OR:", True or False)
print("NOT:", not True)

# Boolean from comparisons
x = 10
y = 5
print("x > y:", x > y)
print("x == y:", x == y)
print("x != y:", x != y)

# Truthy and Falsy values
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(''):", bool(""))
print("bool('Hello'):", bool("Hello"))
print("bool([]):", bool([]))
print("bool([1,2]):", bool([1,2]))

# Python Operators
print("\n=== PYTHON OPERATORS ===")
# Arithmetic operators
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# Comparison operators
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical operators
x, y = True, False
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# Assignment operators
c = 5
c += 3  # c = c + 3
print("c += 3:", c)
c *= 2  # c = c * 2
print("c *= 2:", c)

# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list2:", list1 is not list2)

# Membership operators
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits:", "apple" in fruits)
print("'mango' not in fruits:", "mango" not in fruits)

# Python Lists
print("\n=== PYTHON LISTS ===")
# List creation
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# List operations
fruits.append("orange")
print("After append:", fruits)

fruits.insert(1, "mango")
print("After insert:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

popped = fruits.pop()
print("Popped item:", popped)
print("After pop:", fruits)

# List slicing
print("First two:", numbers[:2])
print("Last two:", numbers[-2:])
print("Every second item:", numbers[::2])

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)