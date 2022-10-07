nums = [-1,0,1,2,-1,-4]

res = set()
nums.sort()

for i in range(len(nums)):
    if nums[i] == nums[i-1]:
        continue

    l = i+1
    r = len(nums)-1

    while l < r:
        total = nums[i] + nums[l] + nums[r]
        if total == 0:
            res.add((nums[i], nums[l], nums[r]))

            l += 1
            r -= 1
        
        elif total > 0:
            r -= 1
        else:
            l += 1

print(res)