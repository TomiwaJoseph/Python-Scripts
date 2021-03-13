'''
If the repeated sum of squares of a digits of a number is equal to 1,
it is considered to be happy.
Note: if the sum of squares reaches 4, 1 can never be reached.

Example:

Input: 23
2**2 + 3**2 = 13
1**2 + 3**2 = 10
1**2 + 0**2 = 1
Output: True

'''
print()

def happy(number):
    if number == '0':
        return False
    num = number
    while 1:
        splitted = list(str(num))
        sum_of_squares = []
        for squares in splitted:
            sum_of_squares.append(int(squares)**2)
        num = sum(sum_of_squares)
        if num == 1:
            return True
        elif num == 4:
            return False


entry = input('Enter your number: ') or '23'
print(entry)
print(happy(entry))
print()

print('Happy numbers within your input range are:')

happy_range = [i for i in range(1, int(entry)) if happy(str(i))]
print(happy_range)