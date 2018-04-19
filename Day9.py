import sys

def factorial(n):
    fact=n
    for i in range(n-1,1,-1):
        fact=fact*i
    return fact

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
