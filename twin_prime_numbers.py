'''
A Twin prime is a prime number that is either 2 less or 2 more than another prime number.
For example: (41,43) or (149,151)

Example:

Input: 0,15
Output: (3,5),(5,7),(11,13)

'''
print()

def check_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))

def twin_prime(number):
    splitted = number.split(',')
    from_, to_ = int(splitted[0]), int(splitted[1])
    # find the primes in that range
    find_primes = [i for i in range(from_, to_) if check_prime(i)]
    # loop through the primes and find the ones with a difference of 2
    twins = [(x,y) for x in find_primes for y in find_primes if y-x == 2]
    return twins

# entry = int(input('Enter your range seperated with a comma: '))
entry = input() or '0,15'
print(twin_prime(entry))
print()
