import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"
resize_to = (800, 600)
output_format = "JPEG"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        input_path = os.path.join(input_folder, filename)
        with Image.open(input_path) as img:
            resized_img = img.resize(resize_to)
            output_filename = os.path.splitext(filename)[0] + "." + output_format.lower()
            output_path = os.path.join(output_folder, output_filename)
            resized_img.save(output_path, output_format)
            print(f"Resized and saved: {output_path}")

print("All images have been resized and converted successfully!")
