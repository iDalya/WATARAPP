from APP import app
from flask import render_template


@app.route('/contact_us')
def contact_us():
    return render_template('public/contact_us.html')


@app.route('/FAQs')
def faq():
    return render_template('public/faq.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('public/404.html'), 404