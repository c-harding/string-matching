from sys import argv, exit
from comparer import Comparer


def run_naïve(text, pattern, compare):
    """
    Yield every match of the pattern in the text, making comparisons with the
    provided compare function.
    """

    # While the pattern does not overflow the text:
    for i in range(len(text)-len(pattern)+1):
        # Check every character in the pattern against the relevant character
        # in the text
        for j in range(len(pattern)):
            if not compare(text, i+j, pattern, j):
                break
        else:
            # If there are no mismatches, yield the position
            yield i


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

    for match in run_naïve(text, pattern, compare):
        print(f'Match found at position {match}')

    print(f'{compare.count} comparisons')

