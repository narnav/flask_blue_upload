
from flask import render_template, Blueprint


main = Blueprint('main', __name__, url_prefix='', template_folder='templates')

# main blueprint
# INDEX


@main.route('/')
def index():
    return render_template('index.html')


# about
@main.route('/about')
def about():
    return render_template('about.html')
