# 배열검색
# - 선형 검색, 이진 검색, 해시법(체인법, 오픈주소법)

# 1. 선형 검색 Linear search
# 직선모양(선형)으로 늘어선 배열에서 검색하는 경우에
# 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘
# 원소값이 정렬되지 않은 배열에서 검색할때 사용하는 유일한 방법
# 종료 조건
# - 검색 실패 : 값을 찾지 못하고 배열의 맨 끝을 지나침
# - 검색 성공 : 값과 일치하는 원소를 찾음
# 배열의 원소가 n개 일때 조건을 판단하는 횟수는 평균 n/2번

# while 문으로 작성한 선형 검색 알고리즘 
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    while True:
        if i == len(a):
            return -1 # search fail
        if a[i] == key:
            return i # search success
        i += 1


# for문으로 구현
def seq_search_f(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


if __name__ == '__main__':
    num = int(input('원소의 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input('검색할 값 입력 : '))
    idx = seq_search_f(x, ky)

    if idx == -1:
        print('검색값이 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

