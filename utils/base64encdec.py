"""
@time       : 2021/9/3 10:15 上午
@author     : JolinXia
@description:
    
"""
import base64


def ToBase64(file, txt):
    """ ToBase64("./desk.jpg", 'desk_base64.txt')  # 文件转换为base64
    :param file:
    :param txt:
    :return:
    """
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def ToFile(txt, file):
    """ ToFile("./desk_base64.txt", 'desk_cp_by_base64.jpg')  # base64编码转换为二进制文件
    :param txt:
    :param file:
    :return:
    """
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()
