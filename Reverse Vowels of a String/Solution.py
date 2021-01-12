class Solution:
    def reverseVowels(self, s: str) -> str:
        # Bruto force solution

        vowels = {'a', 'e', 'u', 'i', 'o'}
        arr = list()
        for i in s:
            if i.lower() in vowels:
                arr.append(i)
        result = ""
        for i in s:
            if i.lower() in vowels:
                result += arr[-1]
                arr.pop(-1)
            else:
                result += i
        return result