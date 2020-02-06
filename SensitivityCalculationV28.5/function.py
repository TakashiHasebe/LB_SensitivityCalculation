import numpy as np

pi = np.pi
c = 299792458.
h = 6.626070040e-34 
k_b = 1.38064852e-23 

def FreqRange(freq, band): #define bandwidth  
    freq_l = freq*(1.-band/2.) # lowest freq
    freq_h = freq*(1.+band/2.) # highest freq
    return freq_l, freq_h

def BB( freq, T): # blackbody distribution
    out =  h*freq /(np.exp( h/k_b*freq/T) - 1.)
    return out

def Trm (t, n, losstan, freq, ref): #emissivity calculation for refractive optics
    emiss = 1. - np.exp(-2.*pi*t*n*losstan*freq/c)
    eff = 1. - ref - emiss
    return emiss, eff

def Hwp (hwp_emiss, ref_hwp):
    eff = 1. - ref_hwp - hwp_emiss
    return eff

def Aperture( dpix, beamwaistfactor, Fnum, freq): #aperture efficiency calulation
    apt_eff = 1. - np.exp(-1.*pi**2./2.*(dpix/beamwaistfactor/Fnum*freq/c)**2.) # aperture efficiency
    apt_emiss = 1. - apt_eff # aperture spillover
    return apt_emiss, apt_eff

def Mirror(freq, rho, epsilon, rms): #emissivity calculation for mirror
    mir_emiss = 4.*np.sqrt(pi*freq*rho*epsilon);
    mir_loss = 1-np.exp(-1.*pow(4.*pi*rms*freq/c,2.))
    mir_eff = 1. - mir_emiss - mir_loss
    return mir_emiss, mir_eff, mir_loss;


def dPdT(freq, eff, T_cmb): # conversion factor from NEP to NET 
    dpdt = eff/k_b*(h*freq /T_cmb/(np.exp( h/k_b*freq/T_cmb) - 1.))**2.*np.exp( h/k_b*freq/T_cmb)
    return dpdt

def Sigma(NET, t): # conversion from [K/rtHz] to [K-arcmin]
    sigma = np.sqrt(4.*pi*2.*NET*NET/t)*10800./pi;
    return sigma
