#!/usr/bin/env python3
"""0. Basic dictionary"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Create a class FIFOCache that inherits from BaseCaching and is a
    caching system:

    You must use self.cache_data - dictionary from the parent class
    BaseCaching
    You can overload def __init__(self): but don’t forget to call the parent
    init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key
    key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher than
    BaseCaching.MAX_ITEMS:
    you must discard the first item put in cache (FIFO algorithm)
    you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None.
    """
    def __init__(self):
        """Constructor for the derived class"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache. Overides not-implemented base class
        function with same name"""
        if key and item:
            if key in self.cache_data.keys() or len(self.cache_data) <\
                    self.MAX_ITEMS:
                self.cache_data.update({key: item})
            else:
                discarded_item_key = next(iter(self.cache_data))
                self.cache_data.pop(discarded_item_key)
                print("DISCARD: {}".format(discarded_item_key))
                self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key. Overides not-implemented base class
        function with same name
        """
        return self.cache_data.get(key)


if __name__ == "__main__":
    pass
