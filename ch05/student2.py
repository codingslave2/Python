# Student
# 클래스 생성 함수 - def __init__()

class Student:
    #생성자 함수(맴버 함수)
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def info(self):
        return f'이름 : {self.name}, {self.grade}'

    def learn(self):
        print("수업을 듣습니다.")

# 메인 영역
if __name__== "__main__":
    s1 = Student('김하나', 1)
    print(s1)
    s1.learn()

    s2 = Student('김현우', 3)
    print(s2)
    s2.learn()