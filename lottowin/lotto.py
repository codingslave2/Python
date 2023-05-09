import requests
from bs4 import BeautifulSoup
from tkinter import *  # 대문자로 변경

def lotto_win():
#     num = 1062
    num = entry.get() # 입력상자에 입력된 값
    url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(num)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    win_result = soup.select_one('div.win_result') 
    win_list = win_result.text.split('\n')[7:13]
    bonus_num = win_result.text.split('\n')[-4]
    
    # 출력 상자에 번호 출력
    output.delete(1.0, END) #첫행 첫문자 위치에서 시작
    output.insert(END, f'당첨번호 : {win_list}\n\n보너스번호 : {bonus_num}')

#     print('당첨번호')
#     print(win_list)     
#     print('보너스번호')
#     print(bonus_num)

# lotto_win()

window = Tk()
window.title("로또 당첨 번호 확인")

Label(window, text="당첨 회차 입력: ").grid(row=0, column=0)
# 입력 상자
entry = Entry(window, bg='yellowgreen')
entry.grid(row=1, column=0)
btn = Button(window, text="당첨 번호 확인", command=lotto_win, bg='pink')
btn.grid(row=2, column=0, sticky=W)



# 출력 상자
output = Text(window, bg='skyblue', width=50, height=6)
output.grid(row=3, column=0, sticky=W)



window.mainloop()
