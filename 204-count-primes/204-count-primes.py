class Solution:
    def countPrimes(self, n: int) -> int:
        isprime = [True]*(n)
        isprime[:2] = [False, False]
        for i in range(2, int(n**0.5)+1):
            if isprime[i]:
                isprime[i*i:n:i] = [False]*len(isprime[i*i:n:i])
        return sum(isprime)
                



        