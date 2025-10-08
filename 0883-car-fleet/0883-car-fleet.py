class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        # Sort by starting position descending (closest to target first)
        cars.sort(reverse=True)
        
        fleets = 0
        times = []
        
        for pos, spd in cars:
            time = (target - pos) / spd  # time to reach target
            if not times or time > times[-1]:
                fleets += 1       # new fleet
                times.append(time)  # record the slowest time in this fleet
            # else: car joins the fleet ahead (do nothing)
        
        return fleets
        