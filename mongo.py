import pymongo

if __name__=="__main__":
    print("welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['ravi']
    collection=db['mysamplecollectionforHarry']
    dictionary={'name':'Harry','marks':'90','address':'odi'}
    collection.insert_one(dictionary)
    