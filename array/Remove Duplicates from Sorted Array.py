nums = [0,0,1,1,1,2,2,3,3,4]

left = 0

for right in range(1, len(nums)):
    # check the left element is equal to right, if so, we increment the left
    # and place the right element
    if nums[left] != nums[right]:
        left += 1
        nums[left]= nums[right]

print(left+1)