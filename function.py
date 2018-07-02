import numpy as np

pi = np.pi
k_b = 1.3806503e-23
c = 299792458.
h = 6.626068e-34

def FreqRange(freq, band):
    freq_l = freq*(1.-band/2.)
    freq_h = freq*(1.+band/2.)
    return freq_l, freq_h

def BB( freq, T):
    out =  h*freq /(np.exp( h/k_b*freq/T) - 1.)
    return out

def Trm (d, n, losstan, freq, ref):
    emiss = 1. - np.exp(-2.*pi*d*n*losstan*freq/c)
    eff = 1. - ref - emiss
    return emiss, eff

def Hwp (hwp_emiss, ref_hwp):
    eff = 1. - ref_hwp - hwp_emiss
    return eff

def Aperture( dpix, beamwaistfactor, Fnum, freq_c):
    apt_eff = 1. - np.exp(-1.*pi**2./2.*(dpix/beamwaistfactor/Fnum*freq_c/c)**2.) # aperture efficiency
    apt_emiss = 1. - apt_eff # aperture emissivity
    return apt_emiss, apt_eff

def Mirror(freq, rho, epsilon, rms):
    mir_emiss = 4.*np.sqrt(pi*freq*rho*epsilon);
    mir_loss = 1-np.exp(-1.*pow(4.*pi*rms*freq/c,2.))
    mir_eff = 1. - mir_emiss - mir_loss
    return mir_emiss, mir_eff, mir_loss;


def dPdT(freq, eff, T_cmb):
    dpdt = eff/k_b*(h*freq /T_cmb/(np.exp( h/k_b*freq/T_cmb) - 1.))**2.*np.exp( h/k_b*freq/T_cmb)
    return dpdt

def Sigma(NET, t):
    sigma = np.sqrt(4.*pi*2.*NET*NET/t)*10800./pi;
    return sigma
