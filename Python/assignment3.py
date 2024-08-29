# This function will expects positive input
def positive(userinput):
    if userinput <= 0: # if the input is less than or equal 0, it will output "Blastoff!"
        print('Blastoff!')
    else: # Else, if the input is greater than 0 and a negative value, the code will execute.
        print(userinput)
        positive(userinput - 1) #this will count down 1 from input and call the 'negative' function until it become 0.

# This function will expects positive input
def negative(userinput):
    if userinput >= 0: # if the input is greater than or equal 0, it will output "Blastoff!"
        print('Blastoff!')
    else: # Else, if the input is less than 0 and a negative value, the code will execute.
        print(userinput)
        negative(userinput + 1) #this will count up 1 to input and call the 'negative' function until it become 0.
    
number = int(input('type your number\n')) # taking a input for number

if number > 0: # If the number is greater than 0, this will call 'positive' function
    positive(number)
elif number < 0: # If the number is less than 0, this will call 'negative' function
    negative(number)
else: # If number is equal to zero, it will print this followings
    print('Your number is not count! May be Zero!')




def division():
    numerator = float(input("Enter a number for numerator.")) # take a numerator number in float and store in variable
    denominator = float(input("Enter a number for denominator.")) # take a denominator number in float and store in variable

    # Condition to check the denominator
    if (denominator == 0): # if denominator is 0, it will output an error message
        return print("Error: Divide by 0 is not allowed")
    result = numerator / denominator # otherwise, it will perform division

    print(f"The result is {result}") # print out!

division() # function call211221