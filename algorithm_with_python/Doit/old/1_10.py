# 왼쪽 아래가 직각인 이등변 삼각형

n = int(input('짧은 변의 길이 : '))

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

# 오른쪽 아래가 직각인 이등변 삼각형

for i in range(n):
    for _ in range(n-i-1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()

# 파이썬의 변수(data,def,class,module,package...) = 객체 object
# object = data type & memory(저장공간) & identity(식별번호)
# 파이썬의 변수는 값을 갖지 않는다
# 변수는 객체를 참조하는 객체에 연결된 이름
# 값이 변경되는 것이 아니므로 immutable 속성을 가짐

# 대입연산자는 변수에 값을 복사하는 것이 아니라 객체를 참조하는 것. 겷합 bind
# ex) n = 17 => 정수 literal 17의 id == n의 id

# 따라서 함수 내부, 외부 에서 정의한 변수들은 같은 값을 가지면 id또한 같음
# 같은 값이 들어있는 상자를 참조하기 때문
# 기본적으로 포인터 개념을 사용함
# C에서는 함수가 종료하면 함수 내부에서 선언된 변수 또한 소멸하지만
# 파이썬에서는 객체가 소멸되지 않고 남아있음

# 함수가 종료된 뒤 함수내부의 변수 id 값을 확인하면 여전히 존재함