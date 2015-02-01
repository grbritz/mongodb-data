import pymongo
import sys
import random

# establish a connection to the database
connection = pymongo.Connection("localhost", 27017)

# get a handle to the school database
db=connection.track
records =  db.tracking_records

def populate_data():
    
    try:
        records.aggregate([{"$match":{"session" : "2014_May", "course" : "M101J"}},{"$out":"May_2014_M101J"}])
    except:
        print "Unexpected error:", sys.exc_info()[0]
    

populate_data()