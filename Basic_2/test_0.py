import requests
BASE = "http://127.0.0.1:5000/"

# for test_1.py
# response = requests.put(BASE + "video/1", {"likes":10, "views":15, "name":"vinayak"})
# print(response.json())


# for test_2.py
# response = requests.put(BASE + "video/1", {"likes":10, "views":15,})
# response = requests.put(BASE + "video/1", {"likes":10, "views":15, "name":"vinayak"})
# print(response.json())

# for test_3.py
# response = requests.put(BASE + "video/1", {"likes":10, "views":15, "name":"vinayak"})
# print(response.json())
# input()
# response = requests.get(BASE+"video/1")
# print(response.json())


# for test_4.py
response = requests.get(BASE + "video/1")
print(response.json())