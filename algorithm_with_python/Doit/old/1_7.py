# 가로, 세로 길이가 정수 이고 넒이가 area인 직사각형의 변의 길이 나열하기
# 약수 구하기

area = int(input('넓이 : '))

for i in range(1, area+1):
    if i * i > area: break # i가 가장 긴 변의 길이가 되고 사각형의 최대 넓이를 초과하므로 강제 종료
    if area % i: continue # 넓이가 i로 나누어 떨어지지 않으면(나머지가 있으면) 출력하지 않고 건너뜀
    print(i,' X ',area // i)


# 10~99 사이의 난수 n개 생성하되 20이 나오면 중단
# else문이 뒤따르는 for문 구현

import random

n = int(input())

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 20:
        print('강제중단')
        break

else:
    print('정상종료')