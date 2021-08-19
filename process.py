"""
@time       : 2021/8/19 12:58 上午
@author     : JolinXia
@description:
    
"""
import reply


def process(recMsg, bot):
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    # TODO: Redis read history
    if recMsg.MsgType == 'image':
        mediaId = recMsg.MediaId
        replyMsg = reply.TextMsg(toUser, fromUser, "拒绝斗图！（其实就是想省流量）")
        # TODO: OCR
        # replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
    elif recMsg.MsgType == 'text':
        if recMsg.Content == 'test':
            content = str(recMsg)
        elif bot is None:
            content = "我是机器人"
        else:
            content = bot.predict(recMsg.Content)
        replyMsg = reply.TextMsg(toUser, fromUser, content)
    else:
        replyMsg = reply.TextMsg(toUser, fromUser, "消息类型未知")

    return replyMsg
