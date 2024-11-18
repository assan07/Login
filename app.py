# app.py.
import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

from http import client

from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

connection_string = MongoClient(MONGODB_URI)
db = connection_string[DB_NAME]

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