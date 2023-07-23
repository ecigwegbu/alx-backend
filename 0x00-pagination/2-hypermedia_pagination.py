#!/usr/bin/env python3
"""0. Simple helper function"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Write a function named index_range that takes two integer arguments
    page and page_size.

    The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1."""
    if page_size < 0 or page < 0:
        return (0, 0)
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a method named get_page that takes two integer arguments
        page with default value 1 and page_size with default value 10.
        You have to use this CSV file (same as the one presented at the top
        of the project)
        Use assert to verify that both arguments are integers greater than 0.
        Use index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset (i.e. the
        correct list of rows).
        If the input arguments are out of range for the dataset, an empty list
        should be returned."""
        # first qc indut with assert
        assert type(page) == int and type(page_size) == int and\
            page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        if start_index < 0 or start_index >= len(self.dataset()) or\
                end_index < 0 or end_index >= len(self.dataset()):
            return []
        return self.dataset()[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing the
        following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation.
        You can use the math module if necessary."""
        total_data_size = len(self.dataset())
        total_pages = None
        prev_page = None
        next_page = None
        try:
            data = self.get_page(page, page_size)
            returned_page_size = len(data)
            total_pages = math.ceil(total_data_size / page_size)
            prev_page = page - 1 if page >= 2 else None
            next_page = page + 1 if page < total_pages else None
        except AssertionError:
            data = []
            returned_page_size = 0
            if type(page_size) == int and page_size > 0:  # page is the prob
                total_pages = math.ceil(total_data_size / page_size)
                next_page = 1
            elif type(page_size) == int and page_size == 0:  # special case ?
                page = None
            if type(page) == int and page > 0 and total_pages is not None:
                prev_page = page - 1 if page >= 2 else None
                next_page = page + 1 if page < total_pages else None
        return {
            "page_size": returned_page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
