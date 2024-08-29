def is_prime(n):
    # Prime number can only be a positive number
    if not isinstance(n, int): # input should be only a number, not string or float number
        return "Invalid input value"
    if n <= 1: # number should be less than or equal 1 and a positive number
        return "Please enter a number greater than 1"
    
    # if the n is diviable by i, it will return false
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 'Your input number is not a Prime number'
    return 'Your input number is a Prime number' # if not, it is a prime number
print(is_prime("10"))
print(is_prime(2.5))
print(is_prime(8))
print(is_prime(3))