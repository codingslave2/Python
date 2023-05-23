# 이미지 처리 - Pillow
from PIL import Image
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = Image.open("c:/coding/py/pyocr/source/cap.png")
# img.show()

text = pytesseract.image_to_string(img, lang="kor+eng")
# print(text)
print(text.replace(" ", "")) # 공백제거

# 변환된 텍스트를 파일에 쓰기
# encoding='utf-8' 꼭 명시해야함

with open("c:/coding/py/pyocr/source/cap.png", 'w', encoding='utf-8') as f:
    f.write(text)
    f.write(text.replace(" ", ""))

