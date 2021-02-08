'''
A number is considered Harshad if it is divisible by the sum of 
its digits.

Example:

Input: 18
1 + 8 = 9, 18 is divisible by 9
Output: True

Input: 48
4 + 8 = 12, 48 is divisible by 12
Output: True

Input: 1729
1 + 7 + 2 + 9 = 19, 1729 is divisible by 19
Output: True

'''
print()


def harshad(number):
    addition = sum([int(digits) for digits in str(number)])
    return number % addition == 0


entry = int(input('Enter your number: '))
print(harshad(entry))
print()

print('Harshad numbers within your input range are:')

harsh_range = [i for i in range(1,entry) if harshad(i)]
print(harsh_range)
