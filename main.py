print('Hello, Mario World!')

# curl http://localhost:11434/api/chat -d '{
#   "model": "mario",
#   "messages": [
#     { "role": "user", "content": "马里奥和奥特曼会发生什么故事？" }
#   ],
#   "stream": false
# }'

# curl http://localhost:11434/api/chat -d '{
#   "model": "yi",
#   "messages": [
#     { "role": "user", "content": "翻译为中文: Well, you know, it\u0027s always an adventure when me and my brother Luigi team up! One time, we were in the Mushroom Kingdom and heard that Bowser had kidnapped Princess Peach again. So we set off on our quest to rescue her. We traveled through various worlds, each with its own unique challenges. We jumped over pits, defeated Goombas, and collected Power Stars or Power Mushrooms along the way. But every time we reached Bowser\u0027s Castle, he would be waiting for us with his Koopa Troop by his side.Despite the challenges, we never gave up! With teamwork and determination, we managed to save Princess Peach and send Bowser packing. After that, we returned to the Mushroom Kingdom as heroes, celebrated with the people, and looked forward to our next adventure together.Isn\u0027t it wonderful how we always stand by each other\u0027s side in times of need? That\u0027s what being brothers is all about!" } ],
#   "stream": false
# }'

import requests
import json

# 定义请求的 URL
url = 'http://localhost:11434/api/chat'

# 提示用户输入 content 马里奥和奥特曼的故事
user_input = input("Please enter the content for the message: ")

# 定义请求的数据
data = {
  "model": "mario",
  "messages": [
    { "role": "user", "content": user_input }
  ],
  "stream": False
}

# 将数据转换为 JSON 格式
json_data = json.dumps(data)

# 发送 POST 请求
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# 输出响应内容
response_json = response.text
# print(response_json)

# 解析 JSON 数据
data = json.loads(response_json)

# 提取 "message" 中 "role" 为 "assistant" 的 "content"
assistant_content = data['message']['content']

# 打印 "content" 内容
print(assistant_content)

# 使用 str.replace() 方法替换单引号
replaced_string = assistant_content.replace("'", "\\u0027")

# 打印替换后的字符串
# print(replaced_string)

# 使用yi翻译为中文 定义请求的数据
data = {
  "model": "yi",
  "messages": [
    { "role": "user", "content": "翻译为中文: " + replaced_string }
  ],
  "stream": False
}

# 将数据转换为 JSON 格式
json_data = json.dumps(data)

# 发送 POST 请求
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# 输出响应内容
response_json = response.text
print(response_json)