import requests
BASE = "http://127.0.0.1:5000/"

# for test_1.py
# response = requests.post(BASE + "helloworld")
response = requests.get(BASE + "helloworld")
print(response.json())

# for test_2.py
# response = requests.get(BASE+"helloworld/vinayak/20")
# print(response.json())

# for test_3.py
# response = requests.get(BASE+ "helloworld/sudhanshu")
# print(response.json())
