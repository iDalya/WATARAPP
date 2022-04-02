from APP import app
from flask import render_template


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('user/index.html')


@app.route('/create_account')
def create_account():
    return render_template('user/create_account.html')


@app.route('/login')
def login():
    return render_template('user/login.html')


@app.route('/profile')
def profile():
    return render_template('user/profile.html')


@app.route('/tts')
def tts():
    return render_template('user/tts.html')


@app.route('/voice_cloning')
def voice_cloning():
    return render_template('user/voice_cloning.html')


