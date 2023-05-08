from calculator1 import Calculator

# 거듭제곱 계산이 추가된 계산기
class MoreCalculator(Calculator):
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num = num * self.x
        return num


    #     return self.x ** self.y
    
    # def div(self):
    #     if self.y == 0:
    #         return 0
    #     else:
    #         return self.x / self.y
        
cal = MoreCalculator(2, 4)
print(f"덧셈 : {cal.add()}")
print(f"뺄셈 : {cal.sub()}")
print(f"곱셈 : {cal.mul()}")
print(f"나누기 : {cal.div()}")
print(f"제곱 : {cal.pow()}")


cal2 = MoreCalculator(5, 2)
print(f"덧셈 : {cal2.add()}")
print(f"뺄셈 : {cal2.sub()}")
print(f"곱셈 : {cal2.mul()}")
print(f"나누기 : {cal2.div()}")
print(f"제곱 : {cal2.pow()}")
