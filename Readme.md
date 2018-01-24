# String Matching

This project provides a command-line implementation of the naïve,
Boyer-Moore-Horspool and Knuth-Morris-Pratt in Python, implemented
as part of the University of Bristol’s Data Structures and Algorithms course.
Each algorithm takes a pattern $P$ and a string $T$ to search for the pattern
in, and returns the indices of matches.

## Naïve algorithm

This algoithm performs simple string matching, without using any preprocessing
to reduce necessary comparisons. It attempts every possible alignment of the
pattern in the text, stopping when a mismatched character is found.

In the worst case, this algorithm has
$O\left(\left|T\right|\left|P\right|\right)$ runtime, which occurs when the
a significant part of the pattern matches at many positions in the string.

In the best case, the algorithm has $O\left(\left|T\right|\right)$ runtime,
which occurs when the pattern is close in length to the text, or the first
character of the pattern only occurs a few times in the text.

## Boyer-Moore-Horspool

This algorithm prepares a shift table for each character in the pattern,
representing the number of alignments that can be skipped when a mismatch 
occurs. The shift is given by the number of characters that occur after the
last occurrence of a given character in the pattern.

The naïve algorithm is then run, with the exception that the string is matched
from the right-hand side, and when a mismatch is found, the pattern is not
shifted by one position, but rather by the value in the shift table
corresponding to the character in the text lined up with the end of the
pattern.

The preparing part takes $O\left(\left|P\right|\right)$ time.

In the worst case, the whole algorithm is still
$O\left(\left|T\right|\left|P\right|\right)$, but in the average case the
runtime is $O\left(\left|T\right|\right)$, performing best when the alphabet is
large.

## Knuth-Morris-Pratt

This algorithm prepares a table of prefix-suffixes of the prefixes of the
pattern. A prefix-suffix is the length of the longest strict prefix of a string
that is also a suffix of the same string. For example, in the string "abcab",
the value is 2, as "ab" is a strict prefix and suffix.

The search algorithm then works without backtracking of the text. In the case
of a mismatch, the algorithm searches earlier in the pattern, using the suffix
of the string that has already been matched as the new part of the
already-searched prefix.

This algorithm has runtime $O\left(\left|T\right|)$, since the prefix-table
takes $O\left(P\right)$ to build, and running the algorithm takes
$O\left(\left|T\right|)$ time.
