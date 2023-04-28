# Customer 클래스 생성
# 맴버 변수 - 고객아이디, 이름, 등급, 보너스 포인트, 보너스 적립율

class Customer:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname
        self.cgrade = "SILVER"
        self.bonus_point = 0
        self.bonus_ratio = 0.01 # 1%

    def getname(self): # 이름을 가져오는 함수
        return self.cname

    def __str__(self):
        return f'{self.cname}님의 등급은 {self.cgrade}이고, ' \
               f'보너스 포인트는 {self.bonus_point}점 입니다.'
    
    def calc_price(self, price):
        # self.bonus_point = price * self.bonus_ratio
        # 보너스 포인트 += 보너스 포인트
        # 할인된 가격 = 원래 가격 - (원래 가격 * 구매할인율)
        price -= int(price * self.bonus_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price


if __name__=="__main__":
    c1 = Customer(1001, "정국")
    price = 10000
    # print(c1.calc_price(price)) # 맴버 변수에 직접 접근하지 않음
    print(f'{c1.cname}님의 구매 비용은 {c1.calc_price(price)}원 입니다.')
    print(c1)

    c2 = Customer(1002, "슈가")
    print(c2)