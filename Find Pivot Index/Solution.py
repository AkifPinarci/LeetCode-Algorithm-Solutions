class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Bruto force solution
        
        # if len(nums) == 1:
        #     return 0
        # if len(nums) == 0:
        #     return -1
        # for i in range(len(nums)):
        #     if sum(nums[0:i]) == sum(nums[i+1:len(nums)]):
        #         return i
        # return -1
        
        # Smarter and faster solution
        
        
        frontTotal = 0
        backTotal = sum(nums)
        
        for i in range(len(nums)):
            if backTotal - frontTotal - nums[i] == frontTotal:
                return i
            else:
                frontTotal += nums[i]
        return -1
            
        