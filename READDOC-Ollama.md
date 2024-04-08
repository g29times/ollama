# Docs
https://github.com/ollama/ollama?tab=readme-ov-file
## models: gpt2, llama, vicuna, alpaca, chatglm
https://ollama.com/library  
## api
https://github.com/ollama/ollama/blob/main/docs/api.md


# Commands
## help
/?
## 方式一 启动脚本
bash /teamspace/studios/this_studio/ollama-start.sh
## 方式二 逐步设置 Setup & Use
### 1 第一步 安装、更新环境
curl -fsSL https://ollama.com/install.sh | sh
### 2 启动服务
ollama serve
### 3 【新开terminal】下载并运行模型 | 改名
ollama run [model] | /save [name]
### 4 创建及刷新 定制模型 建议每次使用
ollama create [model] -f ./[ModelfilePath] | ollama create xizhao -f ./modelfiles/Modelfile_XiZhao
### 5 模型列表 | 更新模型(从远程) | 删除本地模型
ollama list | ollama pull | ollama rm [model]


# Tests
## 如何测试
1 直接使用LM进行对话 ollama run [model]
2 使用main.py进行复杂对话
3 使用streamlit进行web交互
## 启动 Streamlit
streamlit run --server.port 8501 streamlit.py
## Cases
1 Hi Mario!(role play)
2 
3 
## Aspects 
维度                     0 资源 1 速度 2 语言 3 逻辑 4 创意 5 特点 
## Levels
1较 2很 3极 | 1无(不会) 2差 3可 4好 5佳
### 7b- (need 8G GPU)
- yi (BEST Lamma 6b q4)  资源低 速度快 中文佳 逻辑好 创意无 中文突出
- mistral:instruct(L7bq4)资源中 速度慢 中文可 逻辑好 创意好 平衡好用
- gemma:7b(gemma 9b q4)  资源中 速度慢 不会中 逻辑好 创意佳 角色扮演
- phi-2(phi2 3b q4)      资源低 速度慢 中文差 逻辑可 创意差 废话连篇
- qwen(qwen2 4b q4)      较差
- tinyllama( )           较差
- llava(llama clip 7b q4)                                视觉
- codellama( )                                           代码
- neural-chat( )                                         对话
- falcon( )              
- openchat(llama 7b q4)                                  对话
### 7b~13b (need 16G GPU)

### 13b~33b
- command-r(command-r 35b q4)                            RAG
### 33b+ (need 32G GPU)
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


# WEBUI
## docs
https://github.com/open-webui/open-webui#troubleshooting
https://docs.openwebui.com/getting-started/#installing-docker
https://openwebui.com/

## install
### docker
sudo apt-get install ca-certificates curl

sudo install -m 0755 -d ./etc/apt/keyrings

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o ./etc/apt/keyrings/docker.asc
sudo chmod a+r ./etc/apt/keyrings/docker.asc

sudo mkdir -p ./etc/apt/sources.list.d/
sudo touch ./etc/apt/sources.list.d/docker.list

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=./etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee ./etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
检查 docker
sudo docker run hello-world
正常返回：Hello from Docker!

### ollama
检查 ollama
curl http://127.0.0.1:11434/
正常返回：Ollama is running

启动 webui 端口8080
docker run -d --name ollama-webui --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --restart always ghcr.io/open-webui/open-webui:main

curl http://localhost:8080