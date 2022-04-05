from APP import app
from flask import Flask,session
import APP
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,TextAreaField,EmailField,PasswordField,TelField,DateField
from wtforms.validators import DataRequired

APP.app.config['SECRET_KEY'] = 'mysecretkey'
#contact us form

class ContactUsForm(FlaskForm):
    subject = StringField() #type text , placeholder
    issue = SelectField("",choices=[('',''),('enquiry','استفسار'),('complaint','شكوى')])
    issueMsg = TextAreaField()
    email = EmailField('البريد الإلكتروني') #validators.Email()
    submit = SubmitField('إرسال')

#edit user profile form 
class EditProfileForm(FlaskForm):
    name = StringField('',validators=[DataRequired()]) #type text
    username = StringField('',validators=[DataRequired()]) #type text
    email = EmailField('',validators=[DataRequired()]) 
    password = PasswordField() #field name
    phone = TelField() #field name
    country = SelectField('',choices=[('','السعودية'),('','الأردن'),(),(),()],validators=[DataRequired()]) #add choices later
    gender = SelectField('',choices=[('female','أنثى'),('male','ذكر')],validators=[DataRequired()])
    birthdate = DateField('', validators=[DataRequired()]) #https://stackoverflow.com/a/19759661
    #زر لسماع صوته المنسوخ
    
    submit = SubmitField('تعديل الملف الشخصي')

#TTS form
class TTSform(FlaskForm):
    TTStxt = TextAreaField()
    voice = SelectField(('','سارة (أنثى)'),('','محمد (ذكر)'),('','عمر (طفل)'))
    submit = SubmitField(' تحويل النص إلى صوت')



#@app.route('', methods=['GET','POST'])
def handle_ContactUsForm():
    form = ContactUsForm()
    if form.validate_on_submit():
        session['subject'] = form.subject.data
        session['issue'] = form.issue.data
        session['issueMsg'] = form.issueMsg.data
        session['email'] = form.email.data

        return ''
       
def handle_EditProfileForm():
    form = EditProfileForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['username'] = form.username.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        session['phone'] = form.phone.data
        session['country'] = form.country.data
        session['gender'] = form.gender.data
        session['birthdate'] = form.birthdate.data

        return ''

def handle_TTSform():
    form = TTSform()
    if form.validate_on_submit():
        session['TTStxt'] = form.TTStxt.data
        session['voice'] = form.voice.data

        return ''

if __name__ == '__main__':
    APP.app.run(debug=True)
