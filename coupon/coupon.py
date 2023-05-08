# 쿠폰 추첨기 만들기
from tkinter import *
import random

namelist = ['이진성', '노승우', '박성호', '권지혜', '김은효', 
            '이경철', '성의석', '이유진', '유성길', '한주훈',
            '강정현', '김현우', '이영준', '안재훈', '김민정',
            '유세현', '윤기은', '오화룡', '조은별', '이가은']

# 5명 랜덤 추출
def click():    
    winners = []
    while len(winners) < 5:
        name = random.choice(namelist)
        if name not in winners:
            winners.append(name) # 중복 요소 제거

    # 결과 출력
    output.delete('1.0', END)  # 이전 결과 삭제
    # for i, name in enumerate(winners):
    #     output.insert(END, f"{name}\n")
    output.insert(END, winners)

        
    

window = Tk()
window.title("쿠폰추첨기")
window.option_add('*font', '맑은고딕 14')

# 이미지 삽입 - PhotoImage(file)

img = PhotoImage(file = 'C:/coding/py/coupon/bronx.png')

lbl_img = Label(window)
lbl_img.config(image=img)
lbl_img.grid(row=0, column=0, sticky=W)

#추첨 버튼
Button(window, text='추첨', command=click).grid(row=1, column=0)

# 이름 출력
output = Text(window, width=33, height=5, bg='yellow')
output.grid(row=2, column=0, sticky=E)

window.mainloop()