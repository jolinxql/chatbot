# sudo bash chatbot/stop.sh
sudo su
kill $(ps aux | grep "main.py 80" | grep -v grep | awk '{ print $2 }')
exit