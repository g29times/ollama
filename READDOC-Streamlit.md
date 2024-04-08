# 官方
https://github.com/streamlit/llm-examples/blob/main/Chatbot.py


# 分享
探索新Ollama Python库：在应用程序中集成本地LLM  https://zhuanlan.zhihu.com/p/679893306


# 结合Ollama使用
关键过程
1 import streamlit
2 使用 requests.post(url='http://localhost:11434/api/chat' 调用Ollama模型
3 使用 st.chat_message展示对话UI