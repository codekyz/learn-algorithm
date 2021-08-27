# repetition structure

# n에 양수값만 받도록 예외처리
while True: #infinite loop
    n = int(input())
    if n > 0:
        break
    
sum = 0
gsum = 0
i = 1

# 사전 판단 반복 구조
# 파이썬은 사후 판단 반복문 제공X ex) do~ while
while i<=n:
    sum += i
    i += 1
# gauss : sum = n* (n+1) // 2

print('sum =', sum, end=" ")
print('i =', i)

gsum = n*(n+1)//2
print('gsum =', gsum)

# python iterable type : list, str, tuple
