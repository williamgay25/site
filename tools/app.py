import os
from flask import Flask, render_template, request, send_file
from tools import Tools

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def qrcode_generator():
    if request.method == 'POST':
        text = request.form['website_name']
        path = Tools.generate_qr_code(text)
        qrcode_path = os.path.join('tmp', path)
        return render_template('index.html', qrcode=qrcode_path)
    return render_template('index.html')

@app.route('/tmp/<path:filename>')
def serve_qrcode(filename):
    return send_file(os.path.join('tmp', filename), mimetype='image/png')

if __name__ == '__main__':
    app.run()
