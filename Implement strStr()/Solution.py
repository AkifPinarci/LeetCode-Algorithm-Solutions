class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0 or (len(haystack) == 1 and len(needle) == 1 and haystack == needle):
            return 0
        if len(haystack) == 1 and len(needle) == 1 and haystack != needle:
            return -1
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        check = needle[0]
        for i in range(len(haystack)):
            if haystack[i] == check and haystack[i:i+len(needle)] == needle:
                return i
        return -1