class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = dict()
        for i in range(len(s)):
            if s[i] not in table:
                table[(s[i])] = [i, 1]
            else:
                table[(s[i])][1] += 1
        for i in table:
            if table[i][1] == 1:
                return table[i][0]
        return -1