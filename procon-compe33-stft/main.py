import numpy as np
from scipy import signal
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import wave

def main():
    data, fs = wav_read('../sound-data/J01.wav')
    print(max(data), min(data))

    
    
    f, t, Sxx = signal.spectrogram(data, fs, window='hamming', nperseg=512)

    Sxx2 = np.log10(Sxx)
    print(Sxx2.max(), Sxx2.min())
    
    plt.pcolormesh(t, f, Sxx2)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('intensity [dB]')
    plt.show()

def wav_read(path):
    wav = wave.open(path)
    buffer = wav.readframes(-1)
    data = np.frombuffer(buffer, dtype='int16')
    fs = wav.getframerate()
    return data, fs

if __name__ == '__main__':
    main()