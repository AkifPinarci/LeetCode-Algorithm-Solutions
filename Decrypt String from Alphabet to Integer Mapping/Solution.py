class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        code = 1
        hasht = dict()
        for i in alphabeth:
            if code < 10:
                hasht[str(code)] = i
            else:
                hasht[str(code)+"#"] = i
            code += 1

        index = 0
        result = "" 

        while index < len(s):
            try:
                if s[index +2] != '#':
                    result += hasht[s[index]]
                    index += 1
                else:
                    result += hasht[s[index:index + 3]]
                    index += 3
            except IndexError:
                    result += hasht[s[index]]
                    index += 1
        return result