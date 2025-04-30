
def max_area(heights):
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        max_area = max(max_area, h)
            
        if len(stack) == 0:
            stack.append([i, h])
        
        else:
            if h >= stack[-1][1]:
                for stack_i, stack_h in stack:
                    max_area = max(max_area, stack_h * (i-stack_i+1))
                stack.append([i, h])
            else: # h < stack[-1][1]:
                while len(stack) > 0 and h < stack[-1][1]:
                    stack_i, stack_h = stack.pop()
                    max_area = max(max_area, h * (i-stack_i+1))
                stack.append([stack_i, h])

        # print([i, h])
        # print("stack")
        # for ii, hh in stack:
        #     print(f"  i={ii}, h={hh}")

    return max_area

heights = [2,1,4,5,3,0,2]
answer = 9
print(max_area(heights))

heights = [1,0,4,5,3,1,0,1,2,3,4,7,7,6,5,4,3,2,1,0,6,2,0,0,4]
answer = 18
print(max_area(heights))


heights = [7,1,7,2,2,4]
answer = 8
print(max_area(heights))


heights = [1,0,1,0,1,0,1,0,1]
answer = 1
print(max_area(heights))


heights = [1,2,1,2,1,2,1,2,1]
answer = 9
print(max_area(heights))

heights = []
answer = 0
print(max_area(heights))

heights = [0,0,0]
answer = 0
print(max_area(heights))
