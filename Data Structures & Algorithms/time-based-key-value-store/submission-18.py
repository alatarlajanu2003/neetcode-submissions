class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((timestamp, value))
        else:
            self.data[key] = [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:
        key_elems = self.data.get(key, "")
        if not key_elems:
            return ""

        l, r = 0, len(key_elems) - 1
        smallest_delta = float('inf')
        result = None

        while l <= r:
            m = l + (r - l) // 2
            
            delta = timestamp - key_elems[m][0]
            if delta < smallest_delta and delta >= 0:
                result = key_elems[m]

            if key_elems[m][0] == timestamp:
                break
            elif key_elems[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        if not result:
            return ""
            
        return result[1]
