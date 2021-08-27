def seqsearch(n, S, x):
    location = 1
    while (location <= n and S[location] != x):
        location += 1
    if(location > n):
        location = 0
    return location

S = [0, 10, 7, 11, 5, 13, 8]
x = 5
location = seqsearch(len(S) - 1, S, x)
print('location =', location)

x = 4
location = seqsearch(len(S) - 1, S, x)
print('location =', location)

# Sequential Search 순차 탐색
# S의 원소 중 x를 찾아 인덱스를 리턴, 없으면 0 리턴