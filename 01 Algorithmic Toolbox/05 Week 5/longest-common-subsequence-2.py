#Uses python3

import sys

def lcs2(n, m, a, b):
    w, h = m + 1, n + 1
    Matrix = [[0 for j in range(w)] for i in range(h)]

    for i in range(1, h):
        for j in range(1, w):
            insertion = Matrix[i][j - 1]
            deletion = Matrix[i - 1][j]
            mismatch = Matrix[i - 1][j - 1] - 1
            match = Matrix[i - 1][j - 1] + 1
            if a[i - 1] == b[j - 1]:
                Matrix[i][j] = max(insertion, deletion, match)
            else:
                Matrix[i][j] = max(insertion, deletion, mismatch)
    return Matrix[n][m]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(n, m, a, b))
