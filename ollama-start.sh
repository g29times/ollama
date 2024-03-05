### 第一步 安装、更新环境
# cd /teamspace/studios/ollama
cd /teamspace/studios/this_studio
curl -fsSL https://ollama.com/install.sh | sh

### 2 启动服务
nohup ollama serve > /teamspace/studios/this_studio/ollama-serve.log 2>&1 &