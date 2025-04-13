# Task1

Num = int(input("Enter a number: "))


def factorial (n):
    if n < 2:
        return 1
    
    else:
        return  n * (factorial(n-1))
    
result = factorial(5)
print(f"factorial of {Num} is:", result)

