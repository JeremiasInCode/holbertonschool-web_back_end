#!/usr/bin/env python3
"""Task 11"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of schools having
      a specific topic"""
    topics = mongo_collection.find({"topics": topic})
    return topics
