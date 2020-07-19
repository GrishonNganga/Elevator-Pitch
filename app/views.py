from flask import Blueprint
from flask import render_template
from flask_login import current_user

app = Blueprint('app', __name__)

@app.context_processor
def inject_user():
    return dict(user=current_user)

@app.route('/')
def home():
    return render_template('home.html', user = current_user)
