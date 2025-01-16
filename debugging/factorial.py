#!/usr/bin/python3
import sys
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(number)
            print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
