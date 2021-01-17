class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest=-1
        index=len(arr)-1
        for i in reversed(arr):
            arr[index]=greatest
            if i>greatest:
                arr[index] = greatest
                greatest=i
            else:
                arr[index]=greatest
            index-=1
        return arr