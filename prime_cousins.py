'''
Cousin primes are prime numbers that are 4 less or 4 more than another prime number.
For example: (3,7) (43,47)

Example:

Input: 0,15
Output: (3,7),(7,11)

'''
print()

def check_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))


def cousin_prime(number):
    splitted = number.split(',')
    from_, to_ = int(splitted[0]), int(splitted[1])
    # find the primes in that range
    find_primes = [i for i in range(from_, to_) if check_prime(i)]
    # loop through the primes and find the ones with a difference of 4
    twins = [(x,y) for x in find_primes for y in find_primes if y-x == 4]
    return twins

entry = input("Enter two numbers seperated with a comma: ") or '5,20'
print(cousin_prime(entry))
print()
