#!/usr/bin/env python3
"""
This module defines the schools_by_topic function.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Resturns list of schools that have the
    required topic.
    """
    docs = mongo_collection.find({"topics": topic})
    return [doc for doc in docs]
