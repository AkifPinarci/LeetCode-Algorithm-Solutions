class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      maxOfCandies=max(candies)
      booloutput=[]
      for i in candies:
        if(i+extraCandies) >= maxOfCandies:
            booloutput.append(True)
        else:
            booloutput.append(False)
      return booloutput
        