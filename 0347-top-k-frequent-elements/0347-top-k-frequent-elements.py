class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # O(n) time
        

        return heapq.nlargest(k, freq.keys(), key=freq.get)  # O(m log k)

        