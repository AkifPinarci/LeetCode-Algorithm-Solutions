class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return  int((n/2)) + self.numberOfMatches(n/2)
        elif n % 2 == 1:
            return int(((n-1)/2+1)) + self.numberOfMatches((n - 1)/2)
        
#         Fastest and smarter way        
#         return n - 1