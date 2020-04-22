import pymongo
import os

from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.getenv("MONGO_URI") #variable stored in .bashrc
DBS_NAME = "myTestDB" #variable stored in mongo
COLLECTION_NAME = "myFirstMDB"#variable stored in mongo

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to the MongoDB: %s") % e

def show_menu():
    print('')
    print("1. Add a record")
    print("2. Find a record")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter Option: ")
    return option

def get_record():
    print('')
    first = input('Enter first name: ')
    last = input('Enter last name: ')

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print('Error accessing the database')

    if not doc:
        print('')
        print('Error no results found')
    
    return doc

def add_record():
    print('')
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    dob = input('Enter date of birth name: ')
    gender = input('Enter gender(m/f): ')
    hair_colour = input('Enter hair colour: ')
    occupation = input('Enter occupation: ')
    nationality = input('Enter nationality: ')

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender.lower(), 'hair_colour': hair_colour.lower(), 'occupation': occupation.lower(), 'nationality': nationality.lower(), }

    try:
        coll.insert(new_doc)
        print('')
        print('Document inserted')
    except:
        print("Error accessing the database")

def find_record():
    doc = get_record()
    if doc:
        print('')
        for k,v in doc.items():
            if k!= "_id":
                print(k.capitalize() + ": " + v.capitalize())

def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print('')
        for k,v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] >")
                
                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {'$set': update_doc})
            print('')
            print('Document updated')
        except:
            print("Error accessing database")

def delete_record():
    doc = get_record()

    if doc:
        print('')
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print('')
        confirmation = input("is this the correct record you would like to delete? \nY or N > ")
        print('')

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print('Document deleted')
            except:
                print('Error accessing database')
        else:
            print('Document not deleted')

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print('This is not a valid option')
        print('')

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()