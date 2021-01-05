class Solution:
    def isUgly(self, num: int) -> bool:
        
        
        def isPrime2(n):
            if n==2 or n==3: return True
            if n%2==0 or n<2: return False
            for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
                if n%i==0:
                    return False    

            return True
        
#         Bruto Force Solution
#         arr=[]
#         for i in range(7,abs(num)//2 + 1):
#             if isPrime2(i):
#                 arr.append(i)
#         for i in arr:
#             if num % i == 0:
#                 return False
#         return True





        if num == 0:
            return False
        while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            else:
                num /= 5
        return num == 1