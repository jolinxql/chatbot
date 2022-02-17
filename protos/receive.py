"""
@time       : 2021/8/19 12:39 上午
@author     : JolinXia
@description:
    
"""
import logging
import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    elif msg_type == 'voice':
        return VoiceMsg(xmlData)
    else:
        logging.info("msg_type: %s" % msg_type)
        return Msg(xmlData, ET.tostring(xmlData, method='xml').decode())


class Msg(object):
    def __init__(self, xmlData, content=""):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.Content = content if content else str(xmlData)

    def __str__(self):
        return "to:%s\nfrom:%s\ntime:%s\ntype:%s\n" % (self.ToUserName, self.FromUserName,
                                                       self.CreateTime, self.MsgType)


class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.Content = xmlData.find('Content').text

    def __str__(self):
        return super().__str__() + "\nMsgId:%s\nContent:%s" % (self.MsgId, self.Content)


class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
        self.Content = xmlData.find('MediaId').text

    def __str__(self):
        return super().__str__() + "\nMsgId:%s\nPicUrl:%s\nMediaId:%s" % (self.MsgId, self.PicUrl, self.MediaId)


class VoiceMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.MediaId = xmlData.find('MediaId').text
        self.Format = xmlData.find('Format').text
        self.Recognition = xmlData.find('Recognition').text
        self.Content = xmlData.find('MediaId').text

    def __str__(self):
        return super().__str__() + "\nMsgId:%s\nMediaId:%s\nFormat:%s\nRecognition:%s" % (
        self.MsgId, self.MediaId, self.Format, self.Recognition)


class LocationMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.Location_X = xmlData.find('Location_X').text
        self.Location_Y = xmlData.find('Location_Y').text
        self.Scale = xmlData.find('Scale').text
        self.Recognition = xmlData.find('Label').text

    def __str__(self):
        return super().__str__() + "\nmsgid:%s\nLocation_X:%s\nLocation_Y:%s\nScale:%s\nLabel:%s" % (
        self.MsgId, self.Location_X, self.Location_Y, self.Scale, self.Recognition)
