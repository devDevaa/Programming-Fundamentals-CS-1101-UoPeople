import math # To use math function in the program

def hypotenuse(a, b):
    # Accroding to the formula, I calculate the square of each side firstly.
    square1 = a**2
    square2 = b**2
    # Then, Sum the result of the squared sides length
    sum = square1 + square2
    # for the final result, I make the square root of the sum.
    result = math.sqrt(sum)
    # Print Out the Result
    print("if the input are", a, "and", b, "_ the hypotenuse of the triangle is:", result)

hypotenuse(20, 28)
hypotenuse(5, 6)


