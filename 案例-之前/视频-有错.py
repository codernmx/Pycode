import pyaudio
import wave

filename = 'rec.wav'
chunk = 1024
FORMAT = pyaudio.paInt16
channels = 1
sample_rate = 44100
record_second = 5
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=channels, rate=sample_rate,
                input=True, output=True, frames_per_buffer=chunk)
frames = []
print("开始录制")
for i in range(int(44100/chunk * record_second)):
    data = stream.read(chunk)
    frames.append(data)
print('录制完毕')
stream.stop_stream()
stream.close()
p.terminate()
# 写入文件
wf = wave.open(filename, 'wb')
wf.setchannels(channels)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setfreamerate(sample_rate)
wf.writeframes(b"".join(frames))
wf.close()