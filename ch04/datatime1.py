# 날짜 및 시간 모듈 포함하기
import datetime

now = datetime.datetime.today()
print(now)
print(now.strftime("%Y.%m.%d. %H:%M:%S"))

# 날짜 - 년, 월, 일
print(f'{now.year}년')
print(f'{now.month}월')
print(f'{now.day}일')

# 시간 - 시, 분, 초
print(f'{now.hour}시')
print(f'{now.minute}분')
print(f'{now.second}초')

# 오늘의 날짜
today = datetime.date.today()
print(today)

# 특정한 날짜
the_day = datetime.date(2022, 12, 12)
print(the_day)

# 나이가 100세 되는 해의 연도 계산하기
# 현재년도 + (100 - age)

import datetime
import calendar as cal

cal.prcal(2023) # 2023년 달력
cal.prmonth(2023, 4) # 2023년 4월 달력

age = int(input("나이 입력 : "))
now = datetime.date.today()
print(now.year)
result = now.year + (100 - age)
print(f'100세가 되는 해는 {result}년 입니다.')