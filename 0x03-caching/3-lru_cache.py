#!/usr/bin/python3
""" LRU Caching module."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LIFOCache class."""

    def __init__(self):
        """Init constructor."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds item to cache."""
        if key and item:

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_el = self.get_first_list(self.queue)
                if first_el:
                    self.queue.pop(0)
                    del self.cache_data[first_el]
                    print(f"DISCARD: {first_el}")

            if key not in self.queue:
                self.queue.append(key)
            else:
                self.mv_last_list(key)

        else:
            return

    def get(self, key):
        """Returns item from cache using key."""
        item = self.cache_data.get(key)
        if item:
            self.mv_last_list(key)
        return item

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
