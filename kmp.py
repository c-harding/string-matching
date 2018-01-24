from sys import argv, exit
from comparer import Comparer


def prefix(pattern, compare):
    """
    Build the precalculated prefix table: For any index i, gives the length j
    of the longest strict prefix pattern[0:j] which is also a strict suffix
    pattern[i-j:i].
    This is done iteratively, as each prefix-suffix builds on the previous one,
    or a prefix thereof.
    """
    
    # For the string of length 0, there is no prefix.
    # For the string of length 1, a strict prefix must have length 0.
    table = [None, 0]

    # Initially there is no prefix-suffix to build on.
    j = 0

    # For each new character, excluding the initial character:
    for i in range(1,len(pattern)):
        # if the last prefix-suffix was a non-empty (j > 0), try to build upon
        # it:
            # If the character following the prefix is equal to the new
            # character, then we can extend the prefix-suffix.
            # Otherwise, we cannot extend the prefix-suffix. However, we know
            # that the past j characters are the same as the first j
            # characters, so use the analysis of the first j characters. Keep
            # checking prefix-suffixes thereof until a match is found, or there
            # is no more prefix-suffix left
        while j > 0 and not compare(pattern, i, pattern, j):
            j = table[j]

        # If j > 0, no need to perform character comparison: comparison must
        # hold because the loop terminated. Otherwise check if current
        # character matches first in the pattern, starting a new prefix-suffix.
        if j > 0 or compare(pattern, i, pattern, j):
            j += 1

        # j = 0: no prefix-suffix
        # j = 1: new prefix-suffix (length 1)
        # j > 1: extension of previous prefix-suffix
        table.append(j)
    return table


def run_kmp(table, text, pattern, compare):
    """
    Using the precalculated prefix table, yield every match of the pattern in
    the text, making comparisons with the provided compare function.
    """

    # Start with the first character of the text
    i = 0

    # And the first character of the pattern
    j = 0

    # While the pattern does not overflow the text:
    while len(pattern) - j <= len(text) - i:
        
        # Check if the next character in the text matches the next in the
        # pattern. If not, see if we can use a suffix of the text with a prefix
        # of the pattern
        while j > 0 and not compare(text, i, pattern, j):
            j = table[j]

        # If j > 0, no need to perform character comparison: comparison must
        # hold because the loop terminated. Otherwise check if current
        # character matches first in the pattern, starting a new match.
        if j > 0 or compare(text, i, pattern, j):
            j += 1

        # If the whole pattern has been matched, return it, and reuse a suffix
        # of the pattern for the next round.
        if j == len(pattern):
            yield i-j+1
            j = table[j]

        # Move on to the next character in the text
        i += 1

if __name__ == '__main__':
    try:
        pattern = argv[1]
        text = argv[2]
    except IndexError:
        print('usage: python3 kmp.py PATTERN TEXT')
        exit()
    
    print(f'Searching for "{pattern}" in "{text}".')
    print()

    compare = Comparer()

    table = prefix(pattern, compare)
    print(f'Prefix table: {table}')
    print(f'Prefix table took {compare.count} comparisons to build')
    print()

    # Use a new comparer for running the algorithm.
    compare = Comparer()

    for match in run_kmp(table, text, pattern, compare):
        print(f'Match found at position {match}')

    print(f'{compare.count} comparisons')
