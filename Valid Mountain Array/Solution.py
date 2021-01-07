class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        top = False
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] >= 1 and not top:
                pass
            elif arr[i+1] - arr[i] == 0:
                return False
            else:
                top = True
                if i == 0:
                    return False
            if top:
                if arr[i] - arr[i+1] >= 1:
                    pass
                else:
                    return False
                
        return top