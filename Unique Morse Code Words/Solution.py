class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        o=set()
        a=  ["01","1000","1010","100","0","0010","110","0000","00","0111","101","0100","11","10","111","0110","1101","010","000","1","001","0001","011","1001","1011","1100"]
        for word in words:
            temp = ""
            for char in word:
                temp += a[ord(char) - 97]
            o.add(temp)
        return len(o)