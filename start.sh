# sudo bash chatbot/start.sh
sudo su
cd /home/ubuntu/chatbot
nohup ../miniconda3/envs/chatbot/bin/python -u main.py 80 > nohup.out 2>&1 &
exit