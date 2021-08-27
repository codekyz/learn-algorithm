# 기수 변환 (n진수 구하기)
# 정수값을 임의의 기수로 변환하는 알고리즘
# 정수를 n진수로 변환하기 위해서는 정수를 n으로 나누어야 하는데
# 몫은 0이 될때까지 나누고 나머지는 역순으로 정렬한다

# 10진수 정수를 입력받아 2~36진수로 변환하여 출력

# 정수값 x를 r진수로 변환한뒤 그 수에 나타내는 문자열을 반환

def card_conv(x: int, r: int) -> str :
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # while x > 0:
    #     d += dchar[x % r]
    #     x //= r

    n = len(str(x))
    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('  +' + (n + 2) * '-')
        if x//r :
            print(f'{r:2} | {x//r:{n}d} ... {x%r}')
        else:
            print(f'     {x//r:{n}d} ... {x%r}')
        d += dchar [x%r]
        x //= r

    return d[::-1] #역순으로 반환

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:
            no = int(input('변환할 음이 아닌 정수 입력 : '))
            if no > 0:
                break
        while True:
            cd = int(input('어떤 진수로 변환할까요? : '))
            if 2 <= cd <= 36:
                break
        print(f'{cd}진수로는 {card_conv(no, cd)}')

        retry = input('다시 하시겠어요?(y or n) : ')
        if retry in {'N', 'n'}:
            break


# python에서의 인수 전달은 실제 인수인 객체에 대한 참조를 값으로 전달하여 매개변수에
# 대입되는 방식으로 call by value와 call by reference의 중간적인 참조하는 값 전달
# == call by object reference

# immutable 인수 : 함수 안에서 매개변수의 값을 변경하면 다른 객체를 생성하고 그 객체에 대한 참조로 업데ㅣ트
# 따라서 매개변수의 값을 변경해도 호출하는 쪽의 실제 인수에는 영향을 주지 않음

# mutable 인수 : 함수 안에서 매개변수의 값을 변경하면 객체 자체의 업데이트
# 따라서 매개변수의 값을 변경하면 호출하는 쪽의 실제 인수는 값이 변경