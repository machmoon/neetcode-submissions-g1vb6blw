class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack
        # sort the positions
        # push that onto stack
        # majic number till desitnation if less than
        # update and update count

        # 7, 4, 1, 0
        # 1, 2, 2, 1

        zipped = zip(position, speed)
        result = 0
        
        sorted_stack = sorted(zipped, key=lambda x: -x[0])
        # print(sorted_stack, sorted_stack[::-1])
        
        fleet_time = 0
        while sorted_stack:
            if (target - sorted_stack[0][0])/sorted_stack[0][1] > fleet_time:
                fleet_time = (target - sorted_stack[0][0])/sorted_stack[0][1] 
                result+=1
            sorted_stack.pop(0)

        return result

