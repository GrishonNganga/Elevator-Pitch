from flask import Blueprint, render_template

from .forms import RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    
    return render_template('auth/login.html')

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return form.f_name.data
    return render_template('auth/register.html', register_form = form)
