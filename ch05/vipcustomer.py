# VIPCustomer 클래스 - Customer를 상속 받음

from customer import Customer

class VIPCustomer(Customer):
    def __init__(self, cid, cname, agent):
        super().__init__(cid, cname)
        self.agent = agent
        self.grade = "VIP"
        self.sale_ratio = 0.1 # 10%
        self.bonus_ratio = 0.05 # 5%

    def __str__(self):
        return f' {super().__str__()} 전문 상담원 ID는 {self.agent}입니다.'
    
vip = VIPCustomer(1004, '진', 777)
price = 30000
cost = vip.calc_price(price)
print(vip)