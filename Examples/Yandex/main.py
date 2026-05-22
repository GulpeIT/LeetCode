# Найти все простые числа меньше или равные заданному числу N.

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        is_prime = [True] * (n + 1)
        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p > n:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        return primes.count

# Найти наибольший общий делитель всех чисел в заданном диапазоне [L, R].