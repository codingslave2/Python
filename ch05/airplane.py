# Airplane 클래스
# 클래스의 구성 요소 - 생성자 함수, 맴버 변수, 맴버 함수

class Airplane:
    #기본생성자 - 인터프레터가 생성해줌
    def __init__(self):
        pass
    
    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")


# 객체 생성 방식
air = Airplane()
air.take_off()