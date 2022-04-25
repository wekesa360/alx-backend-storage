#!/usr/bin/env python3
from typing import Any
import pymongo
"""a python module that inserts new document based on kwargs"""


def insert_school(mongo_collection, **kwargs) -> Any:
    """
    insert_school - function to insert a new document based on kwargs
    Arguments:
        mongo_coolection: the given mongo collection
        kwargs: the given argument to be inserted
    Returns:
        the id of the new document
    """
    school = mongo_collection.insert_one(kwargs)
    return (school.inserted_id)