from collections import defaultdict
from sys import argv, exit
from comparer import Comparer


def precalc(pattern):
    """
    Create the precalculation table: a dictionary of the number of characters
    after the last occurrence of a given character. This provides the number of
    characters to shift by in the case of a mismatch. Defaults to the length of
    the string.
    """
    table = defaultdict(lambda: len(pattern))
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - i - 1
    return table


def run_bmh(table, text, pattern, compare):
    """
    Using the precalculated table, yield every match of the pattern in the
    text, making comparisons with the provided compare function.
    """
    
    # Currently attempted offset of the pattern in the text
    skip = 0

    # Keep going until the pattern overflows the text
    while skip + len(pattern) <= len(text):

        # Start matching from the end of the string
        i = len(pattern) - 1

        # Match each element in the pattern, from the end to the beginning
        while i >= 0 and compare(text, skip+i, pattern, i):
            i -= 1
      
        # If the start of the string has been reached (and so every comparison
        # was successful), then yield the position
        if i < 0:
            yield skip
        
        # Shift by the precalculated offset given by the character in the text
        # at the far right of the pattern, so that it lines up with an equal
        # character in the pattern, if posssible. Otherwise the pattern is
        # moved to after this position.
        skip += table[text[skip + len(pattern) - 1]]


if __name__ == "__main__":
    try:
        pattern = argv[1]
        text = argv[2]   
    except IndexError:
        print("usage: python3 bmh.py PATTERN TEXT")
        exit()

    print(f'Searching for "{pattern}" in "{text}".')
    print()

    compare = Comparer()

    table = precalc(pattern)
    print(f'Precomputed shift table: {dict(table)}')
    print()

    for match in run_bmh(table, text, pattern, compare):
        print(f"Match found at position {match}")

    print(f"{compare.count} comparisons")
