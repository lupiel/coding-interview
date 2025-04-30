tasks = ["A","A","A","B","B","C","D"]
tasks = ["Z","A","A","A","B","B","C","D"]

n = 2
# A -> B -> C -> A -> B -> D -> A.

# A: 3
# B: 2
# C: 1
# D: 1
# Count of labels=4



# max_heap [
#     [-3, "A"]
#     [-2, "B"]
#     [-1, "C"]
#     [-1, "D"]
# ]
#[- occurence remaining, process label]

# t = 0 1 2 3 4

# iddle_until_t = [
# t=0    [3, A]  t + n + 1
# t=1    [4, B]
# t=2    [5, C]
# ]
#[allowed to process at time t, process label]



from collections import deque, defaultdict
import heapq

def min_time_schedule(tasks, n):
    task_freq = {}
    for task in tasks:
        task_freq[task] = task_freq.get(task, 0) + 1

    idle_q = deque()
    task_min_heap = [[-v, k] for k, v in task_freq.items()]
    heapq.heapify(task_min_heap)
    # task_freq = [[-v, k] for k, v in sorted(task_freq.items(), key=lambda x: x[1], reverse=True)]
    # task_freq = [[k, v] for k, v in sorted(
    #     task_freq.items(), key=lambda x: x[1], reverse=True
    #     )
    # ]
    processed = []

    t = 0
    while task_min_heap or idle_q:
        if idle_q:
            come_back_time, task_chunks_left, task_label = idle_q.popleft()
            if come_back_time <= t:
                  heapq.heappush(task_min_heap, [task_chunks_left, task_label])
            else:
                  idle_q.appendleft([come_back_time, task_chunks_left, task_label])
                  
        if task_min_heap:
            # consume
            task_chunks_left, task_label = heapq.heappop(task_min_heap)
            processed.append(task_label)
            task_chunks_left += 1
            if task_chunks_left < 0:
                idle_q.append([
                    t+n+1,
                    task_chunks_left,
                    task_label
                ])
        else:
            # iddle
            processed.append("")

        t += 1
    print(t, processed)
    return t

min_time_schedule(tasks, n)



tasks = ["A","A","A","B","B","C","D"]
n=5
min_time_schedule(tasks, n)