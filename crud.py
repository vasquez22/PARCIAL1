from conection_parameters import collection
import json

def read_libros(id=None):
    if id is not None:
        query = {"_id": id}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)

def create_libros(json_libros):
    result = collection.insert_one(json_libros)
    print(result.inserted_id)

def update_libros(id, json_libros_update):
    query = {"_id": id}
    new_values = {"$set": json_libros_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)