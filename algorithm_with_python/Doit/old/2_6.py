# 각 배열 원소의 최대값을 구해서 출력하기 (튜플, 문자열, 문자열 리스트)

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DS', 'AAC', 'YZ']

print(f'max of {t} : {max_of(t)}')

print(f'max of {s} : {max_of(s)}')

print(f'max of {a} : {max_of(a)}')
# 문자열 리스트의 최대값은 사전순으로 가장 큰 문자코드 or 문자열 출력(뒤쪽순서)

# python의 대입은 참조를 기본으로 하기때문에
# 원소값이 같은 튜플, 리스트를 따로 생성하면 is 연산자로 identity를 확인했을때
# false가 나옴
# 먼저 생성된 ls1를 ls2가 참조하도록 하게되면
# 같은 객체를 가리키므로 identity를 확인했을때 true가 나오며 원소를 바꾸게 되면 둘다 동일하게 반영