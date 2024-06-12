import argparse
from PIL import Image
import os


def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format)
        print(f"Image converted to {output_format} and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images between different formats.")
    parser.add_argument('input_file', type=str, help="Input file path")
    parser.add_argument('output_file', type=str, help="Output file path")
    parser.add_argument('output_format', type=str, choices=['PNG', 'JPEG', 'BMP', 'GIF'], help="Desired output format")

    args = parser.parse_args()

    convert_image(args.input_file, args.output_file, args.output_format)
