from flask import Flask
from flask import request

# This is for GitHub.
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

# /user-profile/fatih
# /user-profile/omer
@app.route('/user-profile/<name>')
def my_name(name):
    return 'My profile name: ' + name

@app.route('/signIn')
def sign_in():
    email_val = request.args.get('email')
    password_val = request.args.get('password')
    if not (email_val and password_val):
        return {
            'error': 'email and password do not exist!!!'
        }
    return {
        'email': email_val,
        'password': password_val,
    }

if __name__ == '__main__':
   app.run()
