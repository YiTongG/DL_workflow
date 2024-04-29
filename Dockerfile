# 使用官方的 Python 基础镜像
FROM python:3.8

# 工作目录设置为 /app
WORKDIR /app

# 复制所有需要的文件到容器内
COPY . /app

# 安装 Python 依赖
RUN pip install tensorflow

# 运行训练脚本
CMD ["python", "train.py"]

