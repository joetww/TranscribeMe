# 使用官方的 Python 基礎映像
FROM python:3.10.15-slim

# 安裝 ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 到容器中
COPY requirements.txt .

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 複製當前目錄的內容到容器中
COPY . .

# 設定容器啟動時執行的命令
CMD ["python", "transcribe.py"]

