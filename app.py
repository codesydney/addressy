import os
from flask import Flask, render_template, flash, redirect, url_for, Markup, request
app = Flask(__name__)
app.loqate_user = "\"" + os.getenv('LOQATE_USER') + "\"" 
app.loqate_password = "\""  + os.getenv('LOQATE_PASSWORD') + "\"" 


@app.route('/')
def index():
    return render_template('index.html',user=app.loqate_user,password=app.loqate_password)

@app.route('/show_insights',methods=['POST'])
def show_insights():
  print ("In show_insights")      
 
# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
