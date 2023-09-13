# 安装指令
# pip install SpeechRecognition
import speech_recognition as sr
from pydub import AudioSegment

def mp3_to_wav(mp3_filename):
    audio = AudioSegment.from_mp3(mp3_filename)
    wav_filename = mp3_filename.replace(".mp3", ".wav")
    audio.export(wav_filename, format="wav")
    return wav_filename


mp3_filename = "test.mp3"  # 替换为您的MP3文件路径
wav_filename = mp3_to_wav(mp3_filename)
