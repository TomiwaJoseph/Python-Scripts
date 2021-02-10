'''
A Fisher number is an integer whose multiplication of its multipliers are equal to the number's cube

Example:
Input: 12
multiplications of the multipliers of 12 are 1,2,3,4,6,12 == 1728
12 cubed == 1728
Output: True

Input: 18
multiplications of the multipliers of 18 are 1,2,3,6,9,18 == 5832
18 cubed == 5832
Output: True

'''
print()

def check_fisher(number):
    multiplications = 1
    for num in range(1,number+1):
        if number % num == 0:
            multiplications *= num
    return multiplications == number ** 3

entry = int(input('Enter a number: '))
print(check_fisher(entry))
print()

print('Fisher numbers within your input range are:')

fisher_range = [i for i in range(1,entry) if check_fisher(i)]
print(fisher_range)
