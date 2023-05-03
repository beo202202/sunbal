import json

# JSON 파일 읽기
with open('data.json') as file:
    data = json.load(file)

print(data['employee'])
print(data['employee']['name'])
print(data['employee']['salary'])
