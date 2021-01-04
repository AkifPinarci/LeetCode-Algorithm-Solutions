class Solution:
    def lengthOfLastWord(self, s: str) -> int:
#         arr = s.split(" ")
#         while arr[-1] == '':
#             arr.pop()
#             if len(arr) == 0:
#                 return 0
#         if arr[-1] and arr[-1] != '':
#             return len(arr[-1])

#         return 0


        length = 0
        while s[-1] == ' ':
            s = s[:-1]
            if len(s) == 0:
                return 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif s[i] == ' ':
                break
        return length
        