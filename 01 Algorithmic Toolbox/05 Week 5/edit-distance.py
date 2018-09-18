# Uses python3
def edit_distance(s, t):
    # Algorithm returns the minimum number of operations required (insertion, deletion and substitution)
    # to convert a string to another

    # Builds a two-dimensional vector matrix of the min edit distance for each node
    # edit_distance = insertion + deletion + subs

    # first string acts as the row (i), 
    # second string acts as the column (j)
    w, h = len(t) + 1, len(s) + 1
    Matrix = [[0 for i in range(w)] for j in range(h)]
    # D(i, j) = Matrix[i][j]

    for i in range(h):
        Matrix[i][0] = i
    for j in range(w):
        Matrix[0][j] = j

    for j in range(1, w):
        for i in range(1, h):
            insertion = Matrix[i][j - 1] + 1
            deletion = Matrix[i - 1][j] + 1
            substitution = Matrix[i - 1][j - 1] + 1
            match = Matrix[i - 1][j - 1]
            if s[i - 1] == t[j -1]:
                Matrix[i][j] = min(insertion, deletion, match)
            else:
                Matrix[i][j] = min(insertion, deletion, substitution)

    return Matrix[-1][-1] # returns the total editing distance to match the whole of the two strings

if __name__ == "__main__":
    print(edit_distance(input(), input()))
