nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

nums.sort()
N, result = len(nums), []
for i in range(N):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    target = nums[i]*-1
    s,e = i+1, N-1
    while s<e:
        if nums[s]+nums[e] == target:
            result.append([nums[i], nums[s], nums[e]])
            s = s+1
            while s<e and nums[s] == nums[s-1]:
                s = s+1
        elif nums[s] + nums[e] < target:
            s = s+1
        else:
            e = e-1
print(result)




# num = [-1,0,1,2,-1,-4]
# cont = []
# result = []
# for i in range(len(num)):
#     for j in range(i+1, len(num)):
#         for k in range(j+1, len(num)):
#             if (num[i]+num[j]+num[k]) == 0:
#                 cont.append(num[i])
#                 cont.append(num[j])
#                 cont.append(num[k])
#             if sorted(cont) in result:
#                 pass
#             elif len(cont) ==3:
#                 result.append(sorted(cont))
#             cont=[]

# print(result)