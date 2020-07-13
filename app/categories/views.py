from flask import render_template, Blueprint

category = Blueprint('category', __name__)

@category.route('/categories')
def show_categories():
    categories = ['Business', 'Comedy', 'Casual', 'Dating', 'Social', 'Interviews']
    return render_template('category/categories.html', categories = categories)

@category.route('/<category>')
def show_category(category):
    return render_template('category/category.html', category = category)

@category.route('/<category>/<int:id>')
def show_pitch(category, id):
    return render_template('category/pitch.html')