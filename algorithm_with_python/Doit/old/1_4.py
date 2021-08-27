# a ~ b 정수의 합

a, b = map(int,input().split())

if a > b:
    a, b = b, a
# 단일 대입문으로 swap
# 내부적으로 튜플을 만들어 튜플을 풀면서 대입
# 오름차순 정렬

sum = 0
# for i in range(a, b+1):
#     # 합을 구하는 과정 출력
#     if i < b:
#         print(i, '+', end=" ")
#     else:
#         print(i, '=', end=" ")
#     # 덧셈하는 동안 의미없이 조건확인함 / 판단, 반복 n번
#     sum += i

# 개선↓ / 판단x 반복n-1
for i in range(a, b): # 3 4 5 6 7 8 / range : 3 4 5 6 7
    print(i, '+', end=" ")
    sum += i

print(b, '=', end=" ") # b = 8
sum += b

print(sum)
# print('a =', a,'b =', b, 'sum =', sum)
