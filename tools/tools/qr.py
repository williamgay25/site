import qrcode
import os

def generate_qr_code(text):
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
    save_path = os.path.join('/tmp', filename)
    image.save(save_path)
    return save_path