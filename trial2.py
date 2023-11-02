from PIL import Image, ImageFilter
import os

path = '/home/norbudendup'  # Update to the correct directory path containing image files
pathOut = 'editedImgs'

# Create the output directory if it doesn't exist
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Check if the path is a directory
if os.path.isdir(path):
    for filename in os.listdir(path):
        # Check if the file is an image (e.g., by checking the file extension)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            img = Image.open(os.path.join(path, filename))

            edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

            clean_name = os.path.splitext(filename)[0]

            edit.save(os.path.join(pathOut, f"{clean_name}_edited.jpg"))
else:
    print(f"The specified path '{path}' is not a directory.")
