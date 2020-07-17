import numpy as np

############################# Optics Temperatures ############################################
def Temp_Opt():
    T_bath = 0.1 # bolometer operation temp
    T_baf = 5. # telescope shield ( optics tube ) temp
    T_cmb = 2.725 # CMB temp
    T_hwp_LFT = 20. # LFT-HWP temp
    T_hwp_HFT = 20. #HFT-HWP temp
    T_apt_LFT = 5. #aperture temp
    T_apt_HFT = 5. #aperture temp
    T_mir = T_baf #mirror temp
    T_fil = 2. #filter temp
    T_len = T_bath #detector lenslet temp
    T_lens = T_baf# HFT-lens temp
    Tr_hwp = T_baf# reflected temp of HWP
    Tr_mir = T_baf# reflected temp of mirror
    Tr_fil = T_bath # reflected temp of filter
    Tr_len = T_baf # reflected temp of detector lenslet
   # Tr_lens = T_baf # reflected temp of HFT-lens
    Tr_lens = 5 # reflected temp of HFT-lens
   
    return  T_bath, T_baf, T_cmb, T_hwp_LFT,T_hwp_HFT,T_apt_LFT, T_apt_HFT, T_mir, T_fil, T_len, T_lens, Tr_hwp,Tr_mir,Tr_fil,Tr_len,Tr_lens


################################# Optics parameters ##########################################

##### LFT #####
def LFT_Hwp(): #LFT HWP with ARC 
    hwp_emiss_LFT = np.array([[0.38e-2, 0.58e-2, 0.75e-2],[0.48e-2, 0.66e-2, 0.97e-2],[0.66e-2, 0.97e-2, 1.35e-2],[0.75e-2, 1.15e-2, 1.61e-2]]) #emissivity
    ref_hwp_LFT = np.array([[0.1, 0.068, 0.042],[0.1, 0.051, 0.037],[0.051, 0.037, 0.013],[0.042, 0.028, 0.001]]) #reflectance
    pol_hwp_LFT = np.array([[0.783, 0.965, 0.960],[0.929, 0.961, 0.970],[0.961, 0.970, 0.982],[0.960, 0.980, 0.964]]) #polarization eff
    df_LFT = np.array([[0.984, 0.984, 0.984],[0.984, 0.984, 0.984],[0.984, 0.984, 0.984],[0.984, 0.984, 0.984]]) #signal dilution factor
    return hwp_emiss_LFT, ref_hwp_LFT, pol_hwp_LFT, df_LFT


def LFT_Spill():
    spill_ts = np.array([[0.495, 0.222, 0.100],[0.340, 0.155, 0.067],[0.413, 0.232, 0.095],[0.317, 0.166, 0.059]]) #spillover at telescope shield
    spill_fb = np.array([[0.005, 0.004, 0.003],[0.005, 0.004, 0.003],[0.004, 0.003, 0.003],[0.004, 0.003, 0.003]]) #spillover at forebaffle
    spill_hm    = np.array([[0.010, 0.009, 0.008],[0.010, 0.009, 0.008],[0.009, 0.008, 0.008],[0.009, 0.008, 0.008]]) #spillover at HWP mount
    apt_eff = 1.-spill_ts - spill_fb - spill_hm # sky efficiency
    return spill_ts, spill_fb, spill_hm, apt_eff

def LFT_Apt():# LFT cold aperture stop 
    bf_LFT = 2.75 #beam waist factor
    Fnum_LFT = 1.92 #F number
    return bf_LFT, Fnum_LFT

def LFT_Det():# detector coupling efficiency
    det_eff_LFT =  np.array([[0.68, 0.68, 0.68 ],[0.68, 0.68, 0.68],[0.68, 0.68, 0.68],[0.68, 0.68, 0.68]]) 
    return det_eff_LFT 

##### MHFT #####
def HFT_Hwp():
    hwp_emiss_HFT = np.array([[0.035, 0.024, 0.019, 0.015, 0.014],[0.053, 0.033, 0.025, 0.020, 0.023]])  #emissivity
    ref_hwp_HFT   = np.array([[0.010, 0.019, 0.024, 0.012, 0.010],[0.025, 0.021, 0.025, 0.013, 0.009]]) #reflectance
    pol_hwp_HFT   = np.array([[0.987, 0.955, 0.938, 0.956, 0.984],[0.981, 0.966, 0.955, 0.977, 0.984]]) # polarization efficiency
    df_HFT   = np.array([[0.988, 0.988, 0.988, 0.988, 0.988],[0.972, 0.972, 0.972, 0.972, 0.972]]) # HWP rotation dilution factor
    return hwp_emiss_HFT, ref_hwp_HFT, pol_hwp_HFT, df_HFT 

def HFT_Apt():
    bf_HFT   = np.array([[2.75,2.75,2.75,2.75,2.75],[3.1, 3.1, 3.1,3.1,3.1]]) # beam waist factor
    Fnum_HFT = np.array([[2.4,2.4,2.4,2.4,2.4],[2.5,2.5,2.5,2.5,2.5]]) # F number
    return bf_HFT, Fnum_HFT 

def HFT_Det():# detector coupling efficiency
    det_eff_HFT = np.array([[0.68,0.68,0.68,0.68,0.68],[0.75, 0.75, 0.75,0.75,0.75]])
    return det_eff_HFT 


def HFT_Lens():
    emiss_L1 = np.array([[0.033, 0.035, 0.037, 0.040, 0.043],[0.039, 0.044, 0.049, 0.058, 0.069]]) #emissivity of first lens 
    emiss_L2 = np.array([[0.034, 0.036, 0.037, 0.039, 0.043],[0.038, 0.041, 0.045, 0.051, 0.060]]) #emissivity of second lens
    ref_L1   = np.array([[0.021, 0.021, 0.021, 0.021, 0.021],[0.024, 0.024, 0.024, 0.024, 0.024]]) #reflectance of first lens
    ref_L2   = np.array([[0.021, 0.021, 0.021, 0.021, 0.021],[0.024, 0.024, 0.024, 0.024, 0.024]]) #reflectance of second lens
    return emiss_L1, emiss_L2, ref_L1, ref_L2


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

def Len():# detector lenslet
    t_len = 9.e-3 #thickness
    n_len = 3.4 #refractive index
    tan_len = 5.e-5 #loss tangent
    ref_len = 0.05  #reflectance
    return t_len, n_len, tan_len, ref_len
  
