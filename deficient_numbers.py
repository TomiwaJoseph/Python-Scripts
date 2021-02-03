'''
A number is considered deficient if the sum of its factors is less than that
number itself.

Example:
16 is a deficient number
factors of 16 are 1, 2, 4, 8
sum of the factors is 15
15 is less than 16
Output: True

18 is not a deficient number
factors of 18 are 1, 2, 3, 6, 9
sum of the factors is 21
21 is greater than 18
Output: False

'''

def deficient(number):
    # find the factors
    factors = [i for i in range(1,number) if not number % i]
    add_factors = sum(factors)
    return add_factors < number

entry = int(input('Enter a number: '))
print(deficient(entry))
