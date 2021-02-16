'''
A perfect number is a positive integer that is equal to the sum of its proper positive
divisors excluding the number itself

Example:
Input: 6
Output: True(positive divisors excluding 6 are 1,2,3 their addition is 6)

Input: 28
Output: True(positive divisors excluding 28 are 1,2,4,7,14 their addition is 28)

'''

def check_perfect(number):
    divisors = [i for i in range(1,number) if number%i==0]
    addition = sum(divisors)
    return addition == number

entry = int(input('Enter your number: '))
print(check_perfect(entry))
print()

print('Perfect numbers within your input range are:')

perfect_range = [i for i in range(1,entry) if check_perfect(i)]
print(perfect_range)
