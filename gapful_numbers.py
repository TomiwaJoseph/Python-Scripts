'''
A gapful number is a number of at least 3 digits that is divisible without
remainder by the number formed by the first and the last digit of the original number.

Examples:
Input: 100
Output: True (100 is gapful because it is divisible by 10)

Input: 583
Output: True (583 is gapful because it is divisible by 53)

Input: 230
Output: False (230 is gapful because it is not divisible by 20)

'''

def check_gapful(number):
    # Convert the number to a string to retrieve first and last digit
    num_str = str(number)
    first, last = num_str[0], num_str[-1]
    num_int = int(first+last)
    return number % num_int == 0

entry = int(input('Enter a three digit number: '))
print(check_gapful(entry))

