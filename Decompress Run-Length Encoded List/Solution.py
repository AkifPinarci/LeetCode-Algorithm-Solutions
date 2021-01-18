class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output=[]
        iter=0
        for i in range(1,len(nums),2):
            for k in range(nums[i-1]):
                output.append(nums[iter+1])
            iter+=2
        return output