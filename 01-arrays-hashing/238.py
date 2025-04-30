from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    pre = [0] * n
    pos = [0] * n
    ret = [0] * n

    pre[0] = 1
    pos[n-1] = 1

    # pre pass
    for i in range(1, n):
        pre[i] = pre[i-1] * nums[i-1]

    # post pass
    for i in range(n-2, -1, -1):
        pos[i] = pos[i+1] * nums[i+1]

    # ret pass
    for i in range(n):
        ret[i] = pre[i] * pos[i]
    
    print("nums", nums)
    print("pre", pre)
    print("pos", pos)
    print("ret", ret)
    return ret


# pref = [x ,  1, 2, 6]  
# nums = [1 ,  2, 3, 4]
# post = [24, 12, 4, x]


def test():
    nums = [1,2,3,4]
    answer = [24, 12, 8, 6]
    assert product_except_self(nums) == answer

    nums = [-1,0,1,2,3]
    answer = [0,-6,0,0,0]
    assert product_except_self(nums) == answer

test()

# naive solution
# generate product by running each cell with every other cell

# division solution

# saving prefix product 
# saving postfix product
# reading prefix and postfix and calculating prodct except self








