# 146. LRU Cache
# https://leetcode.cn/problems/lru-cache//description/?envType=problem-list-v2&envId=2cktkvj


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRUCache with a given capacity.
        :param capacity: The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest_key = self.order.pop(0)
            del self.cache[oldest_key]
        self.cache[key] = value
        self.order.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
