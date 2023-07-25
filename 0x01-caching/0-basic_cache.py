#!/usr/bin/env python3
"""0. Basic dictionary"""
from sys import maxsize
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache that inherits from BaseCaching and is a
    caching system:

    You must use self.cache_data - dictionary from the parent class
    BaseCaching
    This caching system doesn’t have limit
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key
    key.
    If key or item is None, this method should not do anything.
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None
    """
    def __init__(self):
        """Constructor for the derived class"""
        super().__init__()
        # self.MAX_ITEMS = maxsize

    def put(self, key, item):
        """Add an item in the cache. Overides not-implemented base class
        function with same name"""
        if key is not None:
            self.cache_data.update({key: item})  # [key] = item

    def get(self, key):
        """ Get an item by key. Overides not-implemented base class
        function with same name
        """
        return self.cache_data.get(key)


if __name__ == "__main__":
    pass
