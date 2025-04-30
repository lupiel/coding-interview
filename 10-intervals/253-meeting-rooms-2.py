
# |----------------------|
#                |----|
#     |----------|
# |--------------|
# 1   2          3    4   5

# (1,5)
# (3,4)
# (2,3)
# (1,3)

# starts = [1,1,2,3]
#                 s
# ends   = [3,3,4,5]
#           e


def min_meeting_rooms(intervals):

    max_meetings = float("-inf")
    cur_meetings = 0

    starts = sorted([i[0] for i in intervals])
    ends   = sorted([i[1] for i in intervals])

    s, e, n = 0, 0, len(intervals)

    # loop until start all meetings
    while s < n:
        curr_end = ends[e]
        curr_start = starts[s]
        print("pointers", s, e)
        while s < n and starts[s] < curr_end:
            curr_start = starts[s]
            s += 1
            cur_meetings += 1
            max_meetings = max(max_meetings, cur_meetings)

        while ends[e] <= curr_start:
            curr_end = ends[e]
            e += 1
            cur_meetings -= 1

    return max_meetings

intervals = [[1,5],[3,4],[2,3],[1,3]]
print(min_meeting_rooms(intervals))

intervals = [[1,5],[2,4],[2,3],[1,3]]
print(min_meeting_rooms(intervals))

intervals = [[1,5],[4,6],[2,3],[1,3]]
print(min_meeting_rooms(intervals))





# |----------------------|
#                     |------|
#     |----------|
# |--------------|
# 1   2          3    4   5  6


# (1,5)
# (3,4)
# (2,3)
# (1,3)

# starts = [1,1,2,4]
#               s
# ends   = [3,3,5,6]
#           e