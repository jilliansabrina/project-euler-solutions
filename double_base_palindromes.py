# Project Euler
# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def doublePalindromes(ceiling):
    palindromes = 0
    for i in range(ceiling):
        if i == int(str(i)[::-1]):
            # Unnecessary, but removing '0b' from binary string for aesthetic purposes.
            if bin(i)[2:] == bin(i)[:1:-1]:
                palindromes += i
    return palindromes

  
# Answer is 872187    
print(doublePalindromes(1000000))
