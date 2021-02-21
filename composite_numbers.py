'''
A composite number is a positive integer that is not prime. In other words, it
is a positive integer that has at least one divisor other than 1 and itself.
The composite numbers up to 20 are 4,6,8,9,10,12,14,15,16,18,20

Example:

Input: 10
Output: True (10 has divisors other than 1 and itself, for example, 2 or 5)

Input: 5
Output: False (5 is a prime number and it has no other divisors other than 1 and itself)

'''
print()

def know_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))

def composite(number):
    if know_prime(number):
        return False
    # Find out if it has factors other than 1 and itself
    return bool([i for i in range(2,number+1) if number%i == 0])


entry = int(input('Enter your number: '))
print(composite(entry))
print()

print('Composite numbers within your input range are:')

compo_range = [i for i in range(entry) if composite(i)]
print(compo_range)
print()
