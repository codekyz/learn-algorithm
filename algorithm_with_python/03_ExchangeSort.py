
def exchage (S) :
    n = len(S)
    for i in range(1, n):
        for j in range(i+1, n):
            if(S[i] > S[j]):
                S[i], S[j] = S[j], S[i] # swap
            # print(i, j, S)

S = [-1, 10, 7, 11, 5, 13, 8]
print('Before =', S)
exchage(S)
print(' After =', S)

# Exchange Sort 교환정렬