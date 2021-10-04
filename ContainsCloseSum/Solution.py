def containsCloseNums(nums, k):
    h_list = dict()
    for i in range(len(nums)):
        if nums[i] not in h_list:
            h_list[nums[i]] = i
        else:
            if (i - h_list[nums[i]]) <= k:
                return True
            else:
                h_list[nums[i]] = i
    return False        