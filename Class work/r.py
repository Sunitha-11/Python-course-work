s="python programming"
changestr=list(map(lambda i: i.upper(),s))
print(changestr)
"""['P', 'Y', 'T', 'H', 'O', 'N', ' ', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']"""

#
s="python programming"
asci=list(map(lambda i: ord(i),s))
print(asci)
"""[112, 121, 116, 104, 111, 110, 32, 112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]"""



vowel="python programming"
frmt=list(map(lambda i:"*" if i in vowel else "0" ,s))
print(frmt)