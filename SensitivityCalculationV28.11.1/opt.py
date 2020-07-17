import numpy as np

############################# Optics Temperatures ############################################
def Temp_Opt():
    T_baf = 5. # telescope baffle temperature
    T_bath = 0.1 # detector bath temperature
    T_bolo = T_bath *1.71 # bolometer temperature
    T_cmb = 2.725 # CMB temp
    T_hwp_LFT = 20. # LFT-HWP temp
    #T_apt_LFT = 5. #aperture temp
    T_apt_LFT = 2. #aperture temp
    T_mir = T_baf #mirror temp
    T_fil = 2. #filter temp
    T_FPhood = 2. #FP hood temp
    Tr_hwp = T_baf # reflected temp of HWP
    Tr_mir = T_baf # reflected temp of mirror
    Tr_fil = T_bolo
    Tr_det = T_bolo
    return  T_baf, T_bath, T_bolo, T_cmb, T_hwp_LFT,T_apt_LFT, T_mir, T_fil, T_FPhood, Tr_hwp, Tr_mir, Tr_fil, Tr_det

################################# Optics parameters ##########################################

##### LFT #####
def LFT_Hwp(): #LFT HWP with ARC 
    eff_hwp_LFT = np.array([[0.906, 0.962, 0.961],[0.952, 0.963, 0.969],[0.963, 0.969, 0.978],[0.961, 0.975, 0.976]]) #efficiency
    ref_hwp_LFT = np.array([[0.091, 0.033, 0.032],[0.043, 0.031, 0.024],[0.031, 0.024, 0.012],[0.032, 0.016, 0.013]]) #reflectance
    emiss_hwp_LFT=np.array([[0.003, 0.005, 0.007],[0.005, 0.006, 0.007],[0.006, 0.007, 0.010],[0.007, 0.009, 0.011]]) #reflectance
    pol_hwp_LFT = np.array([[0.866, 0.997, 0.993],[0.972, 0.996, 0.996],[0.996, 0.996, 0.991],[0.993, 0.997, 0.971]]) #polarization eff
    return eff_hwp_LFT, ref_hwp_LFT, emiss_hwp_LFT, pol_hwp_LFT

def LFT_Spill():
    spill_2Khood = np.array([[0.093, 0.093, 0.093],[0.093, 0.093, 0.093],[0.089, 0.062, 0.027],[0.077, 0.047, 0.011]]) #spillover at 2K hood
    spill_2Kstop = np.array([[0.177, 0.049, 0.015],[0.090, 0.025, 0.011],[0.183, 0.122, 0.048],[0.156, 0.088, 0.020]]) #spillover at 2K stop
    #spill_2Kstop = np.array([[0.27, 0.049, 0.015],[0.090, 0.025, 0.011],[0.183, 0.122, 0.048],[0.156, 0.088, 0.020]]) #spillover at 2K stop
    spill_20K    = np.array([[0.004, 0.002, 0.001],[0.003, 0.001, 0.000],[0.004, 0.004, 0.004],[0.004, 0.004, 0.004]]) #spillover at 20K HWP mount
    spill_5Kenve = np.array([[0.093, 0.071, 0.070],[0.073, 0.070, 0.070],[0.193, 0.087, 0.026],[0.134, 0.055, 0.011]]) #spillover at 5K envelope
    #spill_5Kenve = np.array([[0., 0.071, 0.070],[0.073, 0.070, 0.070],[0.193, 0.087, 0.026],[0.134, 0.055, 0.011]]) #spillover at 5K envelope
    apt_eff = 1.-spill_2Khood - spill_2Kstop - spill_5Kenve - spill_20K # sky efficiency
    return spill_2Khood, spill_2Kstop, spill_5Kenve,  spill_20K, apt_eff

def LFT_Det():# detector coupling efficiency
    det_eff_LFT =  np.array([[0.69, 0.69, 0.69 ],[0.69, 0.69, 0.69],[0.69, 0.69, 0.69],[0.69, 0.69, 0.69]]) 
    return det_eff_LFT

def Mir():#Mirror 
    epsilon = 8.854e-12 
    rho = 1.39e-8 #resistivity
    rms = 2.e-6 #surface roughness
    return epsilon, rho, rms


def Fil():#2K filter
    t_fil = 5.e-3 #thickness
    n_fil = 1.5 #refractive index
    tan_fil = 2.3e-4 # loss tangent
    ref_fil = 0.05 # reflectance
    return t_fil, n_fil, tan_fil, ref_fil

  
