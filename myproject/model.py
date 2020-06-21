from pymongo import MongoClient
import dns

client = MongoClient("mongodb+srv://ahmed:yt2kMlCzVVLT5A9d@flaskapp1-lohte.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
class Database:


    def insert_into(self, TABLE_NAME,DATA):
        collection=db[TABLE_NAME].insert(DATA)

    def read_all(self, TABLE_NAME):
        collection=db[TABLE_NAME].find()
        return collection
    def read_one(self, TABLE_NAME,DATA):
        collection=db[TABLE_NAME].find_one(DATA)
        return collection
    def Delete_one(self, TABLE_NAME,DATA):
        collection=db[TABLE_NAME].remove(DATA)
        return collection
    def Delete_all(self, TABLE_NAME):
        collection=db[TABLE_NAME].remove_all()
        return collection
    def update(self, TABLE_NAME,where,DATA):
        collection=db[TABLE_NAME].update_many(where, DATA)
        return collection
emp_rec1 = { 
        "name":"Mr.hello",  
        "eid":24, 
        "location":"kuala-lumpur"
        } 
emp_rec2 = { 
        "name":"Mr.Shaurya", 
        "eid":14, 
        "location":"cairo"
        } 

database= Database()
table='mytable'

try :
    # database.insert_into(table, emp_rec1)
    condition={

     "name":"Mr.Shaurya"
    }
    # i_fount_it=database.read_one(table, condition)
    # print(i_fount_it)
    # database.Delete_one(table, emp_rec1)
    database.update(table,{
        '_id': '5e2d2f23ec20d225a8236d2a'},{
           "$set":{
               "name":"mr.abook Geek"
           },
            "$currentDate":{"lastModified":True} 
        })
    reads=database.read_all(table)
    for read in reads:
        print(read)
except Exception as e :
    print (e)
