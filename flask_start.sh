# sudo su
# cd chatbot
PYTHONPATH=/home/ubuntu/chatbot
export FLASK_APP=flaskback.main
export FLASK_ENV=development
nohup /home/ubuntu/miniconda3/envs/chatbot/bin/flask run --host=0.0.0.0 --port=80 > nohup.out 2>&1 &

