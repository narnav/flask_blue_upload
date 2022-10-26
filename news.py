from flask import render_template, Blueprint


news = Blueprint('news', __name__, url_prefix='/news',
                 template_folder='templates')

# new blueprint
# news


@news.route('/', methods=['GET', 'POST'])
def news_main():
    return render_template('news.html')

# news/world


@news.route('/world')
def world():
    return render_template('world.html')

# new/polity


@news.route('/polity')
def polity():
    return render_template('polity.html')
