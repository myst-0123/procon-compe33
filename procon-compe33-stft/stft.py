import numpy as np
from scipy import signal
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import soundfile as sf

import main

def stft():
    data, fs = main.wav_read('../sound-data/problem.wav')
    binary, Sxx = main.stft(data, fs)
    np.savetxt('../problem.txt', Sxx, delimiter=' ', fmt='%d')
    np.savetxt('../problemb.txt', binary, delimiter=' ', fmt="%d")

if __name__ == '__main__':
    stft()