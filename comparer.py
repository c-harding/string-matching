class Comparer:
   count = 0

   def __call__(self, text, i, pattern, j=0):
       print(' '*(j-i) + text)
       print(' '*(i-j) + pattern)
       print(' '*(max(i,j)) + '^')
       self.count += 1
       return text[i] == pattern[j]
