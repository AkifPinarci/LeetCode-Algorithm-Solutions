left = 1
right = 22
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


print(result)