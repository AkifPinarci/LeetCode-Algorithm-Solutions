class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output=[]
        smallerCount=0
        for i in nums:
            for k in nums:
                if i>k:
                    smallerCount+=1
            output.append(smallerCount)
            smallerCount=0
        return output
                    
            
            
            