#사각형의 넓이 계산 함수
#함수이름 = calc_area(), tri_area()

def calc_area(weight, height):
    area = weight * height
    return area    

# 가로 - 4cm, 세로 = 3cm
result = calc_area(4, 3)
print('사각형의 면적', calc_area(4, 3)) # 12
print(f'사각형의 면적 : {result}')


#삼각형의 넓이 계산 함수

def tri_area(base, height):
    area = 0.5 * base * height
    return area

result2 = tri_area(5, 3)
print('삼각형의 면적', tri_area(5, 3))
print(f'삼각형의 면적 : {result2}')

#정사각형의 면적
# size = int(input("숫자를 입력하세요 : "))
# area = size * size
# print(area)

def calc_size(n):
    area = n * n
    return area

print(calc_size(100))