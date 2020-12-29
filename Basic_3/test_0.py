import requests
BASE = "http://127.0.0.1:5000/"


# for test_1.py
# data = [{"likes":10, "views":150, "name":"cpp"},
#        {"likes":20, "views":200, "name":"java"},
#        {"likes":30, "views":300, "name":"python"}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())


# input()
# # response = requests.get(BASE+"video/2")
# response = requests.get(BASE+"video/6")
# print(response.json())

# for test_2.py
# response = requests.patch(BASE+"video/2", {"views":99})
response = requests.patch(BASE+"video/2", {"views": 99, "likes": 500})
print(response.json())
