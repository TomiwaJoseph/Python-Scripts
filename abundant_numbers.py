'''
A number is considered abundant if the sum of its proper divisors is
greater than the number itself

Example:

18 is an abundant number
factors of 18 are 1, 2, 3, 6, 9
sum of the factors is 21
21 is greater than 18
Output: True

16 is not an abundant number
factors of 16 are 1, 2, 4, 8
sum of the factors is 15
15 is less than 16
Output: False

'''

def abundant(number):
    # find the factors
    factors = [i for i in range(1,number) if not number % i]
    add_factors = sum(factors)
    return add_factors > number

entry = int(input('Enter a number: '))
print(abundant(entry))
