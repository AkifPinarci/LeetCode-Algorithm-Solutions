class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=""

        for i in range(len(indices)):
            result+=(str(s[indices.index(i)]))
        return result