# Stack 스택
# 데이터를 임시 저장할 대 사용하는 자료구조
# 후입선출 LIFO last in first out
# push 스택에 데이터를 넣는 작업
# pop 스택에서 데이터를 꺼내는 작업
# top
#  -
# bottom

# ptr : stack pointer 스택에 쌓여있는 데이터의 개수를 나타내는 정숫값
# FixedStack은 ptr값이 반드시 0이상이거나 capacity값 이하가 됨
# 따라서 is_empty(), is_full() 함수를 정의할 때 ==를 사용하기보다 < >= 연산자를 사용해야 오류X

# 예외처리 클래스 Empty
# pop()함수 또는 peek()함수를 호출할 때 스택 비어있으면 내보내는 예외처리

# 예외처리 클래스 Full
# push()함수를 호출할때 스택이 가득 차 있으면 내보내는 예외처리

# 쌓여있는 데이터 개수를 알아내는 __len()__함수
# __len()__함수는 스택에 쌓여있는 데이터 개수를 반환. 스택보인터 ptr값을 그대로 반환

# 스택이 비어있는지를 판단하는 is_empty() 함수
# 데이터가 하나도 쌓여있지 않은 상태, 비어있는지를 판단.

# 스택이 가득 차 있는 지를 판단하는 is_full() 함수
# 데이터를 푸시할 수 없는 상태, 가득 차 있는지 판단.

# 고정 길이 스택 클래스 FixedStack 구현

# 예외 처리의 기본 구조
# ↓ try문
# try : 원래 처리
# except : 예외 포착과 처리
# else : 예외가 포착되지 않음
# finally : 마무리

# try-finally문


from typing import Any

class FixedStack:
    class Empty(Exception):
        pass
        # 비어있는 FixedStack에 팦 또는 피크할 때 내보내는 예외처리

    class Full(Exception):
        pass
        # 가득 찬 FixedStack에 푸시할 때 내보내는 예외처리

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
    
# 데이터를 푸시하는 push() 함수
# 스택이 가득 차면 FixedStack.Full을 통하여 예외 처리를 내보냄
# 가득 차 있지 않으면 value를 stk[ptr]에 저장하고 ptr을 1 증가

# pop()함수
# 스택이 비어있는 경우 FixedStack.Empry을 통하여 예외 처리를 내보냄
# 비어있지 않으면 ptr을 1 감소시키고 str[ptr]에 저장된 값을 반환

# peek()함수
# 스택의 꼭대기 데이터, pop()할 수 있는 데이터
# 스택이 비어있는 경우 FixedStack.Empty를 통하여 예외 처리 내보냄
# 비어 있지 않으면 stk[ptr-1]의 값을 반환

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full # 예외 처리 발생
        self.stk[self.ptr] = value 
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty # 예외 처리 발생
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty # 예외 처리 발생
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

# raise문을 이용한 의도적 예외 처리
# 표준 내장 예외 처리 : ValueError 클래스 ZeroDivisionError 클래스 등 파이썬이 제공하는 예외처리
# 표준 내장 예외 처리는 BaseException클래스와 직간접적으로 파생한 클래스로 제공
# 사용자 정의 예외 처리 : Exception클래스 에서 파생하는 것이 원칙
# BaseException 클래스는 사용자 정의 클래스가 파생하는 것을 전제로 함

# find()함수
# stk 안에 value와 값이 같은 데이터가 포함되어 있는지 확인하고 어디에 들어있는지 검색
# top에서 bottom으로 선형검색(인덱스큰쪽에서 작은쪽으로)

# __contains__()함수
# stk에 value가 있는지 판단 True or False
# membership test operator인 in을 사용하여 x in stk로도 수행할 수 있음

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> None:
        if self.is_empty():
            print('스택 비어있음')
        else:
            print(self.stk[:self.ptr])

# dunder 던더 함수
# double underscore === dunder
# __len__() 던더 렌
# 클래스형의 인스턴스를 던더 렌 함수에 전달 할 수 있음
# __contains__()
# 클래스형의 인스턴스에 멤머십 판단 연산자인 in을 적용할 수 있음
# 던더 함수에 대해서 더 알아보기