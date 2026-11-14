# Question 1: Variable Assignment and String Manipulation

#Ask the user for their name and store it in a variable
name = input("What is your name? " )

#Ask the user for their age and store it in a variable
age = input("How old are you?" )

#Print a greeting using the name and age variables
print(f"\nHello, {name}! You are {age} years old.\n")

# Question 2: Integer Operations

#Ask the user for the length of a rectangle and store it as an integer

length = int(input("How long is the rectangle? "))

#Ask the user for the width of a rectangle and store it as an integer
width = int(input("How wide is the rectange? "))

#Calculate the area of the rectangle
area = length * width

#Print the result
print(f"\nYour rectangle has an area of area of {area} square units.")


# Question 3: Working with Floats

temperature_c = float(input("\nEnter a temperature in Celsius "))
temperature_f = temperature_c * 9/5 + 32
temperature = print(f"\nToday's temperature is {temperature_c:.2f} in Celsius and {temperature_f:.2f} in Fahrenheit.")

print(temperature)

# some if else and elif examples

num = int(input("\nEnter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

 # ?another example: nested if with logical operators
age = int(input("\nEnter your age: "))
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are a minor.")
