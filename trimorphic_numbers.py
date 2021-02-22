'''
A Trimorphic number is a number whose cube ends in the number itself

Example:

Input: 4
Output: True (4 ^ 3 is 64, which ends in 4)

Input: 25
Output: True (5 ^ 3 is 15625, which ends in 25)

'''
print()

def trimorphic(number):
    # find the cube
    cubed = number ** 3
    # check if the cubed ends with the number
    return str(cubed).endswith(str(number))


entry = int(input('Enter your number: ') or 25)
print(trimorphic(entry))
print()

print('Trimorphic numbers within your input range are:')

trimo_range = [i for i in range(entry) if trimorphic(i)]
print(trimo_range)
print()
