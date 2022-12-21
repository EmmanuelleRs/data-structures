def dinamyc(n, nums = {1: 1, 2: 1}):
    if n in nums:
        return nums[n]
    else:
        nums[n] = dinamyc(n - 1, nums) + dinamyc(n - 2, nums)
        return nums[n]
    
