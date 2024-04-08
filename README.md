# 文件结构说明
DEPRECATED:
    main.py 
    lit.py  尝试支持记忆版bot
    omni.py 多助手版
LOCAL:
    ollama-main.py 本地运行LM对话DEMO
DEV:
    debug.py 
    dev.py 
    multibots.py 多模型切换
PROD:
    llm.py LM基础访问功能封装
    streamlit.py streamlit客户端



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

检查 ollama
curl http://127.0.0.1:11434/
正常返回：Ollama is running

启动 webui 端口8080
docker run -d --name ollama-webui --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --restart always ghcr.io/open-webui/open-webui:main

curl http://localhost:3000