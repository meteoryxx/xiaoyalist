# 使用官方的Python运行时作为父镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖项，包括Nginx
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# 将当前目录内容复制到容器的/app目录
COPY . /app

# 复制Nginx配置文件到Nginx默认配置目录
COPY nginx.conf /etc/nginx/nginx.conf

# 安装Python依赖项
RUN pip install --no-cache-dir flask requests  schedule 

# 暴露端口
EXPOSE 80 5000

# 启动Nginx和Flask应用
CMD ["sh", "-c", "nginx && python app.py"]
