
# tail = 0
# cur = 0
# result = 0
# seen = set()
# for i in range(len(s)):
#     while tail <= len(s) - 1  and s[tail] not in seen:
#         seen.add(s[tail])
#         tail += 1
#         cur += 1
#         if cur > result:
#             result = cur
    
#     cur = 0
#     tail = i+1
#     seen.clear()

# print(result)

s = "abcabcbb"
result = 0
seen = set()
array = list()

for i in range(len(s)):
    print(array)
    if s[i] not in seen:
        seen.add(s[i])
        array.append(s[i])
        if len(array) > result:
            result = len(array)
    else:
        track = 0
        while len(array) != 0 and s[i] != array[0]:
            seen.remove(array.pop(0))
        seen.remove(array.pop(0))
        seen.add(s[i])
        array.append(s[i])

print(result)       