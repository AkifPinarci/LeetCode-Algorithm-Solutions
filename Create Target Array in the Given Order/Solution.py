class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []

        if len(nums) == 0:
            return arr
        if len(nums) == 1:
            arr.append(nums[0])
            return arr
        hasht = dict()

        for i in index:
            hasht[i] = []
        for i in range(len(nums)):
            hasht[index[i]].append(nums[i])
        print(hasht)
        for i in range(len(index)):  # i goes (0, 5)
            if i in hasht:
                for k in range(len(hasht[i])):
                    arr.append(hasht[i].pop())

        return arr
