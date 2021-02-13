'''
A lab number is a number such that the square of any of its prime
divisors is still one of its divisors.

Example:
Input: 8
Output: True(2 is a prime divisor of 8 and its square 4 is also a divisor of 8)

Input: 50
Output: True(5 is a prime divisor of 50 and its square 25 is also a divisor of 50)

Input: 34
Output: False (2 and 17 is a prime divisor of 34 but none of their squares can divide
    34 without a remainder)

'''
print()


def know_prime(number):
    return number > 1 and not any(number % n ==0 for n in range(2, number))

def check_lab(number):
    factors = [i for i in range(1,number) if not number % i]
    prime_divisors = [i for i in factors if know_prime(i)]
    divisible = [1 if number%i**2==0 else 0 for i in prime_divisors]
    return any(divisible)


entry = int(input('Enter a number: '))
print(check_lab(entry))
print()

print('Lab numbers within your input range are:')

lab_range = [i for i in range(1,entry) if check_lab(i)]
print(lab_range)
print()
