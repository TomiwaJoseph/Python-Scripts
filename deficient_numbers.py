'''
A number is considered deficient if the sum of its factors is less than twice that
number.

Example:
16 is a deficient number
factors of 16 are 1, 2, 4, 8, 16
sum of the factors is 31
twice of 16 is 32
31 is less than 32

18 is not a deficient number
factors of 18 are 1, 2, 3, 6, 9, 18
sum of the factors is 39
twice of 18 is 36
39 is greater than 36

'''

def deficient(number):
    # find the factors
    factors = [i for i in range(1,number+1) if not number % i]
    add_factors = sum(factors)
    return add_factors < 2 * number

entry = int(input('Enter a number: '))
print(deficient(entry))