'''
A Leyland number is a number which can be expressed as a^b + b^a
where a and b are integers greater than 1

'''
print()

def check_leyland(number):
    numbers = []
    for x in range(2,number):
        for y in range(2, x):
            if x ** y + y ** x == number:
                numbers.append((x,y))
                break
    return bool(numbers)

entry = int(input('Enter your number: '))
print(check_leyland(entry))

print('\nBonus')
if check_leyland(entry):
    print('The two numbers are:')
    print([(x,y) for x in range(2,entry) for y in range(2,x) if x**y + y**x == entry][0])
else:
    print('Your entry is not a Leyland Number')
