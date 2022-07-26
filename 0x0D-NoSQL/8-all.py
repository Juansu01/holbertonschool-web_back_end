#!/usr/bin/env python3
"""
This module defines the list_all function.
"""


def list_all(mongo_collection):
    """
    Returns all documents from collection.
    """
    docs = mongo_collection.find()
    if docs.count() != 0:
        return docs

    return []
