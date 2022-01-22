count = 0
for _ in range(int(input())):
    p_A = list(map(int, input().split()))
    p_B = list(map(int, input().split()))
    for i in range(3):
        if p_A[i] >= p_B[i]:
            count += 1
    if count >= 2:
        print('A')
        count = 0
    else:
        print('B')
        count = 0
