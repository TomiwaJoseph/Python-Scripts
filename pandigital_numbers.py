'''
If a number contains each of the digits from 0 to 9 at least
once (0 not being the leading digit), it is considered to be
pandigital.

Example:

Input: 12345678902414
Output: True 
(input does not start with 0 and all digits from 0-9 are present)

Input: 1234567802435
Output: False (9 is missing)

'''
print()


def pandigital(number):
    if len(number) < 10 or number.startswith('0'):
        return False
    standard = list('0123456789')
    entry = sorted(list(set(list(number))))
    return standard == entry


entry = input('Enter your number: ') or '234562789604'
print(pandigital(entry))

print('\nBonus:')
print('How many times each number appear: ')
standard = list('0123456789')
for i in sorted(list(set(list(entry)))):
    print(i,'appeared',entry.count(i),'times')

missing = [i for i in standard if i not in entry]
if missing:
    print('\nThese number(s) are missing:')
    print(missing)