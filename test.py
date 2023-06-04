from scipy import integrate
import numpy as np

def square(x):
    if x>=0:
        return 1
    else:
        return -1
    
def fourier(li, lf, n, f):
    l = (lf-li)/2
    # Constant term
    a0=1/l*integrate.quad(lambda x: f(x), li, lf)[0]
    # Cosine coefficents
    A = np.zeros((n))
    # Sine coefficents
    B = np.zeros((n))
     
    for i in range(1,n+1):
        A[i-1]=1/l*integrate.quad(lambda x: f(x)*np.cos(i*np.pi*x/l), li, lf)[0]
        B[i-1]=1/l* integrate.quad(lambda x: f(x)*np.sin(i*np.pi*x/l), li, lf)[0]
 
    return [a0/2.0, A, B]


# Limits for the functions
li = -np.pi
lf = np.pi
 
# Number of harmonic terms
n = 50

coeffs = fourier(li,lf,n,square)
print('Fourier coefficients for the Square wave\n')
print('a0 ='+str(coeffs[0]))
print('an ='+str(coeffs[1]))
print('bn ='+str(coeffs[2]))
print('-----------------------\n\n')