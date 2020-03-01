# python3

"""
    Rabin-Karp Algorithm uses a hashed table data structure for pattern searching.

    Input: Takes two strings: the text, T, in which to search, and the pattern, P,
    string to look for.

    Output: Prints all the positions of the occurences of the pattern in the text
    in ascending order. Uses 0-based indexing of text, T.

"""
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    patternLength, textLength = len(pattern), len(text)
    positionsOfOccurence = []

    # Arbitrarily chosen cardinality (prime), and a multiplier for selecting
    # a hash function from the polynomial family.
    prime, multiplier = 1000000007, 12
    patternHash = polyHash(pattern, prime, multiplier)

    hashedValues = precomputeHash(text, textLength, patternLength, prime, multiplier)

    # Compares the hash values of each substring of pattern length, against the pattern hashed value.
    # If the hash values are the same, compare the entire string.
    for i in range(0, textLength - patternLength + 1):
        if patternHash != hashedValues[i]:
            continue
        if text[i:i + patternLength] == pattern:
            positionsOfOccurence.append(i)
    return positionsOfOccurence

def precomputeHash(text, textLength, patternLength, prime, multiplier):
    # Precomputes the hash values of each substring within text, T, of length pattern, P.
    # Returns an array of these hashed values to be compared against.

    diff = textLength - patternLength
    hashedValues = [0 for _ in range(0, diff + 1)]
    rightEndedString = text[diff:textLength]
    # the hashed value of the last substring key, of pattern length
    hashedValues[diff] = polyHash(rightEndedString, prime, multiplier)

    power = 1
    for _ in range(1, patternLength + 1):
        # Obtains the highest power of the polynomial equation, x^len(p)
        power = (power * multiplier) % prime
    for j in range(diff - 1, -1, -1):
        hashedValues[j] = ((multiplier * hashedValues[j + 1]) + ord(text[j]) - (power * ord(text[j + patternLength]))) % prime
    return hashedValues

def polyHash(string, prime, multiplier):
    # Polynomial hash function family
    ans = 0
    for char in reversed(string):
        ans = ((ans * multiplier) + ord(char)) % prime
    return ans

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

