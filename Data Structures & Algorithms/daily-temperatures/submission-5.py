class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            while stack:
                if stack[-1][0] > temperatures[i]:
                    result[i] = stack[-1][1] - i 
                    break
                else:
                    stack.pop()
                
            stack.append([temperatures[i], i])
            

        return result