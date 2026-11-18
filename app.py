from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

mongo_client = MongoClient('mongodb://mongo:27017/')
mongo_db = mongo_client['tp-docker1']

@app.route('/')
def hello():
    mongo_client.admin.command('ping')
    print("test ok")
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)