class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanceNum=0
        numString=0
        for i in s:
            if(i=="R"):
                balanceNum+=1
            elif(i=="L"):
                balanceNum-=1
            if(balanceNum==0):
                numString+=1
        return numString
            