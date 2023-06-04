import numpy as np
import matplotlib.pyplot as plt

# Number of harmonics in Fourier series
num_harmonics = 50

# Define the square wave function
def square_wave(x):
    wave = 0
    for n in range(1, num_harmonics+1):
        harmonic = (4 / (2*n-1)) * np.sin((2*np.pi*(2*n-1)*x) / T)
        wave += harmonic
    return wave

# Generate x-values
T = 2*np.pi
x = np.linspace(-np.pi, 2*np.pi, 1000)

# Generate y-values using the square wave function
y = np.array([square_wave(val) for val in x])

# Plot the square wave
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Square Wave Fourier Series')
plt.grid(True)
plt.show()