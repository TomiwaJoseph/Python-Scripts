'''
A number is considered a spy number if the sum and product of its
digits are equal.

Example:

Input: 123
1 + 2 + 3 == 1 * 2 * 3
Output: True

Input: 1412
1 + 4 + 1 + 2 == 1 * 4 * 1 * 2
Output: True

'''
print()

def spy(number):
    addition = sum([int(digit) for digit in str(number)])
    multiplication = 1
    for digit in str(number):
        multiplication *= int(digit)
    return multiplication == addition


# entry = int(input('Enter your number: '))
entry = int(input('Enter your number: '))
print(spy(entry))
print()

print('Spy numbers within your input range are:')

emirp_range = [i for i in range(entry) if spy(i)]
print(emirp_range)
