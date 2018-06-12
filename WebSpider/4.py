import tesserocr
from PIL import Image
image = Image.open('image.png')
print(tesserocr.file_to_text(image))
