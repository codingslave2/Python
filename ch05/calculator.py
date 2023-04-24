# Calculator 클래스

class Calculator:
    def __init__(self):
        self.x = 0

# 매개변수 y값을 더하기
    def add(self, y):
        self.x = self.x + y
        return self.x
    
# 매개변수 z값 빼기
    def sub(self, z):
        self.x = self.x - z
        return self.x

cal1 = Calculator()
print(cal1.add[10])
print(cal1.sub[4])

cal2 = Calculator()
print(cal2.add(10.1))
print(cal2.sub(2.5))