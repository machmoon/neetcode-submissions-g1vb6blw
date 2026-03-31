class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = [[temperatures[0], 0]]
        for i in range(1, len(temperatures)):
            
            while stack and stack[-1][0] < temperatures[i]:
                index = stack[-1][1]
                result[index] = i - index
                stack.pop()

            stack.append([temperatures[i], i])

        return result

    