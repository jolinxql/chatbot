"""
@time       : 2021/8/24 12:54 上午
@author     : JolinXia
@description:
    
"""

import json
import logging
import time
import re
from logging.handlers import TimedRotatingFileHandler


def load_json(f):
    with open(f) as fin:
        obj = json.load(fin)
    return obj


def log_config(logfile):
    LOG_FORMAT = "[%(asctime)s][%(levelname)s]: %(message)s"
    level = logging.DEBUG
    logging.basicConfig(level=level, format=LOG_FORMAT)

    # 创建TimedRotatingFileHandler对象,每天生成一个文件
    log_file_handler = TimedRotatingFileHandler(filename=logfile, when="midnight", interval=1, backupCount=3)
    # 设置日志文件后缀，以当前时间作为日志文件后缀名。
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    logger = logging.getLogger()
    logger.addHandler(log_file_handler)
    return logger
