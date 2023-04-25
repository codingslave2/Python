# ScaleConverter 상속받는 클래스
# 화씨온도(F) = 섭씨온도(C) X 1.8 + 32
# 패키지이름.모듈이름
# import scale_converter
from scale_converter import ScaleConverter

# if __name__=="__main__":
# con = ScaleConverter("KB", "B", 1024)
# print("Converting 1 KB")
# print(str(con.convert(1)) + con.units_to)

class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor) # 부모 맴버 상속받음
        self.offset = offset
    
    def convert(self, value):
        return self.factor * value + self.offset
        

conv = Converter('C', 'F', 1.8, 32)
print("Converting 20C")
print(f'{conv.convert(20)}{conv.units_to}')