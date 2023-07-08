import os
from flask import Flask, render_template, flash, redirect, url_for, Markup, request, jsonify
app = Flask(__name__)
app.loqate_user = "\"" + os.getenv('LOQATE_USER') + "\"" 
app.loqate_password = "\""  + os.getenv('LOQATE_PASSWORD') + "\"" 

@app.route('/')
def index():
    return render_template('index.html',user=app.loqate_user,password=app.loqate_password)

@app.route('/home',methods=['POST'])
def home():
    print ("In home")
    return render_template('index.html',user=app.loqate_user,password=app.loqate_password)

@app.route('/process/<chosen_address>')
def process(chosen_address):
    print (type(chosen_address))
    print (chosen_address)
    return render_template("result.html", chosen_address = chosen_address)

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
