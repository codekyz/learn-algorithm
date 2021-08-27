def fib (n):
    if(n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

# for i in range(101):
#     print(fib(i), end=" ")

# 피보나치 수열의 n번째 항 구하기
# 재귀적 정의 이용 : 작성하기도 쉽고 이해하기도 쉬움
# 그러나 비효율적임
# 함수 호출은 부담이 큰 연산인데
# 여러번 중복해서 계산을 해나가야 함
# fib(100) 개 오래 걸림

# 개선점
# 같은 값을 중복해서 재귀적으로 계산X
# 이미 계산한 피보나치 항의 값은 리스트에 저장
# 필요할 때 꺼내 씀

# 효율성을 개선 한 코드 ↓ Iterative한 방법(반복적인)

def fib2 (n):
    f = [0] * (n+1)
    if (n > 0):
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
            # print('i =', i, 'f-1=', f[i-1], 'f-2=', f[i-2])
            # print('f[i]=', f[i])
    return f[n]

# for i in range(11):
    # print(fib2(i), end=" ")
    # print(fib2(i))


# 속도가 훠어어얼씬 빠름
# 그러나 공간적인 측면에서는 재귀함수를 이용하는게 효율성이 좋음

# 그렇다면 list f를 사용하지 않고 피보나치 항을 구할수 있는가?
# 우리가 알고자 하는 값은 마지막 n값


def fib3 (n):
    if (n < 2):
        return n
    else:
        a, b = 0, 1
        for i in range(n-1):
            result = a + b
            a, b = b, result
        return result

for i in range(101):
    print(fib3(i), end=" ")

# list를 사용하지 않음