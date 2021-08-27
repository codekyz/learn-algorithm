def binsearch(n, S, x):
    low = 1
    high = n
    location = 0
    while (low <= high and location == 0):
        mid = (low + high) // 2
        print(low, mid, high)
        if (x == S[mid]):
            location = mid
        elif (x < S[mid]):
            high = mid - 1
            # high의 위치를 mid 앞의 인덱스로
        else:
            low = mid + 1
            # low의 위치를 mid 뒤의 인덱스로
    return location

S = [-1, 5, 7, 8, 10, 11, 13]
x = 1
location = binsearch(len(S)-1, S, x)
print('S =', S)
print('x =', x)
print('location =', location)

# Binary Search 이분 탐색