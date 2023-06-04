import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the square wave
amplitude = 1  # Amplitude of the square wave
frequency = 1  # Frequency of the square wave
phase = 0  # Phase of the square wave

# Set the time range
t = np.linspace(0, 2, num=1000)

# Generate the square wave
square_wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t + phase))

# Plot the square wave
plt.plot(t, square_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Square Wave')
plt.grid(True)
plt.show()