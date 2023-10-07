import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Function to upload an image


def upload_image():
    # Open a file dialog and return the selected file path
    file_path = filedialog.askopenfilename()
    return file_path

# Function to upload a watermark


def upload_watermark():
    # Open a file dialog and return the selected file path
    watermark_path = filedialog.askopenfilename()
    return watermark_path

# Function to apply a watermark to an image


def apply_watermark(image_path, watermark_path):
    # Open the image and the watermark
    image = Image.open(image_path)
    watermark = Image.open(watermark_path)
    # Paste the watermark onto the image
    image.paste(watermark, (0, 0), watermark)
    # Display the image
    image.show()


# Create a tkinter window
root = tk.Tk()
root.title("Watermark Application")
root.geometry("300x200")
root.configure(bg="lightgrey")

# Create a button to upload an image
upload_image_button = tk.Button(
    root, text="Upload Image", command=upload_image, highlightthickness=0,
    highlightbackground="lightgrey", bg="blue", fg="blue")
upload_image_button.pack(pady=10)

# Create a button to upload a watermark
upload_watermark_button = tk.Button(
    root, text="Upload Watermark", command=upload_watermark, highlightthickness=0,
    highlightbackground="lightgrey", bg="blue", fg="blue")
upload_watermark_button.pack(pady=10)

# Create a button to apply the watermark to the image
apply_watermark_button = tk.Button(
    root, text="Apply Watermark",
    command=lambda: apply_watermark(upload_image(), upload_watermark()), highlightthickness=0,
    highlightbackground="lightgrey", bg="blue", fg="blue")
apply_watermark_button.pack(pady=10)

# Start the tkinter main loop
root.mainloop()
