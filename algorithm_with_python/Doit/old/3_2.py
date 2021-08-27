# 선형 검색에서 반복할때 마다 2가지 종료조건을 체크하는데에
# 드는 비용cost를 반으로 줄이기 위한 방법
# 보초법 Sentinel method

# 선형검색 알고리즘 3_1을 보초법으로 수정
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq) # seq 복사
    a.append(key) # 보초 key를 추가

    i = 0
    while True:
        if a[i] == key:
            break # 검색성공 while 종료
# 반복을 종료하기 위해 판단하는 횟수가 절반으로 줄어듬
        i += 1
    return -1 if i == len(seq) else i
# if condition one-liner
# 찾은 원소가 배열의 원래 데이터인지 보초인지 판단
# 따라서 if문의 판단횟수는 반으로 줄었지만 19행 수행으로 1번 늘어남


if __name__ == '__main__':
    num = int(input('원소 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    
    ky = int(input('검색값 입력 : '))
    idx = seq_search(x, ky)

    if idx == -1:
        print('존재하지 않음')
    else:
        print(f'x[{idx}]에 존재함')