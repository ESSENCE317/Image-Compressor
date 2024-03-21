import PIL
from PIL import Image
from tkinter.filedialog import *

# Prompt user to select an image file

# Open a file dialog to select an image file and store its path in 'file_path'
file_path = askopenfilename()

# Open the image file specified by 'file_path' and store it in 'img'
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

# Resize the image using anti-aliasing for better quality
img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)

# Prompt user to specify a save location and filename for the compressed image
save_path = asksaveasfilename()

# Save the resized image in JPEG format
img.save(save_path + "compressed.jpg")
