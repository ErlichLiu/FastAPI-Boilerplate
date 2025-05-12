import os
import sys
import logging
import colorlog
from config.app_config import LOGGER_CONFIG
from logging.handlers import RotatingFileHandler


def setup_logger(name = None, level = None):
    """
    设置并返回一个带有彩色输出的日志记录器
    
    Args:
        name: 日志记录器名称
        level: 日志级别
    
    Returns:
        配置好的日志记录器实例
    """
    # 使用传入的参数或配置中的默认值
    name = name or LOGGER_CONFIG["name"]
    level = level or LOGGER_CONFIG["level"]
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 如果已经有处理器，不再添加新的处理器
    if logger.handlers:
        return logger
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    
    # 创建彩色格式化器
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        }
    )
    
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 根据配置决定是否添加文件处理器
    if LOGGER_CONFIG["log_to_file"]:
        # 确保日志目录存在
        log_file_path = LOGGER_CONFIG["log_file_path"]
        log_dir = os.path.dirname(log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # 创建文件处理器
        if LOGGER_CONFIG["log_file_rotation"]:
            file_handler = RotatingFileHandler(
                log_file_path,
                maxBytes=LOGGER_CONFIG["max_bytes"],
                backupCount=LOGGER_CONFIG["backup_count"]
            )
        else:
            file_handler = logging.FileHandler(log_file_path)
        
        file_handler.setLevel(LOGGER_CONFIG["log_file_level"])
        
        # 为文件处理器创建格式化器（不带颜色）
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger


def setup_uvicorn_logger():
    """
    配置 uvicorn 日志，使其与应用日志风格一致
    """
    # 创建彩色格式化器
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        }
    )
    
    # 配置 uvicorn 主日志
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.handlers.clear()
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    uvicorn_logger.addHandler(console_handler)
    
    # 配置 uvicorn 访问日志
    access_logger = logging.getLogger("uvicorn.access")
    access_logger.handlers.clear()
    
    access_console_handler = logging.StreamHandler()
    access_console_handler.setFormatter(formatter)
    access_logger.addHandler(access_console_handler)


# 创建默认日志记录器实例，可以直接导入使用
logger = setup_logger()
