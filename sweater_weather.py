from flask import Flask, render_template, redirect, flash, session

from jinja2 import StrictUndefined

app = Flask(__name__)

# TO-DO: add secret key to secrets.sh
app.secret_key = 'ABC'

# used so an error will be raised if jinja tries to reference an undefined variable
app.jinja_env.undefined = StrictUndefined

# makes app auto-reload in debug mode
app.jinja_env.auto_reload = True

@app.route('/')
def index():
    """"Render index page."""

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

app.run(port=5000)
