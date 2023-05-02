# 컨트롤 도구 - 클래스 사용 생성

from tkinter import *

root = Tk()
root.title("UI 구성")
root.geometry("200x50")
frame = Frame(root)
frame.pack() # 가운데 정렬



# Button(root, text='제품').grid(row=0, columnspan=2)
Label(frame, text="").grid(row=0, column=0)
Button(frame, text='제품').grid(row=1, column=0)
lbl = Label(frame, text="안녕하세요.")
lbl.grid(row=2, column=0)

root.mainloop()