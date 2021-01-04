def solution(nums):
    if len(set(nums)) < 3:
        return max(nums)
    track = [-1, -1, -1]
    for i in range(len(nums)):
        if nums[i] > track[0] and nums[i] > track[1] and nums[i] > track[2] and nums[i] not in track:
            track[0] = track[1]
            track[1] = track[2]
            track[2] = nums[i]
            print("Check 1")
        elif nums[i] > track[0] and nums[i] > track[1]and nums[i] < track[2] and nums[i] not in track:
            track[0] = track[1]
            track[1] = nums[i]
            print("Check 2")
        elif nums[i] > track[0] and nums[i] not in track:
            track[0] = nums[i]
            print("Check 3")
        else:
            pass
        print(track)
    if track[0] == -1 or track[1] == -1:
        return track[2]
    else:
        return track[0]

    # Solution implemented by using array structure and sort method. 
    # track = []
    # for i in range(len(nums)):
    #     if nums[i] not in track:
    #         track.append(nums[i])

    #         if len(track) > 3:
    #             track = sorted(track)
    #             track = track[1:]
    # print(track)

    # if len(track) < 3:
    #     return max(track)
    # else:
    #     return min(track)

nums = [1, 2, 3, 4, 5, 6, 7,45, 456, 234,12, 8, 9, 10]
print(solution(nums))