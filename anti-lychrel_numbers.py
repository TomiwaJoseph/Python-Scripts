'''
An anti-Lychrel number is a number that forms a palindrome through
the iterative process of repeatedly reversing its digits and adding the
resulting numbers. For example 56 becomes palindromic after one iteration:
56+65=121. If the number doesn't become palindromic after 30 iteratioins,
then it is not an anti-Lychrel number.

Don't be surprised if nearly all the numbers you enter return true! 
The first 3 non anti-lychrel numbers are 196, 295 and 394

Example:

Input: 12
Output: True (12 + 21 = 33, a palindrome)

Input: 57
Output: True (57 + 75 = 132, 132 + 231 = 363, a palindrome)

'''
print()


def anti_lychrel(number):
    num_of_iter = 1
    new_number = number
    while 1:
        split_add = new_number + int(str(new_number)[::-1])
        new_number = split_add
        if num_of_iter == 30:
            return False
        if str(split_add) == str(split_add)[::-1]:
            return True
        else:
            num_of_iter += 1



entry = int(input('Enter your number: ') or '400')
print(anti_lychrel(entry))
print()

print('Bonus')
print('Non Anti-Lychrel numbers within your input range are:')

lychrel_range = [i for i in range(entry) if anti_lychrel(i)]
print([i for i in range(entry) if i not in lychrel_range])

