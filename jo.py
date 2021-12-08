import numpy as np

def remove_mean(signal):
    signal_mean = np.mean(signal)
    signal_mean_removed = signal - signal_mean
    return signal_mean_removed
