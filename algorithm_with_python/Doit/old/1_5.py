# 짝수 + 홀수 -

n = int(input())

# for i in range(n):
#     if i % 2:
#         print('-', end="") # 홀수면 -출력
#     else:
#         print('+', end="") # 짝수면 +출력

# print()

# 문제점 : if문을 n번 수행해야함. 상황에 따라 유연하게 수정하기 어려움.
# i in range(n) => 0 ~ n-1 
# _ (언더스코어) in python = 무시하고 싶은 값

for _ in range(n//2): # range()에서 반환해주는 인덱스값 사용X
    print('-+', end="") # 홀짝이 반복되므로 n//2만큼 -+반복
if n % 2:
    print('-', end="") # n이 홀수일때만 -출력

print()

# 카운터용 변수를 0에서 1로 변경해도 유연하게 대응, 본문 변경X