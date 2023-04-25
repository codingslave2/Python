
class City:
    a = ['Seoul', 'Incheon', 'Daejon', 'Jeju'] #클래스 리스트

    # def __init__(self, name):
    #     self.name = name
    #     self.a2 = []

str1 = ""
for i in City.a: # 클래스 이름으로 직접 접근
    str1 += i[0]

print(str1)