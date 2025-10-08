class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)  # O(n)
        maxi = 0

        for num in nums_set:  # O(n)
            # Only start counting if 'num' is the start of a sequence
            if num - 1 not in nums_set:  
                temp = 1
                current = num
                while current + 1 in nums_set:  # O(1) lookup, overall O(n) total
                    temp += 1
                    current += 1
                
                if temp > maxi:
                    maxi = temp
        
        return maxi