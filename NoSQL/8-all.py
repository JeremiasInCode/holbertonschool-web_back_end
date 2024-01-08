#!/usr/bin/env python3
"""Task 8:
    List all documents in python"""


def list_all(mongo_collection):
    """ list all document in a collection """
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
