'''
If the square of a number ends with the number itself, it is considered
to be automorphic.

Example:

Input: 25
Output: True (the square of 25 is 625, it ends with 25)

Input: 6
Output: True (the square of 6 is 36, it ends with 6)

'''
print()


def automorphic(number):
    squared = number**2
    return str(squared).endswith(str(number))


entry = int(input('Enter your number: '))
print(automorphic(entry))
print()

print('Automorphic numbers within your input range are:')

automorph_range = [i for i in range(entry) if automorphic(i)]
print(automorph_range)
