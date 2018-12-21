import matplotlib.pyplot as plt
import soundfile as sf
from numpy import abs, arange
from numpy.fft import fft
from scipy.signal import butter, lfilter
from sys import argv

data, rate = sf.read(argv[1])

plt.subplots()
plt.plot(arange(0, 131072), abs(fft(data, 131072)))
plt.show()

b, a = butter(10, 3000 / (rate / 2), btype="lowpass", output="ba")

filtered = lfilter(b, a, data)
plt.subplots()
plt.plot(arange(0, 131072), abs(fft(filtered, 131072)))
plt.show()

sf.write(argv[1].split(".")[0] + "_filt_sample.wav", filtered, rate)
