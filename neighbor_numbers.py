'''
Given two strings as input, write a program to find which numbers from the first string
are present in the second string. Print the result as a string containing the matched
numbers in ascending order.

Example:

Input: 10
"12,13,15,2021"
"13,556,12,23,2021,34"
Output:
"12,13,2021"

'''
print()

def neighbor(number1, number2):
    ent_1 = number1.split(',')
    ent_2 = number2.split(',')
    neighbors = ",".join([i for i in ent_1 if i in ent_2])
    return neighbors

entry1 = input('Enter your number: ') or "12,13,15,2021"
entry2 = input('Enter your number: ') or "13,556,12,23,2021,34"
print(neighbor(entry1, entry2))
print()

print()