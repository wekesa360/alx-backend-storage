#!/usr/bin/env python3
"""a python module that return all students sorted by average score"""
import pymongo


def top_students(mongo_collection):
    """
    top_students - function to return all students by average score
    Arguments:
        mongo_collection: the given mongo collection
    Returns:
        all students sorted by the average score
    """
    std_score = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"avaregeScore": -1}}
    ])
    
    return (std_score)