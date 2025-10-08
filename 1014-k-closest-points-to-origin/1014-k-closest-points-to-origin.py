class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        point_map = []

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(point_map, (-distance, x, y))
            if len(point_map) > k:
                heapq.heappop(point_map)
        
        return [(x, y) for (dist, x, y) in point_map]
