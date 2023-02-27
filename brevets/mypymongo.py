import os
from pymongo import MongoClient
import arrow
import sys

# set up mongo connection
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
# use mydb database
db = client.brevets
# use tables collection
collection = db.tables

# define two functions
 
def brevet_insert(brevet_dist, start_time, checkpoints):
    """
    Inserts a new to-do list into the database "todo", under the collection "lists".
    
    Inputs a title (string) and items (list of dictionaries)

    Returns the unique ID assigned to the document by mongo (primary key.)
    """
    output = collection.insert_one({
        "brevet": brevet_dist,
        "start": start_time,
        "checkpoints": checkpoints})

    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)


def brevet_find():
    # return start_time, brvet_dist, checkpoint
    """
    Obtains the newest document in the "lists" collection in database "todo".

    Returns brevet (string) and items (list of dictionaries) as a tuple.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    lists = collection.find().sort("_id", -1).limit(1)

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for table in lists:
        # We store all of our lists as documents with two fields:
        ## brevet: string # brevet value
        ## items: list   # list of items:

        ### every item has three fields:
        #### brevet: int   # description
        #### start: string  # priority
        #### checkpoints: list # checkpoints
        return table["brevet"], table["start"], table["checkpoints"]
