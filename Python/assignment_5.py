# take inputs from user for name and n
name = input("Enter your name: ")
n = int(input("Enter the number of characters to print from left: "))

def display_from_left(name, n):
    """Display n(number of userinput to print) characters from left."""
    print("Characters from the left:", name[:n])

def count_vowels(name):
    """Count the number of vowels."""
    vowels = 'AaEeIiOoUu' # to perfom vowels check
    vowel_count = 0  # Initialize the vowel count
    for char in name:
        if char in vowels:
            vowel_count += 1  #  if character is a vowel, it will increase 1 to vowel_count
    print("Number of vowels:", vowel_count)


def reverse_name(name):
    """Reverse name."""
    reversed_name = name[::-1] # Reversing String by using string slice
    print("Reversed name:", reversed_name)

display_from_left(name, 3)
count_vowels(name)
reverse_name(name)
