from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello! this is the main page <h1>HELLO<h1>'


@app.route('/<where>')
def user(where):
    files = os.listdir('templates/')
    if where in files:
            return render_template(where)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()
