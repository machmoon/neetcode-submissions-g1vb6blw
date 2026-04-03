class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        result = r

        while l <= r:

            m = (l+r)//2

            hours_for_eating_rate = 0
            for i in range(len(piles)):
                hours_for_eating_rate += math.ceil(piles[i] / m)

            if hours_for_eating_rate <= h:
                r = m - 1
                result = min(result, m)

            elif hours_for_eating_rate > h:
                l = m + 1

        return result