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
# response = requests.get(BASE + "video/1")
# print(response.json())


# for test_5.py
data = [{"likes": 10, "views": 150, "name": "cpp"},
        {"likes": 20, "views": 200, "name": "java"},
        {"likes": 30, "views": 300, "name": "python"}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE+"video/2")
print(response.json())
