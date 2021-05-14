# Jeremy Mach


# Function to print the height of the triangle
def triangle(n):

    # Spaces are determined based off of how tall the user specified the input to be
    spaces = n + 1

    # A couple of nested loops to print the spaces and the stars. After each space is printed, one less space will be printed and one more star will be printed.
    for i in range(0, spaces):
        for _ in range(0, spaces):
            print(end=" ")
        spaces = spaces - 1

        for _ in range(0, i+1):
            print("* ", end="")
        print("\r")


# Driver Code
n = int(input("How tall would you like your triangle? Enter here: "))
triangle(n)
