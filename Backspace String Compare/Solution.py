class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        finalT = ""
        indexT = len(T) - 1
        deleteT = 0
        finalS = ""
        indexS = len(S) - 1
        deleteS = 0
        
        while indexT >= 0:
            if T[indexT] == '#':
                deleteT += 1
                indexT -= 1
            elif T[indexT] != '#' and deleteT > 0:
                indexT -= 1
                deleteT -= 1
            else:
                finalT += T[indexT]
                indexT -= 1
        print(finalT) 
        
        while indexS >= 0:
            if S[indexS] == '#':
                deleteS += 1
                indexS -= 1
            elif S[indexS] != '#' and deleteS > 0:
                indexS -= 1
                deleteS -= 1
            else:
                finalS += S[indexS]
                indexS -= 1
        return finalS == finalT