import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI") #variable stored in .bashrc
DBS_NAME = "myTestDB" #variable stored in mongo
COLLECTION_NAME = "myFirstMDB"#variable stored in mongo

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to the MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]


coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

document = coll.find()

for doc in document:
    print(doc)

#insert new row of data
#new_doc = {'first': 'dug', 'last': 'adam', 'dob': '11/03/1952', 'gender': 'm', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}
#coll.insert(new_doc)

#insert new rows of data
# new_docs = [{'first': 'terry', 'last': 'pratt', 'dob': '11/03/1940', 'gender': 'm', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'},{'first': 'george', 'last': 'martin', 'dob': '11/03/1920', 'gender': 'm', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'american'}]
# coll.insert_many(new_docs)

# find specific rows of data
# document = coll.find({'first': 'dug'})

# remove specific row of data
# coll.remove({'first': 'dug'})

# update rows of data
# coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
# coll.update_many to update all in this criteria