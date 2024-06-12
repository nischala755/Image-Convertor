import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format)
        print(f"Image converted to {output_format} and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_input_file():
    input_file = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_file)

def select_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension="." + output_format.get().lower())
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_file)

def start_conversion():
    input_file = input_entry.get()
    output_file = output_entry.get()
    format = output_format.get()
    convert_image(input_file, output_file, format)

app = tk.Tk()
app.title("Image Converter")

tk.Label(app, text="Input File:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(app, width=40)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(app, width=40)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

tk.Label(app, text="Output Format:").grid(row=2, column=0, padx=10, pady=10)
output_format = tk.StringVar(value="PNG")
tk.OptionMenu(app, output_format, "PNG", "JPEG", "BMP", "GIF").grid(row=2, column=1, padx=10, pady=10)

tk.Button(app, text="Convert", command=start_conversion).grid(row=3, column=1, padx=10, pady=10)

app.mainloop()
