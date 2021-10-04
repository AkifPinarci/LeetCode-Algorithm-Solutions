arr = [5, 3, 2, 1, 3]
temp = arr[0:4]
temp = temp[::-1]
arr[0:4] = temp
print(arr)
