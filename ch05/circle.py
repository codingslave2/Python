# 원 그리기
import turtle as t
t.shape('turtle')
t.bgcolor('darkblue')
t.color('white')
t.speed(5) # 1~10의 숫자 선택 0이 가장 빠름

for i in range(20):
    t.circle(50)
    t.left(100)


t.mainloop()