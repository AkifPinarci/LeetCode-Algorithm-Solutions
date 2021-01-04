class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        def helper(number):
            string = str(number)
            for i in string:
                if int(i) == 0:
                    return -1
                if number % int(i) != 0:
                    return -1
            return number


        for i in range(left, right + 1):
            if helper(i) == -1:
                pass
            else:
                result.append(helper(i))


        return result