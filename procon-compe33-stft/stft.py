import numpy as np
from scipy import signal
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import soundfile as sf

def main():
    data, fs = wav_read('../sound-data/problem.wav')
    Sxx = stft(data, fs)
    np.savetxt('../problem.txt', Sxx, delimiter=' ', fmt='%d')

def wav_read(path):
    data, fs = sf.read(path)
    return data, fs

def stft(data, fs):
    f, t, Sxx = signal.spectrogram(data, fs, window='han', nperseg=512)
    Sxx = 20*np.log10(Sxx)
    Sxx = Sxx - (Sxx.max() - 1) 
    return Sxx

if __name__ == '__main__':
    main()