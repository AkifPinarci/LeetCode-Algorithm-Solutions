class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(string):
            if string == string[::-1]:
                return True
            return False
        left = 0
        right = len(s) - 1
        
        while left < right:
            
            if s[left] != s[right]:
                right_string = s[left:right]
                left_string = s[left + 1:right + 1]
                
                return checkPalindrome(left_string) or checkPalindrome(right_string)
            
            left += 1
            right -= 1
        
        return True

# Bruto force solution.
# def checkPalindrome(string):
#     if string == string[::-1]:
#         return True
#     return False
# def validPalindrome(s):
#     if s == s[::-1]:
#         return True
#     for i in range(len(s)):
#         if checkPalindrome(s[0:i] + s[i+1:len(s)]):
#             return True
#     return False

