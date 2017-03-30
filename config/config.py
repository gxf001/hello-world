from singleton import Singleton
from typing import List

import os
import json

from logger import get_logger

logger = get_logger(__name__)


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self) -> None:
        """Initialize the Config class"""
        self.openai_api_key = os.environ.get('OPENAI_API_KEY')
        
        # 读取配置文件
        with open("./config/common-config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
            
        logger.info("数据库地址:%s", config["database"]["host"])
        logger.info("数据库端口:%s", config["database"]["port"])
        logger.info("数据库用户名:%s", config["database"]["user"])
        logger.info("数据库密码:%s", config["database"]["password"])
        logger.info("数据库名称:%s", config["database"]["database"])
        logger.info("openai_api_key:%s", self.openai_api_key)
            
        
 