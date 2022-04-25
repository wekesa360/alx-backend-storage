#!/usr/bin/env python3
import pymongo
"""a python module to change all the topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """
    update_topics - function to update topics of a school
    Arguments:
        mongo_collection: the given mongo collection
        name: the school name to be updated
        topic: list of topics
    Returns:
        nothing
    """
    rqrd_attr = {"name": name}
    updt_attr = {"$set": {"topics":topics}}
    mongo_collection.update.update_many(rqrd_attr, updt_attr)