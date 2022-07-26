#!/usr/bin/env python3
"""
This module defines the update_topics function.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the MongoDB collection with topics.
    """
    query = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_topics)
