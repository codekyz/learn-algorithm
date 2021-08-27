# List scan
# Tuple scan
# 동일함

# x = ['John', 'George', 'Paul', 'Ringo']
x = ('John', 'George', 'Paul', 'Ringo')


# 2_7-1
# 원소 수를 len()함수로 미리 알아내서 0에서 원소 수-1까지 반복
# range()와 len()이 중첩되므로 권장되지 않는 패턴

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
print()

# 2_7-2
# 인덱스와 원소를 짝지어 enumerate()함수로 반복해서 꺼냄
# 반복문 사용 시 몇번째 반복문인지 확인이 필요할때 사용
# 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
print()

# 2_7-3
# -2와 같지만 1부터 카운트를 시작

for i, name in enumerate(x, 1):
    print(f'{i} : {name}')
print()

# 2_7-4
# 인덱스값을 사용하지 않고 in을 사용해서 원소를 처음부터 순서대로 꺼냄
# 인텍스값이 필요하지 않은 경우라면 가장 깔끔

for i in x:
    print(i)


# iterable 이터러블
# 문자열, 리스트, 튜플, 집합, 딕셔너리 등의 자료형 객체는 모두 반복가능한 이터러블 객채로
# 원소를 하나씩 꺼내는 구조이며 내장함수인 iter()의 인수로 전달하면
# 그 객체에 대한 iterator(반복자) 를 반환합니다. 
# 이는 데이터의 나열을 표현하는 객체로 iterator의 __next__ 함수를 호출하거나
# 내장함수인 next()함수에 iterator를 전달하면 원소를 순차적으로 꺼낼수 있음
# 꺼낼 원소가 더이상 없으면 StopIteration 예외 발생


