import re
mytext = "sads fsf dddddddddd, gddno@inbox.ru, Fffffffffff ggggggggggg Hhhhhhhhhhh dima.live dima.ru 1924 928 383u4 1765" \
         "vasya" \
         "olya" \
         "heloo"
"""
\d = Any digital 0-9
\D = Any no Digital ,.-
\w = Any alphabet symbol (A-Z a-z)
\W = Any non Alphabet symbol
\s = breakspace whitespace
\S = All non whitespace
"""

textlookfor = r"\w+\@+\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)