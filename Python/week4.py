# import math

# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x

# print(absolute_value(-200))


# def number(x, y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1
# print(number(51, 5))


# def distance(x1, x2, y1, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     result = math.sqrt(dsquared)
#     return result
# print(distance(1, 2, 5, 6))


# def is_divisible(x, y):
#     return x%y == 0
# print(is_divisible(2, 2))


# def is_between(x, y, z):
#     if x <= y <= z:
#         return True
#     else:
#         return False
# print(is_between(10, 20, 30))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))