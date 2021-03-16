'''
A number is considered Neon if the sum of digits of the square of the number is 
equal to the number itself.

Example:

Input: 9
9 * 9 == 81
8 + 1 == 9
Output: True

'''
print()

def neon(number):
    squared = number ** 2
    sum_of_digits = sum([int(i) for i in str(squared)])
    return sum_of_digits == number 


entry = int(input('Enter your number: ') or '911')
print(entry)
print(neon(entry))
print()

print('Neon numbers within your input range are:')

neon_range = [i for i in range(entry) if neon(i)]
print(neon_range)