# 파이썬의 list와  tuple = 자료구조의 array
# empty array = return false
# 비교 연산자로 배열의 대소 또는 등가 관계르 판단할 수 있음

# 내포 표기 생성이란?
# list 안에서 for, if 문을 사용하여 새로운 list를 생성하는 기법
# (tuple은 불가능)

numbers = [1,2,3,4,5]
twise = [num * 2 for num in numbers if num % 2 == 1]
# list numbers의 홀수 원소값을 *2 한 리스트 생성
# list의 element를 for문을 통해 조회하여 홀수면 2를 곱함
print(twise)