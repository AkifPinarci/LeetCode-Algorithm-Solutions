class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

#         Bruto Force Solution

#         resultStr = ""
#         check = 0
#         for i in digits:
#             if i == 0:
#                 check += 1
#         if check == len(digits):
            
#             digits.append(digits.pop() + 1)
#             return digits 
#         for i in range(len(digits)):
#             resultStr += str(digits[i])
#         resultStr =  str(int(resultStr) + 1)
#         result = []
#         for i in resultStr:
#             result.append(i)
#         return result
        
    
    
#       More efficient way, I am just checking last digit.
        if digits[len(digits) - 1] < 9:
            digits[len(digits) - 1] += 1
        
        else:
            popped = 0
            while digits[len(digits) - 1] == 9:
                digits.pop()
                popped += 1
                if len(digits) == 0:
                    break
            if len(digits) > 0:
                digits[len(digits) -1] += 1
                for i in range(popped):
                    digits.append(0)
            else:
                digits.append(1)
                for i in range(popped):
                    digits.append(0)

        return digits