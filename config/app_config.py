"""
应用配置模块，包含 FastAPI 应用的各种配置项
"""

from typing import Dict, Any
import logging

# FastAPI 应用配置
FASTAPI_CONFIG: Dict[str, Any] = {
    "title": "Your project name",
    "description": "Your project description",
    "version": "0.1.0",
    # 禁用自动生成的文档服务在外部访问，可以根据需求修改
    "docs_url": None,  # 禁用 Swagger UI
    "redoc_url": None,  # 禁用 ReDoc
}

# CORS 配置
CORS_CONFIG: Dict[str, Any] = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

# 服务器配置
SERVER_CONFIG: Dict[str, Any] = {"host": "0.0.0.0", "port": 8000, "reload": True}

# Logger 配置
LOGGER_CONFIG: Dict[str, Any] = {
    "name": FASTAPI_CONFIG["title"],
    "level": logging.INFO,
    "log_to_file": False,  # 是否将日志写入文件
    "log_file_path": "logs/app.log",  # 日志文件路径
    "log_file_level": logging.INFO,  # 文件日志级别
    "log_file_rotation": True,  # 是否启用日志轮转
    "max_bytes": 10 * 1024 * 1024,  # 单个日志文件最大大小（10MB）
    "backup_count": 5,  # 保留的备份文件数量
}
