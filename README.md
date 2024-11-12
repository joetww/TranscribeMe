
# 音訊轉錄應用程式 Docker 映像


## 編譯 Docker 映像

要編譯這個 Docker 映像，請遵循以下步驟：

1. 確保已安裝 Docker。
2. 在命令列中，切換到包含 Dockerfile 和 requirements.txt 的目錄。
3. 執行以下命令來建立 Docker 映像：

```bash
docker build -t transcribe-app .
```

## 運行 Docker 容器

要運行這個 Docker 映像作為容器，請執行以下命令：

```bash
docker run -e OPENAI_API_KEY='YOUR_OPENAI_API_KEY' -e OPENAI_API_URL='YOUR_OPENAI_API_URL' -e 'VIDEO_FILE=meet_part1.mp3' -v $(pwd):/app transcribe-app:latest
```

請將 `YOUR_OPENAI_API_KEY` 和 `YOUR_OPENAI_API_URL` 替換為您的實際 OpenAI API 金鑰和 URL。同時，請確保 `meet_part1.mp3` 是您要轉錄的音訊檔案名稱。

