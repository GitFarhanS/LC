class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        largest = 0
        while l < r:
            left = heights[l]
            right = heights[r]
            h = min(left,right)
            w = r-l
            if w*h > largest:
                largest = w*h
            if left >= right:
                r -=1
            if left < right:
                l += 1
        return largest