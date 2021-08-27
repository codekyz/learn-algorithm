# 파이썬에서는 array가 없고 list와 tuple로 array를 구현함

list1 = [] # 빈리스트 생성
list2 = [1,2,3]
list3 = ['A', 1, 'B',] # 마지막 원소에 쉼표 써도 상관X

# list는 원소를 변경할 수 있는 mutable list object
# 내장함수 list() 사용

list4 = list() # 빈리스트 생성
list5 = list('ABC') # ['A', 'B', 'C'] 문자열의 각 문자로부터 원소 생성
list6 = list([1,2,3]) # 리스트로 부터 원소 생성
list7 = list((1,2,3)) # 튜플로 부터 원소 생성
list8 = list({1,2,3}) # 집합으로 부터 원소 생성

# 특정 범위의 정수로 구성된 리스트는 list()와 range()

list9 = list(range(7)) # 0~6
list10 = list(range(2, 10, 3)) # [2,5,8]

list11 = [None] * 5 # 원소값이 주어지지 않은 크기가 5인 리스트 [none, none, none, none, none]
# 문자열 자료형 또한 *로 반복하는 문자열 만들수 있음 

# tuple은 원소에 순서를 매겨 결합한 것으로 원소를 변경할 수 없는 immutable data type

tuple1 = () # 빈튜플
tuple2 = 1, # (1,)
tuple3 = (1,)
# tuple 의 element가 한개인 경우 반드시 쉼표 붙여야 변수와 구분됨
# tuple2 = (1) <- 튜플이 아닌 하나의 값을 가진 int변수

tuple4 = 1,2,3 #(1,2,3)
tuple5 = 1,2,3,
tuple6 = (1,2,3)
tuple7 = (1,2,3,) #(1,2,3)

# 내장함수 tuple()

tuple8 = tuple() # 빈리스트 생성
tuple9 = tuple('ABC') # ('A', 'B', 'C') 문자열의 각 문자로부터 원소 생성
tuple10 = tuple([1,2,3]) # 리스트로 부터 원소 생성
tuple11 = tuple({1,2,3}) # 집합으로 부터 원소 생성

# 마찬가지로 range()+tuple()로 특정 범위의 값들로 생성가능(원소변경X)


# unpack : list와 tuple 풀어내기
x = [1,2,3]
a, b, c = x # x를 unpack 하여 대입
# print(a,b,c) # 1,2,3

# index는 0부터 1씩 증가
# 음수 index는 0-전체원소 수 부터 1씩 증가
# ex) 양수 index 0 ~ 6 / 음수 index -7 ~ -1

# *** tuple은 immutable 속성때문에 대입하면 오류남
# 존재하지 않는 인덱스로 접근하거나 대입해도 새로 추가 안됨

# Slice 슬라이스
# list or tuple의 원소 일부를 연속해서 또는 일정한 간격으로 꺼내 새로운 list or tuple을 만듬

# s[i:j] -> s[i] ~ s[j-1] 까지 나열
# s[i:j:k] -> s[i] ~ s[j-1]까지 k씩 step
# i, j가 len(s)보다 커도 오류X / len(s)값으로 간주
# i 생략 or None = 0으로 간주
# j 생략 or None = len(s)값으로 간주
# [:] 모두생략하면 처음부터 끝까지
# [::-1] 맨 뒤에서부터 전부 출력(순서 반대로)


x = 6
y = 2
x, y = y + 2, x + 3 
# 두 대입식이 동시에 이루어 지므로 x값이 업데이트 되지 않고 6으로 대입

# mutable : dictionary, list, set
# immutable : number, string, tuple

# 파이썬에서 대입연산자는 연산자로 취급하지 않으므로
# ex) x = 17 -> 식statement 이 아닌 문expression으로 취급
# 따라서 a = (b = 1) 성립되지 않음(error) / c, c++, java와 차이
