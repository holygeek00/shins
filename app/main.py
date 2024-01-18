# FastAPI application main file.

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app import models  # 导入您的模型
from app.api.api_v1.endpoints import user, item, token  # 导入您的路由

app = FastAPI()

# 示例路由
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# 包含您的API路由
app.include_router(user.router)
app.include_router(item.router)
app.include_router(token.router)

# Tortoise-ORM 配置
register_tortoise(
    app,
    db_url="mysql://root:mysql@Shensi2024@localhost/ShenSiDB",  # 根据您的数据库配置进行修改
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
