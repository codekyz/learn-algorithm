# reverse sort of mutable sequence element

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('reverse sort of array element')
    nx = int(input('enter number of element : '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}] = '))

    reverse_array(x)

    print('finish reverse sort')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

# python 표준 라이브러리를 이용한 리스트 역순 정렬
# x.reverse() / 튜플은 안됨 immutable이므로
# y = list(reversed(x)) # x의 원소를 역순으로 정렬하여 y에 대입