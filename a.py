# import pymongo


# client = pymongo.MongoClient("mongodb+srv://revus:revus@cluster0.n76oc9r.mongodb.net/?retryWrites=true&w=majority")  
# for name in client.list_database_names():  
#     print(name)  

# collection = client.Data_ja  
# data = [{
#     "java":0,"c":0,"python":0
# },{"comments":""}]
# collection.insert_one(data)
# # for database_name in client.list_database_names():  
# #     print("Database - "+database_name)  
# #     for collection_name in client.get_database(database_name).list_collection_names():  
# #         print(collection_name)  
import pymongo

from pymongo import MongoClient

from pymongo import collection

cluster = MongoClient(

    'mongodb+srv://revus:revus@cluster0.n76oc9r.mongodb.net/?retryWrites=true&w=majority')

db = cluster["sldb"]

collection = db["employee"]

post = {"name": "amar", "email": "amar@mail.com"}

collection.insert_one(post)