class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            del self.cache[list(self.cache.keys())[0]]