from urllib import request
import re
url = "https://www.ivsky.com/"
re_jpg = re.compile('<img src="(.*?)".*?>')
req = request.Request(url, headers={'User-Agent': 'Chrome/4.0 (compatible; MSIE 5.5; Windows NT)'})
response = request.urlopen(req)
html = response.read().decode('utf-8')
img_list = re_jpg.findall(html)
print(img_list)
n = 0
for i in img_list:
    request.urlretrieve("http:"+i, "%s.jpg"%n)
    print('download %s' % i)
    n+=1
