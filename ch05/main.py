# 객체 리스트
# Customer - 2명, GoldCustomer - 2명, VIP - 1명

from customer import Customer
from goldcustomer import GoldCustomer
from vipcustomer import VIPCustomer

customer = [
    Customer(101, "놀부"),
    Customer(102, "팥쥐"),
    GoldCustomer(103, "흥부"),
    GoldCustomer(104, "콩쥐"),
    VIPCustomer(105, "심청", 1004)
]

print("******* 구매 가격과 보너스 포인트 계산 *******")

for cus in customer:
    price = 10000
    cost = cus.calc_price(price)
    print(f'{cus.getname()}"님의 지불 금액은 : {cost}"원 입니다."')

print("******* 고객 정보 출력 *******")

# 전체 출력

for cus in customer:
    print(cus)