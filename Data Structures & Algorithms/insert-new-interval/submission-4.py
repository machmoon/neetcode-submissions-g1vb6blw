class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else: 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)
        return result

        # if len(intervals) == 0:
        #     return newInterval
        # elif newInterval[-1] < intervals[0][0]:
        #     result.append(newInterval)
        #     return result + intervals
        # elif newInterval[0] > intervals[-1][-1]:
        #     result.append(newInterval)
        #     return intervals + result


        # for interval in intervals:
        #     if newInterval[0] >= interval[0] and newInterval[0] <= interval[1]:
        #         newInterval[0] = interval[0]
        #         continue
        #     elif newInterval[1] >= interval[0] and newInterval[1] <= interval[1]:
        #         newInterval[0] = interval[0]
        #     else: 
        #         result.append(interval)
        #         return 

