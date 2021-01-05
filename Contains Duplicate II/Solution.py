class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         Bruto force solution (There is on extra space usage, Time complexity O(n^2))
#         if len(nums) == len(set(nums)):
#             return False
        
#         for i in range(len(nums)):
#             for j in range(1, k + 1):
#                 if i + j > len(nums) - 1:
#                     break
#                 if nums[i] == nums[i + j]:
#                     return True
#         return False


#       Faster solution with dictionary. (Space complexity = O(n), Time Complexity = O(n))
        hasht = dict()
        if len(nums) == set(nums):
            return False
        for i in range(len(nums)):
            if nums[i] in hasht and abs(i - hasht[nums[i]]) <= k:
                return True
            else:
                hasht[nums[i]] = i
        return False

