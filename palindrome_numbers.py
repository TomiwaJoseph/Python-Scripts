'''
A Palindromic number is a number that is the same when written forwards or backwards.
Create a program that takes a number and output whether or not it is palindromic or
not.

Example:

Input: 10
645 - False
656 - True

'''
print()

def palindromic(number):
    return number == number[::-1]


entry = input('Enter your number: ') or '101'
print(palindromic(entry))
print()
