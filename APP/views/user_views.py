from APP import app
from flask import render_template,redirect,request

from flask_wtf import FlaskForm

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('user/index.html')


@app.route('/create_account',methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        req = request.form
        #print(req)
        name = request.form["name"]
        username = request.form["username"]
        email =  request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]
        country = request.form["country"]
        gender = request.form["gender"]
        birthdate = request.form["birthdate"]
        return redirect(request.url)
    return render_template('user/create_account.html')


@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == "POST":
        req = request.form
        #print(req)
        email =  request.form["email"]
        password = request.form["password"]
        
    return render_template('user/login.html')


@app.route('/profile')
def profile():
    return render_template('user/profile.html')


@app.route('/edit_profile',methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        req = request.form
        #print(req)
        name = request.form["name"]
        username = request.form["username"]
        email =  request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]
        country = request.form["country"]
        gender = request.form["gender"]
        birthdate = request.form["birthdate"]
    
        return redirect(request.url)
    return render_template('user/profile.html')

@app.route('/tts')
def tts():
    return render_template('user/tts.html')


@app.route('/voice_cloning')
def voice_cloning():
    return render_template('user/voice_cloning.html')


