class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i : i[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])

        return output


        # new_interval = [-1, -1]

        # for i in range(1, len(intervals)):
        #     # if the last interval end is greater than or equal to the current interval start we modify a new interval to combine then 
        #     if intervals[i-1][1] >= intervals[i][0]:
        #         new_interval.append([min(result[0], intervals[i][0]), max(result[1], intervals[i][1])])
        #     elif intervals[i-1][1] < intervals[i][0]:
        #         result.append(new_interval)
        #         return result + intervals[i:]
        
        return intervals