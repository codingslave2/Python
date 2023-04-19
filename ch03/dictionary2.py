#딕셔너리
d = {'Tomas': 13, 'Jane': 9}

#요소 추가 - Mike 10살
d['Mike'] = 10
print(d)

#모든 키 가져오기
print(d.keys())
print(list(d.keys())) # 리스트 자료로 가져오기

#모든 값(value) 가져오기
print(d.values())
print(list(d.values())) # 리스트 자료로 가져오기

#모든 키와 값 가져오기
for key, val in d.items():
    print(key, ':', val)