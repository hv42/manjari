import pytesseract
import PIL
from PIL import Image
import os
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

src = os.path.join('C:\\Users\\harithavhs\\Documents\\github\\indic\\quote.jpeg')
img = Image.open('C:\\Users\\harithavhs\\Documents\\github\\indic\\quote.jpeg')
print(img)
result = pytesseract.image_to_string(img)
print(result.strip().split('\n'))