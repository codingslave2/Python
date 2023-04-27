# SuperSonicAirplane 클래스 생성

from airplane import Airplane

class SuperSonicAirplane(Airplane):
    # 1번 - normal, 2번 - SuperSonic
    normal = 1 # 상수 설정
    SuperSonic = 2

    # 모드 - 맴버 변수

    def __init__(self):
        self.fly_mode = SuperSonicAirplane.normal

    def fly(self):
        if self.fly_mode == SuperSonicAirplane.SuperSonic:
            print("초음속으로 비행합니다.")
        else:
            super().fly()

sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SuperSonic # 모드 변경
sa.fly()
sa.land()