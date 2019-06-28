import requests
import time


start = time.time()

for i in range(10):
	url = 'http://www.httpbin.org/get'
	response = requests.get(url)

print(time.time()-start)