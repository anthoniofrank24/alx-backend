#!/usr/bin/env python3
"""
This module contains a FIFO Cache method that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    This is a class that inherits from BasicCaching.
    It uses a dictionary for storing cache data with a FIFO
    (First-In, First-Out) eviction policy.
    """
    def __init__(self):
        """
        Initialize the FIFOCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data
            is higher than BaseCaching.MAX_ITEMS,
            discard the first item put in cache (FIFO algorithm)
            and print DISCARD: <key>.

            Args:
                key: the key to identify the item.
                item: the item to be cached.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_in_key = self.order.pop(0)
                del self.cache_data[first_in_key]
                print(f'DISCARD: {first_in_key}')

    def get(self, key):
        """
        Get an item by key.
            If key is None or if the key doesn't exist in self.cache_data,
            return None.

            Args:
                key: the key to identify the item.

            Returns:
                The value in self.cache_data linked to the key.

        """
        return self.cache_data.get(key)
