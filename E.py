f = open('input.txt')
A = f.readline().split()
N = int(A[0])
K = int(A[1])
S = [0] * N
for i in range(K):
    B = f.readline().split()
    for j in range(len(B)):
        B[j] = int(B[j])
    for a in range(1,N+1):
        if B[0] == a:
            S[a-1] -= B[2]
        if B[1] == a:
            S[a-1] += B[2]

f = open('output.txt', 'w')
print(S, file = f)
f.close()

