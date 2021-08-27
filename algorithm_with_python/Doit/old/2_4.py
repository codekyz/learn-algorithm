# 2_3.py 모듈에 정의된 max_of()함수를 import하여 사용

from max import max_of

print('배열의 최대값 구하기')
print('***"end"를 입력하면 종료')

number = 0
x = []

while True:
    s = input(f'x[{number}]값을 입력하세요: ')
    if s =='end':
        break
    x.append(int(s))
    number += 1

print(f'{number}개를 입력')
print(f'최대값은 {max_of(x)} 입니다')