'''
A number is considered to be ugly if its only prime factors are 2,3 or 5
[2,3,4,5,6,8,9,10,12,15,...] is the sequence of ugly numbers

'''
print()

def know_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))

def check_ugly(number):
    # find all the prime factors of the number
    prime_factors = [i for i in range(1,number+1) if number%i==0 and know_prime(i)]
    # find out if all the primes are in the list of [2,3,5] by assigning 1 for true and 
    # 0 as false and the number is not a prime number
    find_out = all([1 if i in [2,3,5] else 0 for i in prime_factors]) and bool(prime_factors)
    return find_out


entry = int(input('Enter your number: '))
print(check_ugly(entry))

print('\nBonus')
print('Ugly numbers in your input range are:')
print([i for i in range(entry) if check_ugly(i)])