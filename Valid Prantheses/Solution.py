s = "()"

array = []
openn = {')':'(', '}':'{',']':'['}

for i in s:
    if i not in openn:
        array.append(i)
    else:
        if array.pop() != i:
            print(False)
    if len(array) == 0 and i in openn:
        print(False)
    
    
if len(array) == 0:
    print(True)
else:
    print(False)



