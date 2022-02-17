"""
@time       : 2021/8/24 12:25 上午
@author     : JolinXia
@description:
    
"""
import hashlib

from flask import Flask, request

import process
from chatbot import Bot
from protos import receive
from utils import helper
import logging

app = Flask(__name__)
token = helper.load_json("conf/token_private.json")["token"]
bot_conf = helper.load_json("conf/bot.json")
bot = Bot(bot_conf)

hyper_conf = helper.load_json("conf/hyper.json")  # 满足动态调试
logger = helper.log_config(hyper_conf['logfile'])


@app.route("/wx", methods=['GET', 'POST'])
def process_wx():
    hyper_conf = helper.load_json("conf/hyper.json")  # 满足动态调试
    if request.method == 'POST':
        req_data = request.data

        recMsg = receive.parse_xml(req_data)
        if hyper_conf['print_req_content']:
            logger.info(recMsg.Content)

        replyMsg = process.process(recMsg, bot)
        if hyper_conf['print_resp_content']:
            logger.info(replyMsg.Content)

        return replyMsg.send()
    else:
        hyper_conf = helper.load_json("conf/hyper.json")  # 满足动态调试
        if hyper_conf['print_req']:
            logger.info(request.args)
        signature = request.args['signature']
        timestamp = request.args['timestamp']
        nonce = request.args['nonce']
        echostr = request.args['echostr']

        sort_list = [token, timestamp, nonce]
        sort_list.sort()
        sha1 = hashlib.sha1()
        sha1.update("".join(sort_list).encode("utf-8"))
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr
        else:
            return ""


@app.route("/test", methods=['GET'])
def process_test():
    for k in request.args.keys():
        logger.info(k + ":" + str(request.args[k]) + "\n")
    return "test passed"
