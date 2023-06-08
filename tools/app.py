import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from tools import qr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def qrcode_generator():
    if request.method == 'POST':
        text = request.form['website_name']
        filename = qr.generate_qr_code(text)
        qrcode_url = url_for('serve_qrcode', filename=filename)
        return render_template('index.html', qrcode=qrcode_url)
    return render_template('index.html')

@app.route('/qrcode/<path:filename>')
def serve_qrcode(filename):
    tmp_folder = 'tmp' 
    return send_file(os.path.join(tmp_folder, filename), mimetype='image/png')

if __name__ == '__main__':
    app.run()