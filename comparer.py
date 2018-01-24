class Comparer:
    """
    A class for comparing string characters, and keeping a track of the number
    of comparisons. The instances act like functions, but with the attribute
    .count to get the number of comparisons made, so the number of times the
    function has been called.
    """
    count = 0
    
    def __call__(self, text, i, pattern, j=0):
        """
        Run a comparison, printing the strings lined up with a caret at the
        relevant position, and increment the comparison counter.

        :param text: The first string, typically the text being searched in.
        :param i: The index of the character from the first string to compare.
        :param pattern: The second string, typically the pattern to search for.
        :param j: The index of the character from the second string to compare.
                  Defaults to zero, so `pattern` can be a single character
                  rather than a string.
        :return: Boolean of whether the characters match.
        """
        print(' '*(j-i) + text)
        print(' '*(i-j) + pattern)
        print(' '*(max(i,j)) + '^')
        self.count += 1
        return text[i] == pattern[j]
