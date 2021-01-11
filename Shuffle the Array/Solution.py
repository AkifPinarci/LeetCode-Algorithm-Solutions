class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1=nums[0:len(nums)//2]
        arr2=nums[len(nums)//2:len(nums)]
        print(arr1)
        print(arr2)
        result=[]
        for i in range(len(arr1)):
            result.append(arr1[i])
            result.append(arr2[i])
        return result