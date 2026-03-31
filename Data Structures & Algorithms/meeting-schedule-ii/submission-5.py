"""
Definition of Interval:
class Interval(object):
    def __init__(self, start_arr, end_arr):
        self.start_arr = start_arr
        self.end_arr = end_arr
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        start_arr = []
        end_arr = []

        for i in range(len(intervals)):
            start_arr.append(intervals[i].start)
            end_arr.append(intervals[i].end)

        start_arr = sorted(i.start for i in intervals)
        end_arr = sorted(i.end for i in intervals)

        start_arr.sort()
        end_arr.sort()

        max_meetings = 0
        current_meetings = 0
        s, e = 0, 0
        while e<len(end_arr) and s < len(start_arr):
            if end_arr[e] == min(start_arr[s], end_arr[e]):
                e += 1
                current_meetings -= 1
            else: 
                s += 1
                current_meetings += 1
                max_meetings = max(max_meetings, current_meetings)
                

        return max_meetings
        # intervals.sort(key = lambda x:x.start_arr)
        
        # prevend_arr = intervals[0].end_arr

        # result = 1

        # for i in range(1, len(intervals)):
        #     if prevend_arr > intervals.start_arr:
        #         prevend_arr = intervals.end_arr
        #         result += 1
        #     else:
        #         prevend_arr = intervals.end_arr

        # return result