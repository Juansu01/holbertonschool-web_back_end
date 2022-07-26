#!/usr/bin/env python3
"""
This module defines the update_topics function.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the MongoDB collection with topics.
    """

    topic_to_update = {"$set": {"topics": topics}}
    mongo_collection.update_many({"name": name}, {topic_to_update})
