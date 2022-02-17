# sudo bash chatbot/stop.sh
sudo su
kill $(ps aux | grep "flask" | grep -v grep | awk '{ print $2 }')
exit