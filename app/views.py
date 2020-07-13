from flask import Blueprint
from flask import render_template

app = Blueprint('app', __name__)

@app.route('/')
def check_view():
    return render_template('base.html')