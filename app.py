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

@app.route('/home',methods=['GET', 'POST'])
def home():
    return render_template('index.html',user=app.loqate_user,password=app.loqate_password)

@app.route('/process', methods=['GET', 'POST'])
def process():
    if (request.method == "POST"):
        fullAddress = str(request.json['fullAddress'])
        postcode = str(request.json['postcode'])

        db_dir = ('/Users/engramarbollas/Projects/addressy/nswgovschools.db')
        conn = sqlite3.connect(db_dir)
        print ("Opened database successfully")

        details_cur = conn.execute(
            'select School_name, Town_suburb, Postcode from NSW_govt_schools_master_dataset where Postcode = ? COLLATE NOCASE', [postcode])
        
        details = details_cur.fetchall()
        print('details------>', details)

    return render_template("result.html", 
                            fullAddress = fullAddress, details = details)

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)