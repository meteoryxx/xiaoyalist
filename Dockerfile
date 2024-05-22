# 使用官方的Python运行时作为父镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖项
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# 将当前目录内容复制到容器的/app目录
COPY . /app

# 安装Python依赖项
RUN pip install --no-cache-dir flask requests ping3 schedule

# 暴露端口
EXPOSE 5000

# 运行Flask应用
CMD ["python", "app.py"]