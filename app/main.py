from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.app_config import FASTAPI_CONFIG, CORS_CONFIG
from utils.logger import setup_logger, setup_uvicorn_logger

# 配置 uvicorn 日志格式，使其与应用日志保持一致
setup_uvicorn_logger()

# 初始化 app
app = FastAPI(**FASTAPI_CONFIG)

# 配置 CORS
app.add_middleware(CORSMiddleware, **CORS_CONFIG)

# 创建 main 的 logger
logger = setup_logger(name="main")


@app.get("/")
async def test():
    logger.info("请求已经被接收，测试成功")
    return {"message": "测试成功", "status": "success"}

