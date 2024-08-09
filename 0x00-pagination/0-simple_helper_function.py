#!/usr/bin/env python3
"""
This module contains function that paginates a page based on
some parameters
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    This function return a tuple of size two containing
    a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
