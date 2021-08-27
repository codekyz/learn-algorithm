# *를 n개 출력하되 w개 마다 줄바꿈

n, w = map(int, input().split())

# for i in range(n):
#     print('*', end="")
#     if i % w == w - 1:
#         print()

# if n % w:
#     print()

# for loop가 실행되는 동안 계속해서 if문의 조건을 확인 함 효율구데기

# 개선 : n을 w로 나눈 만큼 반복, *은 W만큼 반복, n % W 의 나머지만큼 *을 반복

for _ in range(n // w):
    print('*' * w) # w만큼 반복

rem = n % w
if rem: # 나머지 값이 있으면
    print('*' * rem)
