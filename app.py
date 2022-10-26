from flask import Flask
from sport import sport
from main import main
from news import news
from img_upl import img_upl


UPLOAD_FOLDER = 'UPLOAD_FOLDER'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.register_blueprint(sport)
app.register_blueprint(main)
app.register_blueprint(news)
app.register_blueprint(img_upl)


if __name__ == '__main__':
    app.run(debug=True)
