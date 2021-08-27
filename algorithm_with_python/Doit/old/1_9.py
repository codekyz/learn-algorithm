# 다중루프
# 구구단 곱셈표

print('-' * 27)

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end='') # 출력 자릿수를 :3으로 지정
    print() # 줄바꿈, 행변경

print('-' * 27)
