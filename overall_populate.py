import pymongo
import sys
import random

# establish a connection to the database
connection = pymongo.Connection("localhost", 27017)

# get a handle to the school database
db=connection.track
records =  db.tracking_records
dev = db.overall_sample_set

def populate_data():
    try:
        arr = []
        count = 0
        cursor = records.find()
        for doc in cursor:
            if (random.random() < 0.01):
                arr.append(doc)
            if (count % 1000 == 0):
                dev.insert(arr)
                arr = []
            count += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    

populate_data()