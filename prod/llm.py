# LLM主程序 参考 https://github.com/ollama/ollama/blob/main/docs/api.md
import requests
import json

def send_chat_request(model, user_input):
    # 我们故意抛出一个异常来测试异常处理
    if user_input == "error":
        raise ValueError("Intentional error to test exception handling.")
    # 如果没有异常，返回一个正常的回答

    # 定义请求的 URL
    url = 'http://localhost:11434/api/chat'
    
    print("\n user_input: " + user_input)

    # 定义请求的数据
    data = {
        "model": model,
        "messages": [
            { "role": "user", "content": user_input }
            # , { "role": "system", "content": "" }
        ],
        "stream": False
    }

    # 将数据转换为 JSON 格式
    json_data = json.dumps(data)
    
    print(json_data)
    print(url)

    # 发送 POST 请求
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    # 输出响应内容
    response_json = response.text
    print("Response: " + response_json)

    # 解析 JSON 数据
    data = json.loads(response_json)

    # 提取 "message" 中 "role" 为 "assistant" 的 "content"
    assistant_content = data['message']['content']

    # 打印 "content" 内容
    # print("ORIGIN RESPONSE ---> " + assistant_content)

    if model != "mario":
        return assistant_content
    else:
        # 使用 str.replace() 方法替换单引号
        replaced_string = assistant_content.replace("'", "\\u0027")

        # 打印替换后的字符串
        # print(replaced_string)

        # 使用yi翻译为中文 定义请求的数据
        data = {
            "model": "yi",
            "messages": [
                { "role": "system", "content": "你是一个翻译机器人，将输入的内容翻译为中文输出，一些罕见的人名和特殊名词可以不做翻译，保留原文" },
                { "role": "user", "content": replaced_string }
            ],
            "stream": False
        }

        # 将数据转换为 JSON 格式
        json_data = json.dumps(data)
        # print(json_data)

        # 发送 POST 请求
        response2 = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

        # 输出响应内容
        response_json2 = response2.text

        # 解析 JSON 数据
        data = json.loads(response_json2)

        # 提取 "message" 中 "role" 为 "assistant" 的 "content"
        assistant_content = data['message']['content']

        # 返回响应内容
        return assistant_content

# TEST 运行streamlit时 需要注释
# user_content = input("Please enter the content for the message: ")
# response_text = send_chat_request("mario", user_content)

# # 打印返回的响应内容
# print(response_text)