class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        num = 1
        index = 0
        result = []
        while num <= target[len(target) - 1]:
            if target[index] == num:
                result.append("Push")
                num += 1
                index += 1
            else:
                result.append("Push")
                result.append("Pop")
                num += 1
        return result