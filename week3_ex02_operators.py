# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 2
x += 8
print(x)

# TODO: Multiply y by 2 using the *= operator
y = 12
y *= 3
print(y)

# TODO: Divide x by y and store the result in a variable called 'result'
result = x/y

# TODO: Print the value of 'result'
print(float(f"{result:.2f}"))

# Question 2: Comparison and Logical Operators
a = 10
b = 23

# TODO: Create a condition that checks if a is greater than b

a_greater_than_b = a > b
print(a_greater_than_b)

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b_is_even = b % 2 == 0
print(b_is_even)

if b % 2 == 0:
    print("b is even")
else:
    print("b is odd")   

# TODO: Create a condition that checks if c is less than or equal to a
c = 15
c_less_than_or_equal_to_a = c <= a
print(c_less_than_or_equal_to_a)

if c <= a:
    print("c is less than or equal to a")
else:
    print("c is greater than a")

# TODO: Combine the above conditions using logical operators to create a 'final_condition'


# Question 3: Conditional Statements

score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Question 4: Combining Operators and Conditionals

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")
    