import turtle
import math
alice = turtle.Turtle()

def square(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

square(alice, 7, 50)
print (math.pi)

x = 100
if x%2 == 0:
    print ("x is positive")
else:
    print ("x is negative")


