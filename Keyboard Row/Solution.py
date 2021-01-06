class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        result = []
        line1 = {'q','w', 'e', 'r', 't', 'y', 'u' , 'i', 'o', 'p'}
        line2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        line3 = {'z','x','c','v','b','n','m'}

        for i in words:
            check1 = True 
            check2 = True
            check3 = True
            for k in i:
                if k.lower() not in line1:
                    check1 = False
                if k.lower() not in line2:
                    check2 = False
                if k.lower() not in line3:
                    check3 = False
            if check1 or check2 or check3:
                result.append(i)
        return result