# 2. 이진 검색 Binary Search
# 배열의 원소가 정렬sort 되어 있어야함
# 오름차순이나 내림차순으로 정렬된 배열에서 효율적인 알고리즘
# 선형 검색보다 빠름
# 종료 조건
# - 검색 성공 : a[pc]와 key가 일치하는 경우
# - 검색 실패 : 검색 범위가 더 이상 없는 경우

# 이진 검색 알고리즘
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a)-1

    while True:
        pc = (pl+pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    # return -1
    raise ValueError
    # 예외 처리

if __name__ == '__main__':
    num = int(input('원소 수 입력 : '))
    x = [None] * num

    print('데이터를 오름차순으로 입력하세요')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i-1]:
                break

    ky = int(input('검색할 원소 입력 : '))

    try:
        idx = bin_search(x, ky)
    except ValueError:
        print('검색 실패')
    # 예외처리
    else:
        print(f'검색 성공 : x[{idx}]')

# 반복할때 마다 검색 범위가 거의 절반으로 줄어드므로
# 필요한 비교 횟수는 평균 log n
# 실패할 경우 |log(n+1)| (|x| : x의 천장함수 ceiling function, x보다 크거나 같은 정수 가운데 가장 작은 수)
# 성공할 경우 log n -1

# 알고리즘의 성능을 객관적으로 평가하는 기준 = 복잡도 complexity
# - 시간 복잡도 time complexity : 실행하는데에 필요한 시간 평가
# - 공간 복잡도 space complexity : 메모리와 파일공간이 얼마나 필요한지 평가

# 2~3가지 이상의 계산으로 구성된 알고리즘은
# 차원이 가장 높은 복잡도를 선택해 전체 복잡도가 되므로
# 선형검색 알고리즘의 시간 복잡도는 O(n) / n에 비례하는 횟수만큼 실행되는 경우
# 이진검색 알고리즘의 시간 복잡도는 O(log n) / n에 비례하는 횟수만큼 실행되는 경우

# index() 함수로 검색하기
# obj.index(x, i, j)
# obj[i:j]에서 x와 값이 같은 원소를 찾아서 가장 작은 인덱스 반환
# 없으면 예외처리로 ValueError 반환