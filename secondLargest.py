# Jeremy Mach


# Function to find the second largest number in the list
def secondLargest(l):
    largestIndex = 0
    secondLargestIndex = 0

    for i in range(0, len(l)):
        if l[i] > l[largestIndex]:
            secondLargestIndex = largestIndex
            largestIndex = i
        else:
            secondLargestIndex = i
    for i in range(0, len(l)):
        if i != largestIndex:
            if l[i] > l[secondLargestIndex]:
                secondLargestIndex = i
    return l[secondLargestIndex]


a = [1, 5, -7, 4, 1]
b = [1, 5, -7, 4, 5]
c = [-2, -3, -8, -4, -5]
d = [1, 0, -7, 0, -5]

print("Second largest of a is: " + str(secondLargest(a)))
print("Second largest of a is: " + str(secondLargest(b)))
print("Second largest of a is: " + str(secondLargest(c)))
print("Second largest of a is: " + str(secondLargest(d)))


