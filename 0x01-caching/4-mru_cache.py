#!/usr/bin/env python3
"""4. MRU Caching"""
from base_caching import BaseCaching
from sys import maxsize


class MRUCache(BaseCaching):
    """
    Create a class MRUCache that inherits from BaseCaching and is a caching
    system:

    You must use self.cache_data - dictionary from the parent class
    BaseCaching
    You can overload def __init__(self): but don’t forget to call the parent
    init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the
    key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher than
    BaseCaching.MAX_ITEMS:
    you must discard the most recently used item (MRU algorithm)
    you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None
    """
    def __init__(self):
        """Constructor for the derived class"""
        super().__init__()
        self.access_age = {}

    def put(self, key, item):
        """Add an item in the cache. Overides not-implemented base class
        function with same name"""
        if key and item:
            if key in self.cache_data.keys() or len(self.cache_data) <\
                    self.MAX_ITEMS:
                self.update_cache(key, item)
            else:  # cache is full and key does not exist
                highest_age = max(self.access_age.values())
                key_highest_age = self.get_dict_key(self.access_age,
                                                    highest_age)
                discarded_item_key = key_highest_age
                self.access_age.pop(discarded_item_key)
                self.cache_data.pop(discarded_item_key)
                print("DISCARD: {}".format(discarded_item_key))
                self.update_cache(key, item)

    def update_cache(self, key, item):
        """Append a new key when the cache is not full, with unique new key"""
        next_age = 1 if len(self.cache_data) == 0\
            else max(self.access_age.values()) + 1
        # conditionally rebase access_age
        if next_age == maxsize:
            min_age = min(self.access_age.values())
            access_age = {key: (age - min_age) for key, age in
                          self.access_age.items()}
            next_age = max(self.access_age.values()) + 1
        self.access_age.update({key: next_age})
        self.cache_data.update({key: item})

    def get_dict_key(self, mydict, value):
        """Return the first matching key for a given dict value or None if it
        does not exist"""
        for key in mydict.keys():
            if mydict[key] == value:
                return key
        return None

    def get(self, key):
        """ Get an item by key. Overides not-implemented base class
        function with same name
        """
        if key and key in self.cache_data:
            next_age = 1 if len(self.cache_data) == 0\
                else max(self.access_age.values()) + 1
            # conditionally rebase access_age
            if next_age == maxsize:
                min_age = min(self.access_age.values())
                access_age = {key: (age - min_age) for key, age in
                              self.access_age.items()}
                next_age = max(self.access_age.values()) + 1
            self.access_age.update({key: next_age})
        return self.cache_data.get(key)


if __name__ == "__main__":
    pass
