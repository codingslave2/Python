# GUI(Graphic User Interface) 프로그램 만들기
# CUI(Character User Interface) - 명령 프롬포드, console

#import tkinter 모듈 tkinter.py
from tkinter import *

root = Tk()
root.title("처음 만드는 윈도우")
root.geometry("300x200+300+100") # 가로 300 세로 200 x 좌표 300 y 좌표 100

# 버튼 생성
# grid(), pack()
# Button(root, text='버튼', font='맑은고딕, 18').pack() # pack() - 가운데 위치
btn = Button(root, text='버튼', font=("맑은고딕", 18))
btn.pack()
# btn.grid(row=0, column=0)

root.mainloop()