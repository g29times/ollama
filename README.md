# 文件结构说明
LOCAL：main.py debug.py
DEV：
    lit.py 尝试支持记忆版bot
    omni.py 多助手版
PROD：
    llm.py lm功能封装
    streamlit.py streamlit客户端

# Docs
https://github.com/ollama/ollama?tab=readme-ov-file
## models: gpt2, llama, vicuna, alpaca, chatglm
https://ollama.com/library  
## api
https://github.com/ollama/ollama/blob/main/docs/api.md


# Commands
## help
/?
## set & use
### 第一步 安装、更新环境
`
curl -fsSL https://ollama.com/install.sh | sh
`
### 第二步 启动服务
ollama serve
### 第三步 运行模型 download & run model
ollama run mario | ollama run [model]
### 创建定制模型
ollama create mario -f ./Modelfile
### 模型列表
ollama list


# Tests
## 如何测试
1 直接使用LM进行对话 ollama run [model]
2 使用main.py进行复杂对话
3 使用streamlit进行web交互
## cases
1 Hi Mario!(role play)
2 comment on the value of paper "attention is all you need" to ChatGPT in Chinese
3 鸡兔同笼问题
## levels
1较 2很 3极 | 1无(不会) 2差 3可 4好 5佳
## aspects 
维度                     0 资源 1 速度 2 语言 3 逻辑 4 创意 5 特点
## results
### under 7b (need 8G GPU)
- yi (BEST L6bq4)        资源低 速度快 中文佳 逻辑好 创意无 中文突出
- mistral:instruct(L7bq4)资源中 速度慢 中文可 逻辑好 创意好 平衡好用
- gemma:7b(gemma 9b q4)  资源中 速度慢 不会中 逻辑好 创意佳 角色扮演
- phi-2(phi2 3b q4)      资源低 速度慢 中文差 逻辑可 创意差 废话连篇
- qwen(qwen2 4b q4)      较差
- tinyllama( )           较差
- llava(llama clip 7b q4)视觉
- codellama( )           代码
- neural-chat( )         对话
- falcon( )              
- openchat(llama 7b q4)  对话
### under 13b (need 16G GPU)

### under 33b (need 32G GPU)
- mixtral(llama 47b q4)  资源中 速度慢 中文可 逻辑好 创意好 平衡好用


# Ref
- (https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/)
- (https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)
- (https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)

## Code
- [App Gallery](https://streamlit.io/gallery?category=llms)
- [Llama 2 Chatbot](https://github.com/dataprofessor/llama2/blob/master/streamlit_app.py)
- [ChatGPT Chatbot](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)
- [用Streamlit+LLM](https://blog.csdn.net/weixin_42608414/article/details/128916767)
- [LLM大语言模型（五）：用streamlit开发](https://blog.csdn.net/hugo_lei/article/details/135901123)
- [多模态语言模型：探索 Gemini Pro 和 Streamlit 的神奇组合](https://www.myaiexp.com/blog/ai/duo-mo-tai-yu-yan-mo)