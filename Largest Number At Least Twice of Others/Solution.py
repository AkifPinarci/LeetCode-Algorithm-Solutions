class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        top = nums[0]
        med = 0
        index = 0
        for i in range(1, len(nums)):
            if nums[i] > top:
                med = top
                top = nums[i]
                index = i
            if nums[i] > med and nums[i] < top:
                med = nums[i]
        print(top)
        print(med)
        if med * 2 <= top:
            return index
        else:
            return -1
        
            