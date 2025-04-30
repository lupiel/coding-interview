### naive solution
# for each pair from heights calculate volume
# return max seen volume
# n^2, 1

def max_volume(heights):

    greatest_seen = float("-inf")

    for i1, h1 in enumerate(heights):
        for i2, h2 in enumerate(heights):
            distance = abs(i2-i1)
            height = min(h1, h2)
            volume = distance*height
            greatest_seen = max(volume, greatest_seen)

    return greatest_seen


### optimal solution
# T: O(n), M: O(1)
def max_vol(heights):
    greatest_seen = float("-inf")

    left, right = 0, len(heights) - 1

    while left < right:
        distance = right - left
        height = min(heights[left], heights[right])
        volume = distance * height
        greatest_seen = max(greatest_seen, volume)

        if heights[left] < heights[right]:
            left +=1
        else:
            right -= 1

    return greatest_seen


height = [1,8,6,2,5,4,8,3,7]
print(max_vol(height))
height = [1,7,2,5,4,7,3,6]
print(max_vol(height))
