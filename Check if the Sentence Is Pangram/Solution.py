class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        setCheck = set()
        if len(sentence) < 26:
            return False
        for i in sentence:
            setCheck.add(i)
        if len(setCheck)== 26:
            return True
        else:
            return False
