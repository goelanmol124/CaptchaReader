import pytesseract
from PIL import Image
import cv2
import numpy as np

image = Image.open(r'.\dominant_color.jpg').convert('L')
ret,img = cv2.threshold(np.array(image), 125, 255, cv2.THRESH_BINARY)
image = Image.fromarray(img.astype(np.uint8))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#print('hi')
print(pytesseract.image_to_string(image, config='--psm 7'))