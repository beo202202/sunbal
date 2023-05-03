import json

# JSON 파일 읽기
with open('data.json') as file:
    data = json.load(file)

# Python 객체 출력
print(data)
print(type(data))

