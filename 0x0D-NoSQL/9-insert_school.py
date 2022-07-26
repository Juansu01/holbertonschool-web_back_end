#!/usr/bin/env python3
"""
This module defines the insert_school function.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns new id from inserted document.
    """
    return mongo_collection.insert(kwargs)
