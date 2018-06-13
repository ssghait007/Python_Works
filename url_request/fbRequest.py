import requests, time
r = requests.post('https://requestb.in/q9zwn6qa', data={"ts":time.time()})
print r.status_code
print r.content
