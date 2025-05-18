# -------------------------------------------
# Build a Simple Calculator in Python Part 2
# -------------------------------------------

# Step 1: Get user input
num1 = float(input("Enter the First Number: "))
operator = input("Please Enter the Operator (+, -, *, /, %): ")
num2 = float(input("Enter the Second Number: "))

# Step 2: Perform calculation based on the operator

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print("Result (modulus):", result)
    else:
        print("Error: Modulus by zero is not allowed.")

else:
    print("Error: Wrong Operator. Please use +, -, *, /, or %.")

# ---------------------------------------
# Notes:
# - % (modulus) gives the remainder of the division.
# - For example: 10 % 3 = 1
# ---------------------------------------

print("hiii")







