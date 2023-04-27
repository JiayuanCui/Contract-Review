import os 

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

from script import extract_segement

ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                save_location = os.path.join('input', filename)
                file.save(save_location)

                output = extract_segement(save_location)
                df = output.to_html(classes="table")
                return redirect(url_for('processed', df=df))

        return render_template('upload.html')
    
    @app.route('/processed')
    def processed():
        df = request.args.get('df')
        return render_template('processed.html', df=df)

    
    return app

