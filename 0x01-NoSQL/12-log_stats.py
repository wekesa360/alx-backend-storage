#!/usr/bin/env python3
from pymongo import MongoClient
""" a python module that provides some stats about Nginx logs"""

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    log_collection = client.logs.nginx
    nbr_logs = log_collection.count_documents({})
    print("{} logs".format(nbr_logs))
    print("Methods:")
    for mtd in methods:
        print("\tmethod {} {}".format(
            mtd, log_collection.count_documents({"methods": mtd})
        ))
    nbr_checks = log_collection.count_documents(
        {"methods": "GET", "path": "/status"})
    print("{} status check".format(nbr_checks))