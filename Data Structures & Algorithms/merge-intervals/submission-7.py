class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        
        result = [intervals[0]]
        interval = 1
        while interval < len(intervals):
            if result[-1][1] >= intervals[interval][0]:
                result[-1][1] = max(result[-1][1], intervals[interval][1])
                interval += 1

            else:
                result.append(intervals[interval])

        return result