import os
from PIL import Image


def batch_convert_images(input_dir, output_dir, output_format):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.' + output_format.lower())
            convert_image(input_path, output_path, output_format)


def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format)
        print(f"Image converted to {output_format} and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_dir = 'images/input'  # Change to your input directory
    output_dir = 'images/output'  # Change to your output directory
    output_format = 'PNG'  # Desired output format

    batch_convert_images(input_dir, output_dir, output_format)
