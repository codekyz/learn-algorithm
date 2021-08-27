# collections.deque로 스택 구현하기

# 파이썬의 내장 컨테이너는 dirctionary, list, set, tuple이 있음
# 이 외에도 여러 컨테이너를 collections 모듈로 제공함
# 주요 컨테이너는 namedtuple(), deque, ChainMap, Coundter, OrderedDict, defaultdict, UserDict, UserList, UserString
# 이 중 deque 모듈을 이용하면 스택을 간단하게 구현할 수 있음
# collection.deque는 맨 앞과 맨 끝 양쪽에서 원소를 추가, 삭제하는 자료구조인 덱 deque을 구현하는 컨테이너

# deque의 주요 속성과 함수
# maxlen 속성 : 최대 크기를 나타내는 속성으로 읽기 전용, 크기 제한이 없으면 None
# append(x) : 맨끝(오른쪽)에 x를 추가
# appendleft(x)
# clear() : 모든 원소를 삭제하고 크기를 0으로
# copy() : 얕은 복사 shallow copy
# count(x) : x와 같은 원소의 개수 계산
# extend(iterable) : iterable에서 가져온 원소를 맨 끝에 추가하여 확장
# extandleft(iterable)
# index(x[, stert [, stop]])
# : deque안에 있는 (인덳스 start부터 stop까지 양끝을 포함한 범위) * 가운데 가장 앞쪽에 있는 원소 위치를 반환
# x가 없으면 ValueError 반환
# insert(i, x) : x를 i위치에 삽입, maxlen을 초과한 삽입은 IndexError
# pop() : 맨 끝에 있는 원소를 1개 삭제하고 그 원소를 반환, 원소가 하나도 없으면 IndexError
# popleft()
# remove(value) : value의 첫번째 항목 삭제, 없으면 ValueError
# reserve() : 역순으로 재정렬하고 None을 반환
# rotate(n = 1) : 모든 원소를 n값 만큼 오른쪽으로 밀어냄, 음수라면 왼쪽으로 밀어냄

# 이 외에도 이터레이션과 pickle, len(d), reversed(d), copy.copy(d), copy.deepcopy(d),
# in 연산자로 멤버쉽 판단, d[0]등의 형식에서 인덱스에 의한 참조를 지원
# 양 끝의 데이터를 인덱스로 접근하는 것은 O(1)로 빠르지만 가운데 부분에 있는 데이터를 접근하는 것은 O(n)으로 느림
# 그러므로 인덱스를 사용하여 임의의 원소를 무작위로 접근하는 것은 효율적이지 않음


