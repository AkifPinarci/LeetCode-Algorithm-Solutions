class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        arr = S.split("-")
        string = "".join(arr)
        result = ""
        if len(arr) == len(S) + 1:
            return ""
        if len(string) % K != 0:
            result += string[0:len(string)%K]
            string = string[len(string)%K::]

        # for i in range(1,len(string)//K + 1):
        #     result += "-" +string[i * (len(string)%K):i * (len(string)%K + K)]

        # print((result).upper())

        index = 1
        for i in range(len(string)):
            if i % K == 0:
                result += "-"
            result += string[i]
        if result[0] == "-":
            result = result[1::]
        return result.upper()