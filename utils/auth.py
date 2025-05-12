import os
from dotenv import load_dotenv
from utils.logger import setup_logger
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# 设置 Logger
logger = setup_logger(name="Auth")

# 加载环境变量
load_dotenv()

# 从环境变量获取 API Key
API_KEY = os.getenv("API_KEY")

# 如果环境变量中没有设置 API Key，则抛出错误
if not API_KEY:
    logger.critical("API_KEY 环境变量未设置,请到 .env 内进行设置")
    raise ValueError("API_KEY 环境变量未设置")

# 创建 Bearer 认证工具
security = HTTPBearer()

# API Key 验证函数
async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    验证请求中的 Bearer token 是否与环境变量中设置的 API Key 匹配
    
    Args:
        credentials: 从请求中提取的认证凭据
        
    Returns:
        str: 验证通过的 API Key
        
    Raises:
        HTTPException: 如果认证失败则抛出 401 错误
    """
    if credentials.scheme.lower() != "bearer":
        logger.warning("认证方案无效，验证失败，请留意！")
        raise HTTPException(
            status_code=401,
            detail="认证方案无效，请使用 Bearer 认证"
        )
    
    if credentials.credentials != API_KEY:
        logger.warning("遇到无效的 api key, 请留意")
        raise HTTPException(
            status_code=401,
            detail="无效的 API Key"
        )
    
    return credentials.credentials
