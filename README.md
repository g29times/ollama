# 文件结构说明
LOCAL：main.py debug.py
DEV：lit.py 尝试支持记忆版bot
PROD：streamlit.py llm.py

# Models
https://ollama.com/library  
classic models: gpt2, llama, vicuna, alpaca, chatglm

# Ref
https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/
https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu
https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
# Code
https://streamlit.io/gallery?category=llms
https://github.com/dataprofessor/llama2/blob/master/streamlit_app.py
https://github.com/streamlit/llm-examples/blob/main/Chatbot.py
https://blog.csdn.net/weixin_42608414/article/details/128916767
https://blog.csdn.net/hugo_lei/article/details/135901123
# Docs
https://github.com/ollama/ollama?tab=readme-ov-file

## set & use
ollama create mario -f ./Modelfile
ollama list
ollama run mario
## help
/?
## download & run model
ollama run [model]
## api
https://github.com/ollama/ollama/blob/main/docs/api.md

# Tests
## cases
1 Hi(with system role)
2 comment on the value of paper "attention is all you need" to ChatGPT in Chinese
3 Attention Is All You Need 对ChatGPT的影响是什么
# levels
极 很 较 极 | 不会 错 差 可 好 佳
# aspects 
维度 1 速度 2 多语言 3 角色 4 理解 5 数理
# results
- yi 较快 中文佳(BEST) 角色差
- mistral:instruct 很慢 中文可 角色好
- gemma:7b 很慢 不会中文 角色较好
- phi-2 慢 中文差、错
