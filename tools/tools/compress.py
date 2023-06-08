import os
import zipfile
import tempfile
import shutil
from PIL import Image

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

