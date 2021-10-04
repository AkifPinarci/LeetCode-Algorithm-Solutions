
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

crypt = ["SEND", "MORE", "MONEY"]
input1 = ""
input2 = ""
input3 = ""

h_list = dict()
for i in range(len(solution)):
    h_list[solution[i][0]] = solution[i][1]
    
input1 = ""
input2 = ""
input3 = ""

# for i in crypt[0]:
#     if h_list[crypt[0][0]] == '0':
#         return False
#     input1 += h_list[i]
    
# for i in crypt[1]:
#     if h_list[crypt[0][0]] == '0':
#         return False
#     input2 += h_list[i]
        
# for i in crypt[2]:
#     if h_list[crypt[0][0]] == '0':
#         return False
#     input3 += h_list[i]
#     print(input3)

# print(input3)    
# print(input1, input2, input3)
# print(int(input1) + int(input2) == int(input3))
    
        