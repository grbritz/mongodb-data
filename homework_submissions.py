
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("localhost", 27017)

# get a handle to the school database
db=connection.track
records =  db.May_2014_M101J

def get_data():
    
    try:
        cursor  = records.aggregate([{"$group": {"_id":"$student_id"}}],cursor={})
    except:
        print "Unexpected error:", sys.exc_info()[0]

    for rec in cursor:
        print "hello1"
        stud = rec['_id']
        #print stud
        cursor2 = records.aggregate([
                        {"$match":{"student_id":stud}},
                        # {"$limit":5},
                        {"$unwind":"$events"},
                        {"$match":
                            {"events.event_type":"submit",
                            "events.lesson_format":"homework",
                            "events.correct":"true"}
                        },
                        {"$group":{"_id":
                            {"chapter":"$events.chapter",
                            "lesson":"$events.lesson"}, 
                            "sum":{"$sum":1}
                            }
                        }
                        ],cursor={})

        for doc in cursor2:
            #print "hello2"
            print doc
            hw_submissions=open('./hw_submissions', 'a')
            hw_submissions.write(email + "," + name + "," + game + "\n")


get_data()