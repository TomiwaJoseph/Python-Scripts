# The Latin for six is sex, hence, 
# the name "sexy primes" for prime numbers that differ from 
# each other by six (p, p + 6) -- numbers such as 5 and 11. 
# But you can also find three prime numbers that differ by six; 
# he so-called sexy prime triplets (p, p + 6, p + 12), 
# such as 7, 13, 19.


'''
Sexy primes are prime numbers that are 6 less or 6 more than another prime number.
For example: (5,11) (11,17)

Example:
Input: 0,15
Output: (5,11)

'''
print()

def check_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))


def sexy_prime(number):
    splitted = number.split(',')
    from_, to_ = int(splitted[0]), int(splitted[1])
    # find the primes in that range
    find_primes = [i for i in range(from_, to_) if check_prime(i)]
    # loop through the primes and find the ones with a difference of 4
    twins = [(x,y) for x in find_primes for y in find_primes if y-x == 6]
    return twins

entry = input('Enter a range seperated by a comma eg. 5,20:') or '5,20'
print(sexy_prime(entry))

print('\nBonus:')
print('Sexy prime triplets within your input range are: ')
know_primes = [i for i in range(int(entry.split(',')[0]), int(entry.split(',')[1]))
    if check_prime(i)]
l = [(x,y,z) for x in know_primes for y in know_primes for z in know_primes 
        if y-x == 6 and z-y == 6 and x!=y]
if l: print(l)
else: print('No sexy prime triplets in your input range.')
print()
