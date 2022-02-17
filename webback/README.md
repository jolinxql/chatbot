### Bot环境配置
Ubuntu 20.04 LTS
``` bash
sudo apt update
sudo apt install python3-webpy
sudo apt install python3-pip
sudo apt install libxml2-dev libxslt1-dev
curl --output conda_.sh https://repo.anaconda.com/miniconda/Miniconda3-
latest-Linux-x86_64.sh
bash conda_.sh

# logout & login
conda create -n chatbot python=3.8
conda activate
pip install transformers==4.2.0 web.py tensorboard
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cpuonly -c pytorch
```
vi .git/config修改为
url = ssh://git@github.com/jolinxql/chatbot.git

### Redis部署
```bash
mkdir tools
cd tools~~~~
wget https://download.redis.io/releases/redis-6.2.5.tar.gz
tar -xzvf redis-6.2.5.tar.gz
cd redis-6.2.5
sudo make
sudo make test
sudo make install
```
修改配置
vi redis.conf
```
# 启用密码
requirepass chatbot
# 后台运行
daemonize yes
:wq
```
启动服务
``` bash
redis-server redis.conf
redis-cli -a chatbot
```
检查连通
127.0.0.1:6379> ping
PONG

### 启动bot
sudo bash chatbot/start.sh
### 停止bot
sudo bash chatbot/stop.sh