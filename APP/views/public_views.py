from APP import app
from flask import render_template,request,redirect


@app.route('/contact_us',methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        req = request.form
        #print(req)
        subject = request.form["subject"]
        issue = request.form["issue"]
        issueMsg = request.form["issueMsg"]
        email = request.form["email"]
    
        return redirect(request.url)
    return render_template('public/contact_us.html')


@app.route('/FAQs')
def faq():
    return render_template('public/faq.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('public/404.html'), 404