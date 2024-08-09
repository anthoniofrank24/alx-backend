#!/usr/bin/env python3
"""
This module contains a class that is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a basic caching system that inherits from BaseCaching.
    It uses a dictionary for storing cache data without any limit on size.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method should not do anything.

        Args:
            key: the key to identify the item.
            item: the item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        If key is None or
        if the key doesn't exist in self.cache_data, return None.

        Args:
            key: the key to identify the item.

        Returns:
            The value in self.cache_data linked to the key.
        """
        return self.cache_data.get(key)
