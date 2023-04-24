# 객체 지정 언어 - 모든 사물을 객체화(Object)
# 객체화를 위해 코드로 정의한 것 - 클래스

class Student:
    name = "" # 자료형이 문자
    grade = 0 # 자료형이 숫자

    def infor(self): # 저절로 self가 붙여짐
        print(self.name, self.grade)

std1 = Student() # 객체 생성(인스턴스)
std1.name = '김하나'
std1.grade = 1
print(std1.name, std1.grade)

std2 = Student()
std2.name = '박둘'
std2.grade = 2
print(std2.name, std2.grade)