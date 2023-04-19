#체질량 지수 = 모무게 / 키의 제곱
# 키 - 키 / 100
# 거듭제곱 2 ** 3 = 2 x 2 x 2

# height = 173 / 100 # cm로 변환
# weight = 65



# print(f'{bmi:.2f}')


name = input("이름을 입력하세요.")
height = float(input("키(cm)를 입력하세요"))
height = height / 100
weight = float(input("몸무게(kg)를 입력하세요"))

bmi = weight / (height ** 2)

# % 포멧 방식 : %s - 문자, %f - 실수, %d - 정수

print(f'{name}님의 bmi는 {bmi:2f} 입니다.') # f-string 방식
print("%s님의 bmi는 %.2f 입니다." % (name, bmi)) #string 방식

if bmi < 20:
    print("저체중입니다.")
elif bmi >= 20 and bmi < 24:
    print("정상입니다.")
elif bmi >= 24 and bmi < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")
