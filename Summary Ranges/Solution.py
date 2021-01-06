class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        arr = []
        sp = nums[0]
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if sp == nums[i]:
                    arr.append("{}".format(sp))
                else:
                    arr.append("{}->{}".format(sp,nums[i]))
            elif nums[i+1] - nums[i] != 1:
                if sp == nums[i]:
                    arr.append("{}".format(sp))
                else:
                    arr.append("{}->{}".format(sp,nums[i]))
                sp = nums[i+1]
                            
        return arr
            
                