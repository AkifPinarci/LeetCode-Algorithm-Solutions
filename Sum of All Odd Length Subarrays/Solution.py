class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr)):
            for k in range(i, len(arr), 2):
                total += sum(arr[i:k+1])
        return total