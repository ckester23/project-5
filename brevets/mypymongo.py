import os
from pymongo import MongoClient
import arrow

app = Flask(__name__)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb


# define two functions

def brevet_insert(start_time, brevet_dist, checkpoint):
    pass

def brevet_find():
    # return start_time, brvet_dist, checkpoint
    pass
