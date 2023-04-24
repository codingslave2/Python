import student2
# 파일이름, 클래스 이름
# import 모듈 이름
st1 = student2.Student('이셋', 3)
st1.info()

# from 모듈 이름 import 클래스 이름
from student2 import Student
st1 = Student('이셋', 3)
st1.info()


# 객체 리스트 생성
student = [
    Student("김하나", 1),
    Student("박둘", 2),
    Student("이셋", 3)
]

# 특정한 수 조회
student[0].info()
student[1].info()

# 전체 조회
for i in student:
    i.info()