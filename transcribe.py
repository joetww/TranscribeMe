import openai
import os
from pydub import AudioSegment
import tempfile
import srt

# 設定 OpenAI API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_URL", "https://api.openai.com/v1")

def transcribe_audio_segment(audio_segment):
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_wav:
        audio_segment.export(temp_wav.name, format="mp3")
        
        with open(temp_wav.name, "rb") as audio_file:
            # 在每次呼叫 transcribe_audio_segment 前重新建立一個 ChatGPT 實例
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.Audio.transcribe("whisper-1", audio_file)
            print(response['text'])  # 顯示轉錄出來的字幕內容以進行調試
            
            if 'segments' in response:
                return response['segments']
            elif 'text' in response:
                return [{'start': 0, 'end': len(response['text']), 'text': response['text']}]
            else:
                raise ValueError("Unexpected response format from OpenAI API")

def create_srt(segments, output_file):
    srt_entries = []
    current_time = 0
    
    for i, segment in enumerate(segments):
        content = segment['text'].strip()

        if content:  # 檢查非空行
            # 計算對話的長度，並根據對話長度調整時間軸
            text_length = len(content)
            start_time = current_time
            end_time = current_time + text_length
            current_time = end_time
            
            srt_entry = srt.Subtitle(
                index=i + 1,
                start=srt.timedelta(seconds=start_time),
                end=srt.timedelta(seconds=end_time),
                content=content
            )
            srt_entries.append(srt_entry)

    # 將 SRT 條目轉換為 SRT 格式
    srt_content = srt.compose(srt_entries)
    
    # 寫入 SRT 檔案
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(srt_content)

def split_audio_into_segments(audio_file, segment_length=60):
    audio = AudioSegment.from_file(audio_file)
    segments = []
    duration_ms = len(audio)
    
    for start in range(0, duration_ms, segment_length * 1000):
        end = min(start + segment_length * 1000, duration_ms)
        segment = audio[start:end]
        segments.append(segment)
    
    return segments

if __name__ == "__main__":
    video_file = os.getenv("VIDEO_FILE")
    
    if video_file is None:
        print("請設定 VIDEO_FILE 環境變數來指定影片檔案")
        sys.exit(1)
    
    audio_segments = split_audio_into_segments(video_file, segment_length=5)
    
    all_segments = []
    for i, segment in enumerate(audio_segments):
        print(f"Transcribing segment {i + 1}/{len(audio_segments)}...")
        segments = transcribe_audio_segment(segment)
        all_segments.extend(segments)

    # 輸出 SRT 檔案
    srt_file = "output.srt"
    create_srt(all_segments, srt_file)
    print(f"SRT 檔案已儲存為 {srt_file}")

