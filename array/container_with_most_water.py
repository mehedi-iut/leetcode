height = [1,8,6,2,5,4,8,3,7]

l, r = 0, len(height)-1

max_area = 0

while l < r:
    h = min(height[l], height[r])

    w = r - l
    area = w*h
    max_area = max(area, max_area)

    if height[l] >= height[r]:
        # if left height is greater than right height
        # then move the right height
        r-=1
    else:
        l+=1

print(max_area)
