import requests

BASE = "http://127.0.0.1:5000/" 

data = [{"name":"firstvid", "views":10, "likes":10},
      {"name":"secondvid", "views":20, "likes":20},
      {"name":"thirdvid", "views":30, "likes":30}]


for i in range(len(data)):  
    response = requests.put(BASE + "video/" + str(i), data[i] )
    print (response.json()) 

input()


response = requests.get(BASE + "video/2")
print (response.json())

input ()
response = requests.patch(BASE + "video/2", {"views": 100})
print (response.json())
