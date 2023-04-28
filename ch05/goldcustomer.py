# goldcustomer 클래스 생성 - Customer 상속
# 맴버 변수 - 고객아이디, 이름, 고객등급, 구매할인율, 보너스

from customer import Customer

class GoldCustomer(Customer):

    def __init__(self, cid, cname):
        super().__init__(cid, cname)
        self.cgrade = "GOLD"
        self.sale_tario = 0.1 # 10%
        self.bonus_point = 0
        self.bonus_ratio = 0.02 #2%

    def calc_price(self, price):
        # price = price * sale_ratio (가격 - 가격 x 구매할인율)
        price = int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)

g1 = GoldCustomer(1001, "뷔")
price = 10000
print(g1)