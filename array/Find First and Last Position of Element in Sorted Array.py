
nums = [5,7,7,8,8,10]
target = 8

def find_position(nums, target):
    left = bin_search(nums, target, True)
    right = bin_search(nums, target, False)

    return [left, right]

def bin_search(nums, target, leftbias):
    l, r = 0, len(nums)-1
    i = -1
    while l<=r:
        mid = (l+r)//2

        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            i = mid

            if leftbias:
                r = mid - 1
            else:
                l = mid + 1
    return i

if __name__ == "__main__":
    print(find_position(nums, target))
    