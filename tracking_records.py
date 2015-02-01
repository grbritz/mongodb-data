
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("localhost", 27017)

# get a handle to the school database
db=connection.track
records =  db.tracking_records

def get_data():
    
    try:
        cursor  = records.aggregate([{"$group": {"_id":"$student_id"}},{"$limit":5}])
    except:
        print "Unexpected error:", sys.exc_info()[0]

    for rec in cursor:
        stud = cursor[rec]
        cursor2 = records.aggregate([
                        {"$match":{"student_id":stud}},
                        {"$limit":5},
                        {"$unwind":"$events"},
                        {"$match":
                            {"events.event_type":"submit",
                            "events.lesson_format":"homework"}
                        },
                        {"$group":{"_id":
                            {"chapter":"$events.chapter",
                            "lesson":"$events.lesson"}, 
                            "sum":{"$sum":1}
                            }
                        }])

        for doc in cursor2:
            print doc

get_data()