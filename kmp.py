from sys import argv
from comparer import Comparer


def prefix(pattern):
    table = [0]
    j = 0
    compare = Comparer()
    for i in range(1,len(pattern)):
        print(table)
        # if the last case was a success (j > 0), use it: if they compare true,
        # that means that this character is the one after the prefix in the
        # previous case
        # If they compare false, then clearly this is not the case. However,
        # we know that the past j characters are the same as the first j
        # characters, so use the analysis of the first j characters. Keep checking
        while j > 0 and not compare(pattern, i, pattern, j):
            j = table[j-1]

        # If j > 0, no need to perform character comparison: it must be true
        # because while loop has terminated
        if j > 0 or compare(pattern, i, pattern, j):
            j += 1

        # j = 0: no prefix.
        # j = 1: new prefix (len 1)
        # j > 1: extension of previous prefix
        table.append(j)
    return table

if __name__ == "__main__":
    try:
        pattern = argv[1]
    except IndexError:
        raise RuntimeError("No pattern")
    try:
        text = argv[2]
    except IndexError:
        raise RuntimeError("No text")
    
    print('Searching for "'+pattern+'" in "'+text+'".')
    print()

    compare = Comparer()

    table = prefix(pattern)
    print(table)

    q = 0

    for i in range(len(text)):
        # omit this to implement the algorithm a la CLRS/the slides/sheet 7q1,
        # which involves surplus comparisons
        if i - q + len(pattern) > len(text):
            break

        while q > 0 and not compare(text, i, pattern, q):
            q = table[q-1]
        if q > 0 or compare(text, i, pattern, q):
            q += 1
        if q == len(pattern):
            print("Match found at position "+str(i-q+1))
            q = table[q-1]

    print(str(compare.count)+" comparisons")
