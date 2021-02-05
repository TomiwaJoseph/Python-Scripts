'''
A number is a Disarium number if the sum of the powers of its digits equals
the number itself. The digits are powered to their positions in the number.

Examples:
Input: 135
1**1 + 3**2 + 5**3 == 135
Output: True 

Input: 89
8**1 + 9**2 == 89
Output: True 

Input: 137
1**1 + 3**2 + 7**3 != 137
Output: False 

'''
print()

def disarium(number):
    list_to_add = []
    for position, num in enumerate(str(number)):
        raised = int(num) ** (position + 1)
        list_to_add.append(raised)
    return sum(list_to_add) == number

entry = int(input('Enter your number: '))
print(disarium(entry))
print()

print('Disarium numbers within your input range are:')
dis_range = [i for i in range(entry) if disarium(i)]
print(dis_range)
print()

