class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        unsort = []
        for key, value in counts.items():
            unsort.append([value, key])
        
        result = sorted(unsort)[::-1]
        print(result)
        answer = []
        for i in range(k):
            answer.append(result[i][1])

        return answer
        