class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if len(J) == 0 or len(S) ==0 :
            return 0
        s = 0
        for i in J:
            s += S.count(i)
        return s