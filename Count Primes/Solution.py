class Solution:
    def countPrimes(self, n: int) -> int:
#         Bruto force solution.
#         counter = 0
#         def checkPrime(num):
#             if num == 1 or num == 0:
#                 return False
#             if num == 2:
#                 return True
#             for i in range(2, int(num **1/2) + 1):
#                 if num % i == 0:
#                     return False
#             return True

#         for i in range(n):
#             if checkPrime(i):
#                 counter += 1
#         return counter


#       Sieve of Eratosthenes method
        if n <= 1:
            return 0
        arr = [True] * n
        counter = 0
        
        for i in range(2, int(n **1/2) + 1):
            for j in range(i*i, n, i):
                arr[j] = False
        return sum(arr) - 2