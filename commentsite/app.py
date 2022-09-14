from flask import Flask, render_template, request, jsonify
from ignore.secure import MYDBURL
app = Flask(__name__)
import certifi
ca=certifi.where()
from pymongo import MongoClient
client = MongoClient(MYDBURL,tlsCAFile=ca)
db = client.wakhoo

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.homework.insert_one(doc)
    return jsonify({'msg':'응원 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5030, debug=True)