import requests
import re
link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
number ='12345'
while (1):
	visit = link + number
	print "try :" +visit
	r = requests.get(visit)
	print r.content
	if("Yes. Divide by two and keep going" in r.content):
		print "number Divide "+ number
		number = str(int(number)/2)
		continue
	if("nothing" not in r.content):
		print r.content
		break
	else:
		number = "".join(re.findall("([0-9])",r.content))


	