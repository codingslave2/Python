class Employee:
    serial_num = 1000 # 사번 기준값(클래스 변수)

    def __init__(self, name):
        # 기준값을 1 증가 한 후 id에 저장함
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):
        return " 사번 : {}, 이름 : {}".format(self.id, self.name)

emp1 = Employee("회사원")
print(emp1.id)

emp2 = Employee("유사원")
print(emp2.id)

emp3 = Employee("이사원")
print(emp3.id)


# 객채 리스트
employee = [
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달')
]

for emp in employee:
    print(emp)