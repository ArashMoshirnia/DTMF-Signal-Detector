#!/usr/bin/env python3
from scipy.io import wavfile as wav
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16 # format of sampling 16 bit int
CHANNELS = 1 # number of channels it means number of sample in every sampling
RATE = 44100 # number of sample in 1 second sampling
CHUNK = 1024 # length of every chunk
RECORD_SECONDS = 1 # time of recording in seconds
WAVE_OUTPUT_FILENAME = "file.wav" # file name
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

# storing voice
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

#reading voice
rate, data = wav.read('file.wav')

fft = np.fft.fft(data)
fft_list = fft.tolist()
fft_list = [abs(x) for x in fft_list]

fft_list = fft_list[0:len(fft_list)//2]


margin = 30
for i in range(0,margin):
    fft_list[i] = 0

max1 = max(fft_list)
max_index1 = fft_list.index(max1)

tolerance = 50
for i in range(max_index1-tolerance,max_index1+tolerance):
    fft_list[i] = 0

max2 = max(fft_list)
max_index2 = fft_list.index(max2)

row = [697,770,852,941]
col = [1209,1336,1477,1633]

print(max_index1)
print(max_index2)

tolerance = 30
max_index1, max_index2 = max_index2,max_index1

if row[0]-tolerance<max_index1<row[0]+tolerance and col[0]-tolerance<max_index2<col[0]+tolerance:
    print("Key pressed is 1")
if row[0]-tolerance<max_index1<row[0]+tolerance and col[1]-tolerance<max_index2<col[1]+tolerance:
    print("Key pressed is 2")
if row[0]-tolerance<max_index1<row[0]+tolerance and col[2]-tolerance<max_index2<col[2]+tolerance:
    print("Key pressed is 3")
if row[0]-tolerance<max_index1<row[0]+tolerance and col[3]-tolerance<max_index2<col[3]+tolerance:
    print("Key pressed is A")
if row[1]-tolerance<max_index1<row[1]+tolerance and col[0]-tolerance<max_index2<col[0]+tolerance:
    print("Key pressed is 4")
if row[1]-tolerance<max_index1<row[1]+tolerance and col[1]-tolerance<max_index2<col[1]+tolerance:
    print("Key pressed is 5")
if row[1]-tolerance<max_index1<row[1]+tolerance and col[2]-tolerance<max_index2<col[2]+tolerance:
    print("Key pressed is 6")
if row[1]-tolerance<max_index1<row[1]+tolerance and col[3]-tolerance<max_index2<col[3]+tolerance:
    print("Key pressed is B")
if row[2]-tolerance<max_index1<row[2]+tolerance and col[0]-tolerance<max_index2<col[0]+tolerance:
    print("Key pressed is 7")
if row[2]-tolerance<max_index1<row[2]+tolerance and col[1]-tolerance<max_index2<col[1]+tolerance:
    print("Key pressed is 8")
if row[2]-tolerance<max_index1<row[2]+tolerance and col[2]-tolerance<max_index2<col[2]+tolerance:
    print("Key pressed is 9")
if row[2]-tolerance<max_index1<row[2]+tolerance and col[3]-tolerance<max_index2<col[3]+tolerance:
    print("Key pressed is C")
if row[3]-tolerance<max_index1<row[3]+tolerance and col[0]-tolerance<max_index2<col[0]+tolerance:
    print("Key pressed is *")
if row[3]-tolerance<max_index1<row[3]+tolerance and col[1]-tolerance<max_index2<col[1]+tolerance:
    print("Key pressed is 0")
if row[3]-tolerance<max_index1<row[3]+tolerance and col[2]-tolerance<max_index2<col[2]+tolerance:
    print("Key pressed is #")
if row[3]-tolerance<max_index1<row[3]+tolerance and col[3]-tolerance<max_index2<col[3]+tolerance:
    print("Key pressed is D")
