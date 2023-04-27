# 입력 받아 파일 쓰기


with open ('./py/ch06/output/input.txt', 'a') as f:
    while True:
        text = input("저장할 내용을 입력해주세요(종료 - z) : ")
        if text == 'z':
            break
        f.write(text)
        f.write('\n')