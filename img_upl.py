from flask import render_template, Blueprint
from flask import send_from_directory
# import fro upload
import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'UPLOAD_FOLDER'

img_upl = Blueprint('upl', __name__, url_prefix='/upl',
                    template_folder='templates')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@img_upl.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)


@img_upl.route('/img', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            print(os.path.join(UPLOAD_FOLDER, filename))
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # return redirect(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upl.download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# @sport.route('/sportmain')
# def sport_end_p():
#     return render_template('sport.html')
