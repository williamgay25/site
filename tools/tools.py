import qrcode
import os
import cv2
import numpy as np
import os
import zipfile
import tempfile
from PIL import Image

class Tools:
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
    
def reduce_image_quality(image_path, quality=90):
    image = Image.open(image_path)
    image.save(image_path, quality=quality)

def compress_epub(input_file_path, output_file_path):
    if os.path.getsize(input_file_path) <= 25*1024*1024: # if file is already less than or equal to 25MB
        print("The file is already less than or equal to 25MB.")
        return

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Extract the epub file
        with zipfile.ZipFile(input_file_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)

        # Walk through the extracted files and reduce the quality of images
        for subdir, dirs, files in os.walk(tmpdir):
            for file in files:
                filepath = subdir + os.sep + file

                if filepath.endswith(".jpg") or filepath.endswith(".jpeg") or filepath.endswith(".png"):
                    reduce_image_quality(filepath)

        # Create the new epub file
        with zipfile.ZipFile(output_file_path, 'w') as epub:
            for subdir, dirs, files in os.walk(tmpdir):
                for file in files:
                    epub.write(os.path.join(subdir, file), arcname=os.path.relpath(os.path.join(subdir, file), tmpdir))

    if os.path.getsize(output_file_path) > 25*1024*1024: # if compressed file is still more than 25MB
        print("The compressed file is still more than 25MB.")
    else:
        print(f"Compression successful. The compressed file is located at: {output_file_path}")

# example usage
compress_epub("Liftoff.epub", "output.epub")

def remove_background(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Create a mask to specify the areas to be marked as background or foreground
    mask = np.zeros(image.shape[:2], np.uint8)

    # Define background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define the rectangle that contains the foreground object
    rectangle = (10, 10, image.shape[1]-10, image.shape[0]-10)

    # Apply the GrabCut algorithm to segment the foreground object
    cv2.grabCut(image, mask, rectangle, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask where 0 and 2 indicate background, while 1 and 3 indicate foreground
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)

    # Apply the mask to the original image
    result = image * mask[:, :, np.newaxis]

    # Set the background to white
    result[np.where((result == [0, 0, 0]).all(axis=2))] = [255, 255, 255]

    return result

""" # Path to the image file
image_path = "test.JPEG"

# Call the function to remove the background
result_image = remove_background(image_path)

# Display the original image and the result
cv2.imshow("Original Image", cv2.imread(image_path))
cv2.imshow("Result", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the resulting image as "final.jpg"
cv2.imwrite("final.jpg", result_image)
print("Result saved as final.jpg") """

