import numpy as np
from scipy import signal
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import soundfile as sf

def main():
    print('processing...')
    for i in range(1, 10):
        print(str(i))
        data, fs = wav_read('../sound-data/J0' + str(i) + '.wav')
        for start in range(0, 144001, 4800):
            binary, Sxx = stft(data[start:start+72000], fs)
            np.savetxt('../data/J' + str(i) + '-' + str(start) + '.txt', Sxx, delimiter=' ', fmt='%d')
            np.savetxt('../data/Jb' + str(i) + '-' + str(start) + '.txt', binary, delimiter=' ', fmt='%d')
    for i in range(10, 45):
        print(str(i))
        data, fs = wav_read('../sound-data/J' + str(i) + '.wav')
        for start in range(0, 144001, 4800):
            binary, Sxx = stft(data[start:start+72000], fs)
            np.savetxt('../data/J' + str(i) + '-' + str(start) + '.txt', Sxx, delimiter=' ', fmt='%d')
            np.savetxt('../data/Jb' + str(i) + '-' + str(start) + '.txt', binary, delimiter=' ', fmt='%d')

    for i in range(1, 10):
        print(str(i))
        data, fs = wav_read('../sound-data/E0' + str(i) + '.wav')
        for start in range(0, 144001, 4800):
            binary, Sxx = stft(data[start:start+72000], fs)
            np.savetxt('../data/E' + str(i) + '-' + str(start) + '.txt', Sxx, delimiter=' ', fmt='%d')
            np.savetxt('../data/Eb' + str(i) + '-' + str(start) + '.txt', binary, delimiter=' ', fmt='%d')
    for i in range(10, 45):
        print(str(i))
        data, fs = wav_read('../sound-data/E' + str(i) + '.wav')
        for start in range(0, 144001, 4800):
            binary, Sxx = stft(data[start:start+72000], fs)
            np.savetxt('../data/E' + str(i) + '-' + str(start) + '.txt', Sxx, delimiter=' ', fmt='%d')
            np.savetxt('../data/Eb' + str(i) + '-' + str(start) + '.txt', binary, delimiter=' ', fmt='%d')

def wav_read(path):
    data, fs = sf.read(path)
    return data, fs

def stft(data, fs):
    threshold = -60
    f, t, Sxx = signal.spectrogram(data, fs, window='han', nperseg=2048, noverlap=256)
    Sxx = 20*np.log10(Sxx)
    Sxx = Sxx - Sxx.max() - 1

    output = Sxx.copy()

    output[Sxx >= threshold] = 1
    output[Sxx < threshold] = 0
    
    return output, Sxx

if __name__ == '__main__':
    main()