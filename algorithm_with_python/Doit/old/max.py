# Sequence element의 최대값 출력

from typing import Any, Sequence
# 복잡한 타입의 어노테이션 추가를 위해 typing 모듈 사용
# Any = 제약없는 임의의 자료형
# Sequence = list, bytearray, str, tuple, bytes

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)): # maximum = a[0] 이므로 i는 1 시작
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    # __name__은 모듈 이름을 나타내는 변수
    # 스크립트 프로그램이 직접 실행 될 때 변수 __name__ = '__main__'
    # 스크립트 프로그램이 import 될 때 변수 __name__ = 원래의 모듈 이름
    # 해당 프로그램(모듈, 파일)을 다른 파일에서 import시켜 사용하게 되는 경우
    # __name__은 '__main__'이 아니므로 해당 내용은 실행되지 않음
    print('배열의 최대값 구하기')
    num = int(input('원소의 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요 : '))
    
    print(f'최대값은 {max_of(x)}입니다')


# 함수 어노테이션, 변수 어노테이션 / type hint, type hinting
# python3
# 변수나 함수 사용시 자료형에 대한 선언이 없으므로 명시적 해석을 위해 추가한 주석
# 파라미터에 :expression 형태로 매개변수마다 작성 가능
# function의 return값에 대해서는 -> expression 형태로 사용
# annotation은 주석이므로 실제로는 이와 상관없이 실행됨
# 작성한 타입 어노테이션을 검사하고 싶을때는 __annotations__ 내장 사전 객체 사용