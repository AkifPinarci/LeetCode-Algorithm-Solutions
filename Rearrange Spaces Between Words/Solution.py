class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = 0
        for i in text:
            if i == " ":
                count += 1
        result = ""
        arr = text.split(" ")
        word = 0
        for i in arr:
            if i != "":
                word += 1
        check = 0
        for i in arr:
            if i != "":
                result += i
                check += 1
                if check == word:
                    break
                for i in range(count // (word - 1)):
                    result += " "
        if word - 1 == 0:
            for i in range(count):
                result += " "
        else:
            for i in range(count % (word - 1)):
                result += " "
        return result