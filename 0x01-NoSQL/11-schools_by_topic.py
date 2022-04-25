#!/usr/bin/env python3
import pymongo
""" a python module that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic) -> list:
    """
    school_by_topic - function that finds list in schools
    Arguments:
        mongo_collection: the given mongo collection
        topic: the topic to be searched
    Returns:
        list of school
    """
    output: list = []
    for dc in mongo_collection.find({"topics": topic}):
        output.append(dc)
    return output