class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = {'q':5,'w':5, 'e':5, 'r':5, 't':5, 'y':5, 'u':5 , 'i':5, 'o':5, 'p':5}
        line2 = {'a':2, 's':2, 'd':2, 'f':2, 'g':2, 'h':2, 'j':2, 'k':2, 'l':2}
        line3 = {'z':11,'x':11,'c':11,'v':11,'b':11,'n':11,'m':11}
        result = []
        for i in words:
            total = 0
            for k in i:
                if k.lower() in line1:
                    total += 5
                if k.lower() in line2:
                    total += 2
                if k.lower() in line3:
                    total += 11
            if total == len(i)*5 or total == len(i)*2 or total == len(i)*11:
                result.append(i)
        return result
        
#         result = []
#         line1 = {'q','w', 'e', 'r', 't', 'y', 'u' , 'i', 'o', 'p'}
#         line2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
#         line3 = {'z','x','c','v','b','n','m'}

#         for i in words:
#             check1 = True 
#             check2 = True
#             check3 = True
#             for k in i:
#                 if k.lower() not in line1:
#                     check1 = False
#                 if k.lower() not in line2:
#                     check2 = False
#                 if k.lower() not in line3:
#                     check3 = False
#             if check1 or check2 or check3:
#                 result.append(i)
#         return result