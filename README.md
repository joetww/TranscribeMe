```markdown
# 音訊轉錄應用程式 Docker 映像

這個專案包含了一個 Docker 映像，其中包含了用於音訊轉錄的 Python 應用程式。

## Dockerfile

```Dockerfile
# 使用基礎映像
FROM python:3.8-slim

# 設定工作目錄
WORKDIR /app

# 複製所需檔案到工作目錄
COPY . .

# 安裝所需套件
RUN pip install -r requirements.txt

# 執行應用程式
CMD ["python", "app.py"]
```

## requirements.txt

```plaintext
requests==2.26.0
```

## 編譯 Docker 映像

要編譯這個 Docker 映像，請遵循以下步驟：

1. 確保已安裝 Docker。
2. 在命令列中，切換到包含 Dockerfile 和 requirements.txt 的目錄。
3. 執行以下命令來建立 Docker 映像：

```bash
docker build -t audio-transcriber .
```

## 運行 Docker 容器

要運行這個 Docker 映像作為容器，請執行以下命令：

```bash
docker run -e OPENAI_API_KEY='YOUR_OPENAI_API_KEY' -e OPENAI_API_URL='YOUR_OPENAI_API_URL' -e 'VIDEO_FILE=meet_part1.mp3' -v $(pwd):/app transcribe-app:latest
```

請將 `YOUR_OPENAI_API_KEY` 和 `YOUR_OPENAI_API_URL` 替換為您的實際 OpenAI API 金鑰和 URL。同時，請確保 `meet_part1.mp3` 是您要轉錄的音訊檔案名稱。這樣可以保護您的私密資訊不被公開顯示在 GitHub 上。

這將啟動一個包含音訊轉錄應用程式的 Docker 容器。您可以通過運行 `docker ps` 命令來檢查容器是否正在運行。

## 操作說明

一旦容器正在運行，您可以透過訪問容器內的應用程式來進行音訊轉錄。請注意，具體操作取決於應用程式的功能和使用方法。

請確保在使用之前仔細閱讀應用程式的文件或說明，以確保正確使用音訊轉錄應用程式。

有關更多操作說明和使用方法，請參考應用程式的文件或相關資源。
```

