# Inser function used
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums))[::-1]:
            result.insert(0,sum(nums))
            nums.pop(i)
        return result