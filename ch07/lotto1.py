# 로또 복권 추첨 프로그램
# 1 ~ 45까지 6개 랜덤수로 저장

import random

# 빈 리스트 생성
lotto = []

# 처리
while len(lotto) < 6: # lotto의 개수가 6개일 때 빠져나옴
    num = random.randint(1, 45)
    if num not in lotto: # 중복 제거
        lotto.append(num)



# 출력
lotto.sort() # 오름차순 정렬
print(lotto)



# 1부터 45까지의 숫자 중 6개를 랜덤하게 추출하여 리스트에 저장
lotto = random.sample(range(1, 46), 6)

# 결과 출력
lotto.sort(reverse=True) #내림차순 정렬
print(lotto)
