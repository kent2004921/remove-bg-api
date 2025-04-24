FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir flask pillow numpy opencv-python dlib

# 暴露 Flask 默认端口
EXPOSE 5000

# 启动 Flask 应用
CMD ["python", "app.py"]