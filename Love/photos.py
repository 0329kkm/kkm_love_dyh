from PIL import Image
import os

# Set the directory containing the jpg files
jpg_dir = "images"

# Set the directory where you want to save the png files
png_dir = "img"

# Loop through each file in the jpg directory
for filename in os.listdir(jpg_dir):
    # Check if the file is a jpg file
    if filename.endswith(".jpg"):
        # Open the image using Pillow
        with Image.open(os.path.join(jpg_dir, filename)) as im:
            # Convert the image to png format
            png_filename = os.path.splitext(filename)[0] + ".png"
            # Save the image to the png directory
            im.save(os.path.join(png_dir, png_filename), "png")

# Set the directory containing the images you want to resize
directory = "img"

# Set the new size you want the images to be
new_size_big = (400, 400)
new_size_small = (100, 100)
# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    # if filename.endswith(".jpg") or filename.endswith(".png"):
    if filename.startswith("0"):
        # Open the image
        image = Image.open(os.path.join(directory, filename))
        # Resize the image
        resized_image = image.resize(new_size_small)
        # Save the resized image with the same filename
        resized_image.save(os.path.join(directory, filename))
    else:
        # Open the image
        image = Image.open(os.path.join(directory, filename))
        # Resize the image
        resized_image = image.resize(new_size_big)
        # Save the resized image with the same filename
        resized_image.save(os.path.join(directory, filename))

