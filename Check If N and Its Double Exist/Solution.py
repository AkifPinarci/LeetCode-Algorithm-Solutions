class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) == 2:
            return True
        for i in arr:
            if i==0:
                pass
            elif i*2 in arr:
                return(True)
        return False