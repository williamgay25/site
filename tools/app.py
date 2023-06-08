from flask import Flask, render_template, request, redirect, url_for, send_file
from tools import qr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def qrcode_generator():
    if request.method == 'POST':
        print("hello")
        text = request.form['website_name']
        qr.generate_qr_code(text)
        qrcode_url = url_for('static', filename='qrcode.png')
        return render_template('index.html', qrcode=qrcode_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()