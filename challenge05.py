import requests
import pickle
r = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
#load list co trong respone gui ve]
dump = pickle.loads(r.content)
#in noi dung cua mang ra
for i in dump:
	print("".join([k * v for k, v in i]))