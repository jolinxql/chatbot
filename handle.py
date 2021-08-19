"""
@time       : 2021/8/19 12:37 上午
@author     : JolinXia
@description:
    
"""
import hashlib
import json

import web

import process
import receive
from chatbot import Bot


def load_json(f):
    with open(f) as fin:
        obj = json.load(fin)
    return obj


token = load_json("conf/token.json")["token"]
bot_conf = load_json("conf/bot.json")
bot = Bot(bot_conf)


class Handle(object):
    def __init__(self):
        global bot, token
        self.bot = bot
        self.token = token

    def GET(self):
        try:
            data = web.input()
            hyper_conf = load_json("conf/hyper.json")  # 满足动态调试
            if hyper_conf['print_req']:
                print(data)
            if len(data) == 0:
                return "data in GET is empty"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = self.token

            sort_list = [token, timestamp, nonce]
            sort_list.sort()
            sha1 = hashlib.sha1()
            sha1.update("".join(sort_list).encode("utf-8"))
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            print("exception", Argument)
            return Argument

    def POST(self):
        try:
            webData = web.data()
            hyper_conf = load_json("conf/hyper.json")  # 满足动态调试

            if hyper_conf['print_req']:
                print("Handle Post webdata is ", webData)

            recMsg = receive.parse_xml(webData)
            if hyper_conf['print_req_content']:
                print(recMsg.Content)

            replyMsg = process.process(recMsg, self.bot)
            if hyper_conf['print_resp_content']:
                print(replyMsg.Content)

            return replyMsg.send()
        except Exception as Argument:
            print("exception", Argument)
            return Argument
