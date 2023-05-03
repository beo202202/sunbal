import requests

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=data)
print(response.text)

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.text)
