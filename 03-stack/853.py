# sort input cars by position
# iterating from the highest value check if the car would "collide" by the target with the previous one
    # if collide add to a stack
    # if wouldnt collide then groups++

def time_to_target(position, speed, target):
    return (target - position) / speed

def car_fleets(target, positions, speeds):

    cars = [[p, s] for p, s in zip(positions, speeds)]
    cars.sort(key=lambda x: x[0], reverse=True)
    stack = []
    fleets = 0


    for p, s in cars:
        if len(stack) == 0:
            stack.append([p, s])
        else:
            t = time_to_target(p, s, target)
            stack_t = time_to_target(stack[0][0], stack[0][1], target)
            collide_by_target = t < stack_t
            if collide_by_target:
                stack.append([p, s])
            else:
                stack = []
                stack.append([p, s])
                fleets += 1
    
    if len(stack) > 0:
        fleets += 1

    return fleets

# Time O(n logn)
# Memory O(n)

#test case
target = 16
position = [0,5,10,15,3]
speed = [10,9,12,11,5]
print(car_fleets(
    target,
    position,
    speed
))