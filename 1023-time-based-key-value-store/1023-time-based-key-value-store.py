class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        val_time = self.time_map[key]
        L = 0
        R = len(val_time) - 1
        biggest = ""
        while L <= R:
            MID = (L+R)//2
            if val_time[MID][1] <= timestamp:
                L = MID +1
                biggest = val_time[MID][0]
            else:
                R = MID - 1
        return biggest



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)