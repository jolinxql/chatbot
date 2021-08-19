"""
@time       : 2021/8/19 12:39 上午
@author     : JolinXia
@description:
    
"""
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


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.Content = "Msg"

    def __str__(self):
        return "to:%s\nfrom:%s\ntime:%s\ntype:%s\n" % (self.ToUserName, self.FromUserName,
                                                       self.CreateTime, self.MsgType)


class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.Content = xmlData.find('Content').text

    def __str__(self):
        return super().__str__() + "\nmsgid:%s\ncontent:%s" % (self.MsgId, self.Content)


class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
        self.Content = xmlData.find('MediaId').text

    def __str__(self):
        return super().__str__() + "\nmsgid:%s\npicurl:%s\nmediaid:%s" % (self.MsgId, self.PicUrl, self.MediaId)
