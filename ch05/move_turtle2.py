# turtle 모듈
import turtle as t

t.shape('turtle')
t.bgcolor('purple')

n = 4 # 변의 개수
d = 100 #길이 (크기)
# 각도 = 360 | 변의 개수

for i in range(n):
    t.forward(d)
    t.right(360/n)

n = 6
for i in range(n):
    t.forward(d)
    t.right(360 / n)





t.mainloop()