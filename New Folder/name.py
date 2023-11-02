from PIL import Image, ImageFilter
import os

path = '/.jpg'
pathOut = 'editedImgs'  # Remove the leading forward slash

# Create the output directory if it doesn't exist
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))  # Use os.path.join to join paths

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    clean_name = os.path.splitext(filename)[0]

    edit.save(os.path.join(pathOut, f"{clean_name}_edited.jpg"))