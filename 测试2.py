

import re
from  urllib import request
url="https://www.sqlsec.com/"

request=request.urlopen(url)
html=request.read().decode('utf-8')
img=re.compile('<img src="(.*?)".*?>')
items=re.findall(img,html)
for item in items:
    print(item)

list=img.findall(html)

n=0
for i in list:
    request.urlretrieve("https:"+i,"%s.jpg" % n)
    print('download %s' % i)
    n+=1


