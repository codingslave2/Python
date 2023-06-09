# 온도 변환기

from tkinter import *
from classification.extend.converters import Converter

root = Tk()
root.title("온도 변환기")
root.geometry("240x80+100+100")

Label(root, text=' degree C ').grid(row=0, column=0)
ent_c = Entry(root, width=15) # 입력 - 섭씨온도
ent_c.grid(row=0, column=1)

Label(root, text=' degree F ').grid(row=1, column=0)
txt_f = Text(root, width=15, height=1)
txt_f.grid(row=1, column=1) # 출력 - 화씨 온도

Button(root, text="변환", width=10, command=convert).grid(row=2, columnspan=2)


root.mainloop()