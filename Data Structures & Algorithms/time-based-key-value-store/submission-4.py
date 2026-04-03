from collections import defaultdict
class TimeMap:
    

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        l, r = 0, len(self.timeMap[key]) - 1

        result = ""
        while l <= r:
            m = (l+r)//2

            if self.timeMap[key][m][1] <= timestamp:
                l = m+1
                result = self.timeMap[key][m][0]
            else:
                r = r-1
        return result

        
