from flask import render_template, Blueprint


sport = Blueprint('sport', __name__, url_prefix='/sport',
                  template_folder='templates')
# sport - blueprint


@sport.route('/sportmain')
def sport_end_p():
    return render_template('sport.html')


# sport /swim
@sport.route('/swim')
def swim():
    return render_template('swim.html')

# sport/football


@sport.route('/football')
def fotball():
    return render_template('football.html')
