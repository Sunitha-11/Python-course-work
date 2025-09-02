#re.match
import re
pattern=r"\d"
res=re.match(pattern,"1hello world")
print(res.group() if res else"No match")    #output=1

#re.search
import re
pattern=r"\d"
res=re.search(pattern,"hello world38")
print(res.group() if res else"No match")      #output=3

import re
pattern=r"[aeiou]"
res=re.search(pattern,"hello world")
print(res.group() if res else"No match")       #output=e

pattern=r"[A-Z]"
res=re.search(pattern,"Hello world")
print(res.group() if res else"No match")     #opt=H

#re.findall
pattern=r"[aeiou]"
res=re.findall(pattern,"hello world")
print(res)        #opt=['e', 'o', 'o']


pattern=r"\d{4}|\d{2}"
res=re.findall(pattern,"pfs-31 2025 pfs-14 2024 pfs-10 2023")
print(res)    #opt=['31', '2025', '14', '2024', '10', '2023']


#re.finditer
pattern=r"\d{4}|d{2}"
res=re.finditer(pattern,"2023")
for i in res:
    print(i.group(),i.start())    #opt=2023 0


#re.fullmatch
pattern=r"\d{10}"
res=re.fullmatch(pattern,"8106735528")
print(res.group() if res else"No match")    #opt=8106735528



#re.sub
pattern=r"[aetou]"
res=re.sub(pattern,"*","Python programming language")
print(res)     #opt=Py*h*n pr*gr*mming l*ng**g*




#res.split
pattern=r"[:,0]"
res=re.split(pattern,"Python,programming:lang0uage")
print(res)     #['Python', 'programming', 'lang', 'uage']


#re.findall(.)
pattern=r"h.t"
res=re.findall(pattern,"hot hit hat")
print(res)   #opt=['hot', 'hit', 'hat']

pattern=r"...d"
res=re.findall(pattern,"hood wood food")
print(res)    #opt=['hood', 'wood', 'food']

