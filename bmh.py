from collections import defaultdict
from sys import argv
from comparer import Comparer


def precalc(pattern):
    table = defaultdict(lambda: len(pattern))
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - i - 1
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

    skip = 0

    compare = Comparer()

    i = len(pattern) - 1

    table = precalc(pattern)
    print(dict(table))

    while skip + len(pattern) <= len(text):
        while i >= 0 and compare(text, skip+i, pattern, i):
            i -= 1
      
        if i < 0:
            print("Match found at position "+str(skip))
            i = len(pattern) - 1
      
        skip += table[text[skip + len(pattern) - 1]]

    print(str(compare.count)+" comparisons")
