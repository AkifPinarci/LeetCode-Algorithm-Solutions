class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for k in range(len(nums)):
                if nums[i]==nums[k] and i<k:
                    count +=1
        return count