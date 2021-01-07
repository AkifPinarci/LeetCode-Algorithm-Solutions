class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hasht = dict()
        for i in deck:
            if i in hasht:
                hasht[i] += 1
            else:
                hasht[i] = 1
        arr = hasht.values()
        
        def hcfnaive(a,b): 
            if(b==0): 
                return a 
            else: 
                return hcfnaive(b,a%b)
        gcd = hcfnaive(min(arr), max(arr))
        for i in range(2, min(arr)+1):
            check = 0
            for k in arr:
                if k % i == 0:
                    check += 1
            if check == len(arr):
                return (True)
        return (False)