import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
import .models import db, testpmk
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    title = "main"
    return render_template('home.html')

@app.route('/table')
def table_page():
    title = "table"
    return render_template('table.html')

@app.route('/listin')
def listin_page():
    title = "listin"
    songList = ["MAZKO - S4nri0", "fakken777angel - Гладиатор", "Hesitation - Andrew Garden"]
    return render_template('listin.html', songList=songList)

@app.route('/image')
def image_page():
    title = "image"
    return render_template('image.html')

@app.route('/text')
def text_page():
    title = "text"
    text ="текст"
    return render_template('text.html', text=text)

@app.route('/auth', methods=['POST', 'GET'])
def auth_page():
    title = "auth"
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']
        return render_template ('auth_result.html', username=username, password=password)
    else:
        return render_template('auth.html')
    

if __name__ == '__main__':
    app.run()
