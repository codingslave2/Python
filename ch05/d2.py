# 2차원 리스트 - 3행 2열(for 형태로 인식)
a = [
    [10, 20],
    [30, 40],
    [50, 60]
]

#출력
print(a[0][0]) #10
print(a[0][1]) #20
print(a[1][0]) #30
print(a[1][1]) #40

# 2차원 리스트에서 요소 추가
a.append([70, 80])

# 전체 출력
for x, y in a:
    print(x, y)

#b = [1, 2, 3, 4]
#len(b) #4

print("2차원 리스트 크기(행)", len(a))
print("2차원 리스트 크기(열)", len(a[0]))
print("2차원 리스트 크기(열)", len(a[1]))

# for ~ range()
for i in range(0, len(a)): # len(a)=3, 3-1=2
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')


# 리스트의 연산(합계)
total = 0
count = 8 #2차원 이상은 개수를 직접 카운트 해야함
for i in range(0, len(a)): # len(a)=3, 3-1=2
    for j in range(0, len(a[i])):
        total += a[i][j]
        print()

# i=0 j=0 0+10, total = 10
#     j=1 10+20, total = 30

# 평균 구하기

avg = total / len(a)

print(f'합계 : {total}')
print(f'개수 : {count}')
print(f'평균 : {avg}')


