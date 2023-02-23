#https://leetcode.com/problems/count-primes/
#https://python.plainenglish.io/count-primes-day-78-python-7c37eb7c2c07

def checkPrime(n):
    prime = True
    for i in range(2,n):
        if n%i ==0:
            prime = False
    return prime

def countPrimes(n: int) -> int:
    count = 0
    for i in range(2,n):
        if checkPrime(i):
            count = count +1
    return count

n = 10
print(countPrimes(n))