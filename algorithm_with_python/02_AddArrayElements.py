def sum(n, S):
    result = 0
    for i in range(1, n+1):
        result += S[i]
    return result

S = [-1, 10, 7, 11, 5, 13, 8]
sum = sum(len(S) - 1, S)
print('sum =', sum)

# Add Array Elements
# 리스트 S의 원소들을 모두 더한 값을 구하기