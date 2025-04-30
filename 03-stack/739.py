

# naive solution
# for each day iterate to the end of array to find a warmer day

def days_until_warmer(temperatures):

    answer = [0] * len(temperatures)

    for i in range(len(temperatures)):
        for j in range(i+1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                answer[i] = j-i
                break
    return answer

t = [8,7,6,5,6,7,8]
print(days_until_warmer(t))




    # EITHER - push
    # OR - pop in a loop

# for each t in temperatures

    # if stack is empty push to the stack (temp, index)
    # elif stack.top() >= t push to the stack (temp, index)
    # else in a loop pop+update until stack.top() >= t , then push

def days_until_warmer_stack(temperatures):
    answer = [0] * len(temperatures)
    stack = [] # tuples (temp[i], i)

    for i, t in enumerate(temperatures):
        if len(stack) == 0:
            stack.append((t, i))
        elif stack[-1][0] >= t:
            stack.append((t, i))
        else:
            while True:
                stack_t, stack_i = stack.pop()
                answer[stack_i] = i-stack_i
                if len(stack) == 0 or stack[-1][0] >= t:
                    break
            stack.append((t, i))

    return answer

        
t = [8,7,6,5,6,7,8]
print(days_until_warmer_stack(t))


