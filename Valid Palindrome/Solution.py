import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = re.findall("[a-zA-Z|0-9]", s)

        # Optimized solution at the bottom by iterating throug only the half of the string
        for i in range(len(x) // 2):
            if x[i] == x[-1 - i]:
                pass
            else:
                return False
        return True
    
    
        # if x == x[::-1]:
        #     return True
        # return False
