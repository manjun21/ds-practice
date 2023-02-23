def countPrimes(n: int) -> int:
        if n < 2:
            return 0
        primes = [True]*n 
        primes[0] = False
        primes[1] = False

        for i in range(2,n):
            if primes[i]:
                for j in range(i+i,n,i):
                    primes[j] = False
        return primes.count(True)

print(countPrimes(10))