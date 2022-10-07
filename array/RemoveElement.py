nums = [0,1,2,2,3,0,4,2]
val = 2

left = 0

for r in range(len(nums)):
    if nums[r] != val:
        nums[left] = nums[r]
        left += 1

print(left)