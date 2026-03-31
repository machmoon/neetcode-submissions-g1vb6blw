"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)):
            r = i + 1
            # [(5,8),(9,15)]
            # [(9,15), (5,8)]
            while r < len(intervals):
                if intervals[i].end > intervals[r].start:
                    return False

                r+=1
            

        return True