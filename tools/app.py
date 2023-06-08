import qrcode
from flask import Flask, render_template, request, redirect, url_for, send_file
from tools import qr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qrcode', methods=['GET', 'POST'])
def qrcode_generator():
    if request.method == 'POST':
        text = request.form['text']
        filename = qr.generate_qr_code(text)
        return redirect(url_for('download', filename=filename))
    return render_template('qrcode.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
