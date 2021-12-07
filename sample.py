from flask import Flask, request, jsonify
import pymongo
app = Flask(__name__)

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['Harry']
collection=db['mysamplecollectionforHarry']


@app.route('/foo', methods=['POST']) 
def foo():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message":"request received"})

if __name__=='__main__':
    app.run(debug=True,port=8080)








