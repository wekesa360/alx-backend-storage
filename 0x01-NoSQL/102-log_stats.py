#!/usr/bin/env python3
"""
a python  module that provides some stats about Nginx logs
this include the method, the number of logs & top 10 most ips
"""
from cgi import print_directory
from pymongo import MongoClient

if __name__=="__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    log_collection = client.logs.nginx
    nbr_logs = log_collection.count_documents({})
    print("{} logs".format(nbr_logs))
    print("Methods")
    for mtd in methods:
        print("\tmethod {} {}".format(
            mtd, log_collection.count_documents({"method": mtd})
        ))
    nbr_checks = log_collection.count_documents({"methods": "GET", "path": "/status"})
    print("{} status check".format(nbr_checks))
    print("IPs:")
    top_10 = log_collection.aggregate([
        {

            "$group": {"_id": "$ip", "total_ips": {"$count":{}}}
        },
        {"$sort": {"total_ips":-1}},
        {"$limit": 10},
        {"$project": {"ip": "$_id", "total_ips": "$total_ips"}}
    ])
    for dc in top_10:
        print("\t{}: {}".format(dc.get("ip"), dc.get("total_ips")))