# input : 정수 3개
# Find Maximum Value

# a = int(input())
# b = int(input())
# c = int(input())
# input() enter 입력전까지 문자열을 받고 enter를 제외한 string return

def max3(a, b, c):
    max = a
    if b > max: max = b
    if c > max: max = c
    return max
# sequential structure
# select Structure

print(f'max3(3,2,1)= {max3(3,2,1)}')
print(f'max3(5,1,0)= {max3(5,1,0)}')
print(f'max3(6,-1,-3)= {max3(6,-1,-3)}')