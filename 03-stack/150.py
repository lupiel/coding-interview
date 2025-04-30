

def eval_rpn(tokens):
    stack = []

    for t in tokens:
        if t == "+":
            b, a = stack.pop(), stack.pop()
            print(f"{a}+{b}={int(a) + int(b)}")
            stack.append(int(a) + int(b))
        elif t == "-":
            b, a = stack.pop(), stack.pop()
            print(f"{a}-{b}={int(a) - int(b)}")
            stack.append(int(a) - int(b))
        elif t == "*":
            b, a = stack.pop(), stack.pop()
            print(f"{a}*{b}={int(a) * int(b)}")
            stack.append(int(a) * int(b))
        elif t == "/":
            b, a = stack.pop(), stack.pop()
            print(f"{a}/{b}={int(int(a) / int(b))}")
            stack.append(int(int(a)/int(b)))
        else:
            stack.append(t)

    return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(eval_rpn(tokens))



# for each token
# put numbers on stack until operator met
# for a met operator replace last 2 numbers from the stack with (stack[-2]) (operator) (stack[-1])
