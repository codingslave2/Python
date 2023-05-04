# 주식 종목 가져오기 - 네이버 금융 > 증권 > 증권홈 > 우측 하단(인기 종목 검색)

import requests
from bs4 import BeautifulSoup

def getcontent():
    url = 'https://finance.naver.com/item/main.naver?code=086520#'
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

def getprice(item_code):
    content = getcontent() # 호출
    today = content.find('div', attrs={'class':'today'})
    if today is None:
        return None
    price = today.find('span', attrs={'class':'blind'})
    return price.text

에코프로 = getprice('086520')
삼성전자 = getprice('005930')
네이버 = getprice('035420')


if 에코프로 is None:
    print('가격 정보를 가져올 수 없습니다.')
else:
    print(f'에코프로 주가: {에코프로}원')

if 삼성전자 is None:
    print('가격 정보를 가져올 수 없습니다.')
else:
    print(f'삼성전자 주가: {삼성전자}원')

if 네이버 is None:
    print('가격 정보를 가져올 수 없습니다.')
else:
    print(f'네이버 주가: {네이버}원')

