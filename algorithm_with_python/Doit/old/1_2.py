# FEB 8 : 파이썬 코드 작성 규칙
# 2개 이상의 단순문은 ;으로 구분하여 같은행에 있을 수 있음

# Find mid value

# def mid3(a, b, c):
#     if a >= b:
#         if  b >= c:
#             return b
#         elif a <= c:
#             return a
#         else:
#             return c
#     elif a > c:
#         return a
#     elif b > c:
#         return c
#     else:
#         return b

def mid3(a, b, c):
    if (a >= b and c >= a) or (a <= b and c <= a):
        return a
    elif (b >= a and c >= b) or (b <= a and c <= b):
        return b
    return c
# 코드는 짧지만 if에서 비교를 마친 a,b를 elif에서 다시 비교를 하므로 효율X


a, b, c = map(int,input().split())

print(mid3(a,b,c))