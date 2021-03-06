'''
A Pronic number is a number which is the product of two consecutive integers, that is
n = x*(x+1)

Example:

Input: 6
Output: True (6 = 2*(2+1))

Input: 42
Output: True (42 = 6*(6+1))

'''
print()


def pronic(number):
    know = []
    for i in range(number):
        if i*(i+1) == number:
            know.append(i)
            break
    return bool(know)


entry = int(input('Enter your number: ') or '56')
print(pronic(entry))
print()

print('Pronic numbers within your input range are:')

compo_range = [i for i in range(entry) if pronic(i)]
print(compo_range)
print()
