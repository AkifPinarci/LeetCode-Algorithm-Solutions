class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        newheights = sorted(heights)
        students = 0
        for i in range(len(heights)):
            if heights[i] != newheights[i]:
                students += 1
        return students