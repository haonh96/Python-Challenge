import requests
import re
#get source index.html
r = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
#get text in comment <!---->
#Tuy chon voi co re.DOTTAL nham regex ca xuong dong.
text = re.findall("<!--(.*?)-->", r.content, re.DOTALL)[-1]

#Tim cac ky tu thoa man dieu kien la 1 chu thuong duoc bao boc ben ngoai bang 3 chu hoa
output = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",text,re.DOTALL)
result =""
for i in output:
	result += i
print "KQ: "+result