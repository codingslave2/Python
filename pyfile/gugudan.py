# 구구단 쓰기
# with - as 구문에서는 f.close()를 사용하지 않음

try:
    with open("c:/coding/pyfile/output/gugu.txt", 'w') as f:
        for i in range(2, 10):
            for j in range(1, 10):
                gugu = f'{i} x {j} = {i*j}\n'
                f.write(gugu)
            f.write('\n')

except FileExistsError:
    print("파일을 찾을 수 없습니다.")