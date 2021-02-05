'''
An emirp is a prime that results in a different prime when its decimal digits
are reversed.

Example:

Input: 13
Output: True (13 and 31 are prime numbers)

Input: 23
Output: False (23 is prime but 32 is not)

Input: 113
Output: True (113 and 311 are prime numbers)

'''
print()

def know_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))


def emirp(number):
    reversed = int(str(number)[::-1])
    # find if the number and its reverse is prime
    return know_prime(number) and know_prime(reversed)


entry = int(input('Enter your number: '))
print(emirp(entry))
print()

print('Emirp numbers within your input range are:')

emirp_range = [i for i in range(entry) if emirp(i)]
print(emirp_range)
