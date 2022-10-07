
def two_sum(nums, target):
    hashmap = {}
    for ind, val in enumerate(nums):
        diff = target - val

        if diff in hashmap:
            return [hashmap[diff], ind]
        
        hashmap[val] = ind

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(two_sum(nums, target))
     