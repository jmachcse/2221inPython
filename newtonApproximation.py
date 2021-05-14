# Jeremy Mach

# Function to approximate a square root using Newton's algorithm
def sqrt(x):

    estimate = float(x)
    approximation = 1.0
    while abs(approximation - (estimate / approximation)) > (0.0001 * approximation):
        approximation = 0.5 * (approximation + (float(x) / approximation))

    # When the approximation is less than 0.0001 * approximation,
    # the approximation will be returned as the guess for the square root
    return approximation


userAns = input("Would you like to calculate a square root? : ")

while userAns == "Y" or userAns == "y":
    userNum = input(
        "Please enter the number you would like to calculate the square root of: ")
    float(userNum)

    sqrt = sqrt(userNum)

    print("The square root of your number using Newton Iteration is " + str(sqrt))

    userAns = input("Would you like to calculate another square root? (Y/N): ")
print("Goodbye!")
