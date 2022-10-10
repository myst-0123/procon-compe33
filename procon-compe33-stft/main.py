import numpy as np
from scipy import signal
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import soundfile as sf

def main():
    for i in range(1, 10):
        print(i)
        data, fs = wav_read('../sound-data/J0' + str(i) + '.wav')
        binary, Sxx = stft(data[24000:96000], fs)
        np.savetxt('../data/J' + str(i) + '.txt', Sxx, delimiter=' ', fmt='%d')
        np.savetxt('../data/Jb' + str(i) + '.txt', binary, delimiter=' ', fmt='%d')
    for i in range(10, 45):
        print(i)
        data, fs = wav_read('../sound-data/J' + str(i) + '.wav')
        binary, Sxx = stft(data[24000:96000], fs)
        np.savetxt('../data/J' + str(i) + '.txt', Sxx, delimiter=' ', fmt='%d')
        np.savetxt('../data/Jb' + str(i) + '.txt', binary, delimiter=' ', fmt='%d')

    for i in range(1, 10):
        print(i)
        data, fs = wav_read('../sound-data/E0' + str(i) + '.wav')
        binary, Sxx = stft(data[24000:96000], fs)
        np.savetxt('../data/E' + str(i) + '.txt', Sxx, delimiter=' ', fmt='%d')
        np.savetxt('../data/Eb' + str(i) + '.txt', binary, delimiter=' ', fmt='%d')
    for i in range(10, 45):
        print(i)
        data, fs = wav_read('../sound-data/E' + str(i) + '.wav')
        binary, Sxx = stft(data[24000:96000], fs)
        np.savetxt('../data/E' + str(i) + '.txt', Sxx, delimiter=' ', fmt='%d')
        np.savetxt('../data/Eb' + str(i) + '.txt', binary, delimiter=' ', fmt='%d')

def wav_read(path):
    data, fs = sf.read(path)
    return data, fs

def stft(data, fs):
    threshold = -50
    f, t, Sxx = signal.spectrogram(data, fs, window='han', nperseg=512, noverlap=128)
    Sxx = 20*np.log10(Sxx)
    Sxx = Sxx - Sxx.max() - 1

    output = Sxx.copy()

    output[Sxx >= threshold] = 1
    output[Sxx < threshold] = 0
    

    print(output[output == 1].size)
    print(Sxx.size)
    return output, Sxx

if __name__ == '__main__':
    main()