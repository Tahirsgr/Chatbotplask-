from flask import Flask
from flask import render_template

app =Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    Sitename = 'First project in flask'
    fname="tahir"
    lname="khan"
    email='tahir@gmail.com'
    return render_template('index.html', title="welcome",  fastname=fname,lname=lname, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=84)
