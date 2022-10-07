nums = [4,5,6,7,0,1,2]
target = 0

def search_sorted_array(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        
        # check whether we are in left portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        # otherwise, we are in right portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        
    return -1



if __name__ == '__main__':
    print(search_sorted_array(nums, target))