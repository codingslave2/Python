# 이미지 파일 읽고 쓰기
# open(파일경로, 'rb')

with open("./py/ch06/images/coffee-blue.jpg", "rb") as f1:
    img = f1.read()

# 쓰기
with open("./py/ch06/images/coffee-blue.jpg", "wb") as f2:
    f2.write(img)