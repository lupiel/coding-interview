
# compare each i to every other i
# def valid_calendar_naive(intervals):

# sort by start
# for each n
# i[n].start >= i[n-1].end


def valid_calendar_sort(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i-1][1] > intervals[i][0]:
            return False

    return True

intervals = [(0,30),(5,10),(15,20)]
print(valid_calendar_sort(intervals))

intervals = [(5,8),(8,8),(8,20)]
print(valid_calendar_sort(intervals))
