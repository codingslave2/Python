# 이미지 처리 - Pillow
from PIL import Image
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r"C:\coding\py\pyocr\tesseract.exe"
img = Image.open("c:/coding/py/pyocr/source/cap.png")
# img.show()

text = pytesseract.image_to_string(img, lang="kor")
print(text)
