import os
from flask import Flask, render_template, flash, redirect, url_for, Markup, request, jsonify, json, g
import sqlite3
import os.path

app = Flask(__name__)
app.loqate_user = "\"" + os.getenv('LOQATE_USER') + "\"" 
app.loqate_password = "\""  + os.getenv('LOQATE_PASSWORD') + "\"" 

@app.route('/')
def index():
    return render_template('index.html',user=app.loqate_user,password=app.loqate_password)

@app.route('/home',methods=['POST'])
def home():
    return render_template('index.html',user=app.loqate_user,password=app.loqate_password)

@app.route('/process/<chosen_address>')
def process(chosen_address):
    print('chosen_address', chosen_address)

    data = json.loads(chosen_address)
    fullAddress = data["fullAddress"]
    print('fullAddress', fullAddress)

    postcode = data["postcode"]
    print('postcode', postcode)

    db_dir = ('/Users/engramarbollas/Projects/addressy/nswgovschools.db')
    conn = sqlite3.connect(db_dir)
    print ("XXX Opened database successfully")

    details_cur = conn.execute(
        'select School_name, Town_suburb, Postcode from NSW_govt_schools_master_dataset where Postcode = ? COLLATE NOCASE', [postcode])
    
    details = details_cur.fetchall()
    print('details------>', details)

    return_values = []

    print ('before return_values---------> ',return_values);

    for detail in details:
        detail_dict = {}
        detail_dict['School_name'] = detail['School_name']
        detail_dict['Town_suburb'] = detail['Town_suburb']
        detail_dict['postcode'] = detail['postcode']
        return_values.append(detail_dict)
        
    print ('after return_values---------> ',return_values);
    return render_template("result.html", 
                        fullAddress = fullAddress, return_values=return_values)

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500