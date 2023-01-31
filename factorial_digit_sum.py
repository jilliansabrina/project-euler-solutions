"""
Project Euler
Problem 20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(num):
    if num > 0:
        return num * factorial(num - 1)
    else:
        return 1

def digitSum(num):
    digit_sum = 0
    for i in str(num):
        digit_sum += int(i)
    return digit_sum

# Answer is 648.
print(f'The factorial digit sum of 100 is: {digitSum(factorial(100))}')
