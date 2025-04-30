#   +---+           
# +--+ +--+ ++ 
# [1,4],[3,7],[6,9],[11,12]
# answer
# +-------+ ++


def merge_intervals(intervals):
    intervals.sort()
    ret = [intervals[0]]

    for start, end in intervals[1:]:
        prev_end = ret[-1][1]

        if prev_end >= start:
            # merge prev with curr
            ret[-1][1] = max(end, prev_end)
        else:
            # add a disjoint intervals
            ret.append([start, end])

    return ret


intervals = [[1,4],[3,10],[6,9],[11,12]]
print(merge_intervals(intervals))

intervals = [[1,2],[2,3],[3,5],[3,6],[7,9]]
print(merge_intervals(intervals))


