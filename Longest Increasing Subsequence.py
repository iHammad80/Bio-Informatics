import os

def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result


def lds(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] > arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result


def solution(number):
    lis_seq = lis(numbers)
    print(' '.join(map(str, lis_seq)))
    lds_seq = lds((numbers))
    print(' '.join(map(str, lds_seq)))



file = 'rosalind_lgis.txt'
if os.path.exists(file):
    print(f'{file} exists!\n')
    with open(file) as f:
        n = int(f.readline())
        numbers = list(map(int, f.readline().strip().split()))
    solution(numbers)

else:
    print(f'{file} does\'nt exists!\n')


