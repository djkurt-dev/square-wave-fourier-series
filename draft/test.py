import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import *
import scipy.integrate as integrate

def square(x):
    if x>=0:
        return 1
    else:
        return -1
    
def fourierCoeffs(li, lf, n, f):
    l = (lf-li)/2
    # Constant term
    a0=1/l*integrate.quad(lambda x: f(x), li, lf)[0]
    # Cosine coefficents
    A = np.zeros((n))
    # Sine coefficents
    B = np.zeros((n))
     
    for i in range(1,n+1):
        A[i-1]=1/l*integrate.quad(lambda x: f(x)*np.cos(i*np.pi*x/l), li, lf)[0]
        B[i-1]=1/l*integrate.quad(lambda x: f(x)*np.sin(i*np.pi*x/l), li, lf)[0]
 
    return [a0/2.0, A, B]
 
# This functions returns the value of the Fourier series for a given value of x given the already calculated Fourier coefficients
def fourierSeries(coeffs,x,l,n):
    value = coeffs[0]
    for i in range(1,n+1):
        value = value + coeffs[1][i-1]*np.cos(i*np.pi*x/l) +  coeffs[2][i-1]*np.sin(i*np.pi*x/l)
    return value

   # Limits for the functions
li = -np.pi
lf = np.pi
l = (lf-li)/2.0

n = 1
for n in range(1,10):
    plt.title('Fourier Series Approximation\nSquare Wave\n n = '+str(n))

    coeffsSquare = fourierCoeffs(li,lf,n,square)
    
           # Step size for plotting
    step_size = 0.05
 
        # Limits for plotting
    x_l = -np.pi*2
    x_u = np.pi*2
    
    y2 = [squareP(li,lf,xi) for xi in x]
    y2_fourier = [fourierSeries(coeffsSquare,xi,l,n) for xi in x]
    
    # Square
    y_plot2 = []
    y_plot2_fourier = []
    
    x_l_plot = x_l - 13
    x_u_plot = x_l_plot + 14
    plt.xlim(x_l_plot,x_u_plot)
    plt.ylim(-6,7)
    
    for i in range(x.size):
        y_plot2.append(y2[i])
            # Values from fourier series
        y_plot2_fourier.append(y2_fourier[i])