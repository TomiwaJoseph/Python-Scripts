'''
A Semiprime number is a natural number that is the product of exactly two
(not necessarily distinct) primes.

Example:

Input: 57
Output: True (57 is the product of 3 * 19)

Input: 121
Output: True (121 is the product of 11 * 11)

'''
print()

def know_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))

def semi_prime(number):
    prime_factors = [i for i in range(3,number) if know_prime(i)]
    semis = [(x,y) for x in prime_factors for y in prime_factors if x*y == number]
    return bool(semis)


entry = int(input('Enter your number: ') or '33')
if semi_prime(entry):
    print(semi_prime(entry))
    prime_factors = [i for i in range(3,entry) if know_prime(i)]
    print('The two number are:',[(x,y) for x in prime_factors for y in prime_factors if x*y == entry][0])
else:
    print(semi_prime(entry))

print('\nSemi-Prime numbers within your input range are:')

semi_p_range = [i for i in range(entry) if semi_prime(i)]
print(semi_p_range)
print()

