def solution(array):
    nums = [0 for _ in range(max(array)+1)]
    for i in array:
        nums[i] += 1
    
    max_count = 0
    
    if len(array) > 1:
        for j in nums:
            if j == max(nums):
                max_count += 1
    
    if max_count > 1:
        return -1
    else:
        return nums.index(max(nums))
