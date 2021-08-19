
sudo apt update

``` bash
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

cd chatbot
sudo su
nohup ../miniconda3/envs/chatbot/bin/python -u main.py 80 > nohup.out 2>&1 &

# 端口冲突时，查看本机python的进程
kill $(ps aux | grep "main.py 80" | grep -v grep | awk '{ print $2 }')

```
vi .git/config修改为
url = ssh://git@github.com/jolinxql/chatbot.git