class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        
        for i in range(n):
            nums.append(start+2*i)
        value=nums[0]
        for i in range(1,len(nums)):
            value^=nums[i]
        return value