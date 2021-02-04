'''
An Armstrong number is a number that is the sum of its own digits each raised
to the power of the number of digits.

Hint:
The first ten Armstrong numbers are 0,1,2,3,4,5,6,7,8,9,153

Examples:
Input: 153
the number of digits in 153 is 3
Therefore: 1**3 + 5**3 + 3**3 == 153
Output: True 

Input: 200
the number of digits in 200 is 3
Therefore: 2**3 + 0**3 + 0**3 != 200
Output: False 

Input: 370
the number of digits in 370 is 3
Therefore: 3**3 + 7**3 + 0**3 == 370
Output: True

'''
print()

def armstrong(number):
    length = len(str(number))
    raised = [int(i)**length for i in str(number)]
    addition = sum(raised)
    return addition == number

entry = int(input('Enter your number: '))
print(armstrong(entry))
print()

print('Armstrong number within your input range are:')

armst_range = [i for i in range(entry) if armstrong(i)]
print(armst_range)

