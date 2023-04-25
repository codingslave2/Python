# 영어 단어장 만들기

import random

try:
    word = ['ant', 'bear', 'chicken', 'deer', 'fox', 'elephant', 'horse', 'lion', 'monkey', 'penguin']

    with open("c:/coding/pyfile/output/word.txt", 'w') as f:
        # 파일 쓰기
        for i in word:
            if i == word[-1]:
                f.write(i)
            else:
                f.write(i + ' ')

except FileNotFoundError:
    print("파일을 쓸 수 없습니다.")

# 파일 읽기
try:
    with open("c:/coding/pyfile/output/word.txt", 'r') as f:
        data = f.read().split() #공백 문자로 구분 - 리스트로 변환
        word = random.choice(data) # 단어 1개 랜덤 추출
        print(word)


except:
    print("파일을 읽을 수 없습니다.")
