#!/usr/bin/env python3
"""0. Simple helper function"""
import typing


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Write a function named index_range that takes two integer arguments
    page and page_size.

    The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1."""
    if page_size < 0 or page < 0:
        return (0, 0)
    return ((page - 1) * page_size, page * page_size)
