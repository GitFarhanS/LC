class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h

        while left <= right:
            middle = (left + right) //2
            if k_works(middle):
                right = middle-1
            else:
                left = middle+1
        
        return left     