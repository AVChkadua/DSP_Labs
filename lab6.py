import os.path as path
from sys import argv

import soundfile as sf
from numpy import arange, cos, pi
from scipy.signal import butter, lfilter

if len(argv) < 2:
    print("Usage: python3 lab5.py <WAV_file>")
    exit(-1)

if not path.isfile(argv[1]):
    print(f"{argv[1]} is not a file")
    exit(-1)

data, rate = sf.read(argv[1])

b_low, a_low = butter(10, 6000 / (rate / 2), btype="lowpass", output="ba")
b_high, a_high = butter(10, 6000 / (rate / 2), btype="highpass", output="ba")

lf = lfilter(b_low, a_low, data)
hf = lfilter(b_high, a_high, data)

carrier = cos(2 * pi * 44000 * arange(0, len(data) / rate, 1 / rate) + pi * 0.35)

demodulated = 2 * lfilter(b_low, a_low, hf * carrier)

sf.write(f"{path.basename(argv[1]).split('.')[0][6:]}_ch1.wav", lf + demodulated, rate)
sf.write(f"{path.basename(argv[1]).split('.')[0][6:]}_ch2.wav", lf - demodulated, rate)
