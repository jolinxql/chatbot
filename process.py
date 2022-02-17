"""
@time       : 2021/8/19 12:58 上午
@author     : JolinXia
@description:
    
"""
import logging

from protos import reply


def process(recMsg, bot):
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    # TODO: Redis read history
    if recMsg.MsgType == 'image':
        replyMsg = reply.TextMsg(toUser, fromUser, "拒绝斗图！（其实就是想省流量）")
        # TODO: OCR
        mediaId = recMsg.MediaId
        # replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
    elif recMsg.MsgType == 'text':
        if recMsg.Content == 'test':
            content = str(recMsg)
        else:
            content = bot.predict(recMsg.Content)
        replyMsg = reply.TextMsg(toUser, fromUser, content)
    elif recMsg.MsgType == 'voice':
        content = bot.predict("我给你发语音")
        replyMsg = reply.TextMsg(toUser, fromUser, content)
        # TODO: Voice Recognition
        mediaId = recMsg.MediaId
        # replyMsg = reply.TextMsg(toUser, fromUser, content)
    elif recMsg.MsgType == 'location':
        content = bot.predict("这是我的地址")
        replyMsg = reply.TextMsg(toUser, fromUser, content)
        # TODO: Location Recognition
        # replyMsg = reply.TextMsg(toUser, fromUser, content)
    else:
        content = recMsg.Content
        logging.info(content)
        replyMsg = reply.TextMsg(toUser, fromUser, content)  # "消息类型未知"

    return replyMsg
