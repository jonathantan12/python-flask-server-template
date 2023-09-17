from flask import Flask
from flask import request
from app import app

@app.route("/")
def home():
    return "The server is running!"

