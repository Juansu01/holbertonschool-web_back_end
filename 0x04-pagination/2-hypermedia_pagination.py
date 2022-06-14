#!/usr/bin/env python3
"""
Simple pagination moduel
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


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
        """
        Gets pagination of the cached dataset.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()

        if self.__dataset:
            first_idx, second_idx = index_range(page, page_size)
            return self.__dataset[first_idx:second_idx]

        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary with information about the
        current dataset.
        """

        data_set = self.__dataset
        if data_set:
            set_size = 0
        else:
            set_size = len(data_set)

        total_pages = math.ceil(set_size / page_size) if data_set else 0

        return {
            'page_size': page_size,
            'page': page,
            'data': data_set,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
