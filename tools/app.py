import os
from flask import Flask, render_template, request, url_for
from tools import Tools

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def qrcode_generator():
    if request.method == 'POST':
        text = request.form['website_name']
        path = Tools.generate_qr_code(text)
        qrcode_path = url_for('tmp', filename=path)
        return render_template('index.html', qrcode=path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
