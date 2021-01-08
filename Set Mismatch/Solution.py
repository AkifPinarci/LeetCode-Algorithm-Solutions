class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hasht = dict()
        for i in range(len(nums)):
            if nums[i] in hasht:
                hasht[nums[i]] += 1
            else:
                hasht[nums[i]] = 1
        for i in range(1, len(nums)+1):
            if i not in hasht:
                missing = i
            if i in hasht and hasht[i] == 2:
                doubled = i
                
        return [doubled, missing]
            
            