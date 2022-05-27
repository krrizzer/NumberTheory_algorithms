'''#Q2

my_primes =[2, 3, 5, 7, 11, 13, 17, 19]
for i in my_primes:
    print(i)'''

import random

#Q3, the GCD function

def gcd(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a

    # base case
    if (a == b):
        return a

    # a is greater
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)

#Q4 is_prime



#Q5

#----------------








    bases2 = int(input("Enter the number of bases: "))




def is_prime(n, k):
        bases = []
        for i in range(2, k + 1):
            bases.append(i)
        for base in bases:
            a = pow(base, n - 1) % n
            if (a == 1):
                return True
            else:
                return False



'''k=3
for i in range(1,201):
    if is_prime(i,k):
        print(i,"true")
    else:
        print(i, "false")'''
#PA2
#Q1

def mersennePrimes(p, k):
        n = 2**p -1
        if is_prime(n,k):
            return True
        else:
            return False

for i in range(2, 29):
    print(i ,mersennePrimes(i, 3), "for mersenne")



print(mersennePrimes(31,3))

# it takes around 1 minute to compute

#Q2





def mod_exp(b, n, m):
    # Initialize result
    res = 1

    # Update 'a' if 'a' >= p
    b = b % m

    while n > 0:

        # If n is odd, multiply
        # 'b' with result
        if n % 2:
            res = (res * b) % m
            n = n - 1
        else:
            b = (b ** 2) % m

            # n must be even now
            n = n // 2

    return res % m

b = int(input("Enter b:"))
n = int(input("Enter n:"))
n= 2**n -2
m = int(input("Enter m:"))
m = 2**m -1
r = mod_exp(b, n, m)
print("{} ^ {} ≡ {} (mod {})".format(b, n, r, m))
# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def isPrime2(n, k):
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True

    # Try k times
    else:
        for i in range(k):

            # Pick a random number
            # in [2..n-2]
            # Above corner cases make
            # sure that n > 4
            a = random.randint(2, n - 2)

            # Fermat's little theorem
            if mod_exp(a, n - 1, n) != 1:
                return False

    return True



def mersennePrimes2(p, k):
        n = 2 ** p - 1
        if isPrime2(n, k):
            return True
        else:
            return False


for i in range(2, 16001):
    print(i, mersennePrimes2(i, 3), "for mersenne2")



print(mersennePrimes2(31, 3))

# it is much faster than mersenne prime 1 , it took less than 1 second
# i tried the first 16000 numbers and it took about 4 minutes