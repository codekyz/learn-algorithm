# 어떤 정수 이하의 소수prime number를 모두 나열하는 알고리즘

# 1000 이하의 소수를 나열하기
# n은 2부터 n-1까지 어떤 정수로도 나누어 떨어지지 않으면 = 소수

# cnt = 0

# for n in range(2,1001):
#     for i in range(2, n):
#         cnt += 1
#         if n % i == 0:
#             break
#     else:
#         print(n)

# print(f'나눗셈을 실행한 횟수: {cnt}')

# 불필요한 나눗셈을 계속 실행하고 있는 프로그램

# 개선된 알고리즘1
# n는 2부터 n-1까지 어떤 소수로도 나누어 떨어지지 않으면 = 소수

# cnt = 0 # 나눗셈 횟수
# ptr = 0 # 이미 찾은 소수의 개수
# prime = [None] * 500 # 소수를 저장하는 배열

# prime[ptr] = 2
# # 소수 2 초기값으로 지정
# ptr += 1

# for n in range(3, 1001, 2): # 홀수만
#     for i in range(1, ptr): # 저장된 소수와 나눗셈
#         cnt += 1
#         if n % prime[i] == 0:
#             break
#     else:
#         prime[ptr] = n
#         ptr += 1

# for i in range(ptr):
#     print(prime[i])
# print(f'나눗셈 실행 횟수 : {cnt}')


# 개선된 알고리즘 2
# 약수의 대칭성
# n은 n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않으면 = 소수


cnt = 0 # 나눗셈 횟수
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수를 저장하는 배열

prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2): # 홀수만
    i = 1
    while prime[i] * prime[i] <= n:
        cnt += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        cnt += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈 실행 횟수 : {cnt}')


# 리스트의 원소와 복사
# list.copy()로 복사를 해서 두 변수에 대입을 하게 되면 두 변수가 같은 곳을 참조하므로
# 값을 변경하면 두 변수 모두 달라 질 수 있음
# = 원소 수준에서 얕은 복사 shallow copy
# copy 모듈안에 deepcopy()
# = 구성 원소 수준까지 깊은 복사 deep copy

# 객체가 참조 자료형의 멤버를 포함하는 경우 = 얕은 복사
# 참조값만 복사하는 방식

# 참조값 뿐만 아니라 참조하는 객체 자체를 복사하는 경우 = 깊은 복사
# 객체가 갖는 모든 멤버(값과 참조형식 모두)를 복사하므로 전체 복사라고도 함