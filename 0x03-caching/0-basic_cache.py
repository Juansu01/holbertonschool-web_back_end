#!/usr/bin/python3
"""Basic Cache module."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Base Cache class."""

    def put(self, key, item):
        """Adds item to cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns item from cache using key."""
        return self.cache_data.get(key)
