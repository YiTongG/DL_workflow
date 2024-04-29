# 使用官方的 Python 基础镜像
FROM python:3.8-slim

# 安装依赖
RUN pip install flask tensorflow

# 设置工作目录
WORKDIR /app

# 复制推理脚本
COPY inference.py /app/

# 暴露端口
EXPOSE 5000

# 容器启动时运行推理脚本
CMD ["python", "inference.py"]

