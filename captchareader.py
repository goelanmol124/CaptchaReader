from PIL import Image
#import pytesseract
from transformers import TrOCRProcessor, VisionEncoderDecoderModel, AutoTokenizer, AutoModelForCausalLM
import requests
import time
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
model_id = "ayoubkirouane/moondream2-image-captcha"
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)#.to(device)
tokenizer = AutoTokenizer.from_pretrained(model_id , trust_remote_code=True)


start = time.time()
image = Image.open(r'.\dominant_color.jpg')

enc_image = model.encode_image(image)#.to(device)
print(model.answer_question(enc_image, "What does captcha read?", tokenizer))
print(time.time() - start)