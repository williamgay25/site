import qrcode
from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qrcode', methods=['GET', 'POST'])
def qrcode_generator():
    if request.method == 'POST':
        text = request.form['text']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white")
        filename = 'qrcode.png'
        image.save(filename)
        return redirect(url_for('download', filename=filename))
    return render_template('qrcode.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
