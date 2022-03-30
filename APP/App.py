from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/FAQs')
def faq():
    return render_template('faq.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/tts')
def tts():
    return render_template('tts.html')

@app.route('/voice_cloning')
def voice_cloning():
    return render_template('voice_cloning.html')

if __name__ == '__main__':
    app.run(debug=True)