nums = [2,3,2]

n = len(nums)
        
# if n == 1: return nums[0]


temp1 = nums[1:]
temp2 = nums[:-1]


def house_robber(arr):
    # here we are using space optimized code
    # but we can use other technique like memoization or tabulation also
    prev = arr[0]
    prev2 = 0

    for i in range(1, len(arr)):
        pick = arr[i] + prev2
        not_pick = 0 + prev

        curr = max(pick, not_pick)

        prev2 = prev
        prev = curr

    return prev

ans1 = house_robber(temp1)
ans2 = house_robber(temp2)

print(max(ans1, ans2))