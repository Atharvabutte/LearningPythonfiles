# using format function
import string


letters = "Hey this is my first program & i write on {0}"
Date = "22/05/2005"
print(letters.format(Date))

# Using f-string 
st = "f-string"
Sta = f"Hey this is my first program on {st}"
print(Sta)

# /example 2

name = "Atharva balasaheb butte"
Course ="BE"
clgName ="Atharva Clg of Enginerring"
print(f"By using f-string function we print as: I am {name} and studying in {Course} on {clgName}")


# video 30: Recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive approach

print(fibonacci(6))
print(fibonacci(5))
print(fibonacci(4))
print(fibonacci(3))
print(fibonacci(2))
print(fibonacci(1))
print(fibonacci(0))