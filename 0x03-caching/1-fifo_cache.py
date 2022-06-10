#!/usr/bin/python3
"""FIFOCache module."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class."""

    def __init__(self):
        """Init constructor."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds item to cache."""
        if key and item:
            if key not in self.queue:
                self.queue.append(key)
            else:
                self.mv_last_list(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = self.get_first_list(self.queue)
                if first:
                    self.queue.pop(0)
                    del self.cache_data[first]
                    print(f"DISCARD: {first}")
        else:
            return

    def get(self, key):
        """Returns item from cache using key."""
        return self.cache_data.get(key)

    def mv_last_list(self, item):
        """Moves item to the last index of list."""
        size = len(self.queue)

        if self.queue[size - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """Gets the first element of list
        Returns None if list is None
        """
        if array:
            return array[0]
        return None
