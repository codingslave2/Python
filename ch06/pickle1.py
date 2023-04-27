#pickle 모듈 사용

import pickle

with open ('./py/ch06/output/object.txt', 'wb') as f:
    a = ['강아지', '고양이', '말']
    dic = {1:'강아지', 2:'고양이', 3:'말'}
    pickle.dump(a, f) #쓰기
    pickle.dump(dic, f)

with open ('./py/ch06/output/object.txt', 'rb') as f:
    a = pickle.load(f)
    dic = pickle.load(f)
    print(a)
    print(dic)