#!/usr/bin/env python3
"""
This module defines the main function.
"""
from pymongo import MongoClient


def main():
    """
    Prints nginx logging stats.
    """

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")

    for method in methods:
        doc_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {doc_count}")

    status = collection.count_documents(
        {
            "method": "GET",
            "path": "/status"
        }
    )

    print(f"{status} status check")


if __name__ == "__main__":
    main()
