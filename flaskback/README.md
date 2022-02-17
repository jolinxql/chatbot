# follow README.md from parent folder, then
pip install flask
sudo su
PYTHONPATH=/home/ubuntu/chatbot
export FLASK_APP=flaskback.main
export FLASK_ENV=development
/home/ubuntu/miniconda3/envs/chatbot/bin/flask run  --host=0.0.0.0 --port=80
