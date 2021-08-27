# 비교 연산자를 연속으로 사용하는 방법과 드모르간의 법칙

# 2자리 양수(10~99) 입력받기

while True:
    no = int(input())
    # if no >= 10 and no <= 99:
    # if 10 <= no <= 99:
    if not(no < 10 or no > 99):
        # 드모르간의 법칙 : 각 조건을 부정하고 논리곱을 논리합으로 논리합을 논리곱으로 바꾸고
        # 다시 전체를 부정하면 원래 조건과 같다.
        # x and y == not(not x or not y)
        # x or y == not(not x and not y)
        break

print(no)

# 구조적 프로그래밍 structured programming
# 순차, 선택, 반복 세 종류의 제어 흐름 사용 