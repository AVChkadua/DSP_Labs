import matplotlib.pyplot as plt
import soundfile as sf
from numpy import abs, arange
from numpy.fft import fft
from scipy.signal import butter, lfilter
from sys import argv
import os.path as path


if len(argv) < 2:
    print("Usage: python3 lab5.py <WAV_file>")
    exit(-1)

if not path.isfile(argv[1]):
    print(f"{argv[1]} is not a file")
    exit(-1)

data, rate = sf.read(argv[1])

plt.subplots()
plt.plot(arange(0, 134160), abs(fft(data)))
plt.show()

b, a = butter(10, 3000 / (rate / 2), btype="lowpass", output="ba")

filtered = lfilter(b, a, data)
plt.subplots()
plt.plot(arange(0, 131072), abs(fft(filtered, 131072)))
plt.show()

sf.write(f"{path.basename(argv[1]).split('.')[0][6:]}_filt_sample.wav", filtered, rate)
