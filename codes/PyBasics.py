# Program to show Python basics

def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
        return(1)
    else:
        print(n, "is odd")
        return(0)

num = input("Enter an integer: ")         # Input captures a string
num = int(num)                           # Convert to integer type

val = is_even(num)
print(val)

