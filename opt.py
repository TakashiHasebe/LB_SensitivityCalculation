
import numpy as np

############################# Optics Temperatures ############################################
def Temp_Opt():
    T_bath = 0.1
    T_cmb = 2.725
    T_hwp_LFT = 20.
    T_hwp_HFT = 20.
    T_apt = 5.
    T_mir = 5.
    T_fil = 2.
    T_len = T_bath
    T_lens = 5.
    T_baf = 5.
    Tr_hwp = 5.
    Tr_mir = 5.
    Tr_fil = T_bath
    Tr_len = T_bath
    Tr_lens = 5.
   
    return  T_bath, T_cmb, T_hwp_LFT,T_hwp_HFT,T_apt, T_mir, T_fil, T_len, T_lens, T_baf, Tr_hwp,Tr_mir,Tr_fil,Tr_len,Tr_lens


################################# Optics parameters ##########################################

##### LFT #####
def LFT_Hwp(confLFT):#LFT HWP with ARC 
   # hwp_emiss_LFT = np.array([[3.83e-3, 5.79e-3, 7.52e-3],[4.81e-3, 6.57e-3, 8.59e-3],[6.57e-3, 8.59e-3, 1.15e-2],[7.52e-3, 9.66e-3, 1.35e-2]])
   # ref_hwp_LFT = np.array([[0.116, 0.03, 0.036],[0.046, 0.033, 0.027],[0.033, 0.027, 0.016],[0.036, 0.02, 0.013]])
    hwp_emiss_LFT = np.array([[0.38e-2, 0.58e-2, 0.75e-2],[0.48e-2, 0.66e-2, 0.97e-2],[0.66e-2, 0.97e-2, 1.35e-2],[0.75e-2, 1.15e-2, 1.61e-2]])
   # ref_hwp_LFT = np.array([[0.175, 0.068, 0.042],[0.103, 0.051, 0.037],[0.051, 0.037, 0.013],[0.042, 0.028, 0.001]])
    ref_hwp_LFT = np.array([[0.1, 0.068, 0.042],[0.1, 0.051, 0.037],[0.051, 0.037, 0.013],[0.042, 0.028, 0.001]])
   # ref_hwp_LFT = np.array([[0., 0., 0.],[0.103, 0.051, 0.037],[0.051, 0.037, 0.013],[0.042, 0.028, 0.001]])
   

#   # hwp_holder_LFT = np.array([[0.013, 0.013, 0.013],[0.013, 0.013, 0.013],[0.013, 0.013, 0.013],[0.013, 0.013, 0.013]])
    hwp_holder_LFT = np.array([[1.3e-2, 0.49e-2, 0.15e-2],[0.84e-2, 0.3e-2, 0.06e-2],[1.03e-2, 0.51e-2, 0.13e-2],[0.75e-2, 0.33e-2, 0.04e-2]])
    return hwp_emiss_LFT, ref_hwp_LFT, hwp_holder_LFT

def LFT_Apt(confLFT):# LFT aperture 
    bf_LFT = 2.75 #beam waist factor
    Fnum_LFT = 3. #F number
    return bf_LFT, Fnum_LFT

def LFT_Det(confLFT):# detector coupling efficiency
    det_eff_LFT = 0.68
    return det_eff_LFT 

##### HFT #####
def HFT_Hwp(confHFT):
    if confHFT == 0:#embedded mesh HWP for reflective HFT   
        hwp_emiss_HFT = np.array([[2.1e-2,2.1e-2,2.1e-2],[2.1e-2,2.1e-2,2.1e-2],[2.1e-2,2.1e-2,2.1e-2]])
        ref_hwp_HFT = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
    if confHFT == 1:#transmissive mesh HWP for split HFT
        hwp_emiss_HFT = np.array([[3.3e-2, 3.3e-2, 3.3e-2],[3.3e-2, 3.3e-2, 3.3e-2],[3.e-2, 3.e-2, 3.e-2]])  
        ref_hwp_HFT = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
    if confHFT == 2:#transmissive mesh HWP for split HFT
        hwp_emiss_HFT = np.array([[4.4e-2, 2.1e-2, 2.4e-2],[2.7e-2, 1.7e-2, 2.8e-2],[2.1e-2, 1.7e-2, 2.7e-2]])  
        ref_hwp_HFT = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
     
    return hwp_emiss_HFT, ref_hwp_HFT 

def HFT_Apt(confHFT):
    if confHFT == 0:#reflective HFT aperture
        bf_HFT = np.array([[2.75,2.75,2.75],[2.75,2.75,2.75],[3.1,3.1,3.1]])
        Fnum_HFT = 3.5
    if confHFT == 1:#split HFT aperture
        bf_HFT = np.array([[2.75,2.75,2.75],[2.75,2.75,2.75],[3.1,3.1,3.1]])
        Fnum_HFT = 2.2
    if confHFT == 2:#split HFT aperture
        bf_HFT = np.array([[2.75,2.75,2.75],[2.75,2.75,2.75],[3.1,3.1,3.1]])
       # bf_HFT = np.array([[2.75,2.75,2.75],[2.75,2.75,2.75],[2.75,2.75,3.1]])
       # Fnum_HFT = 3.0
        Fnum_HFT = 2.2
    return bf_HFT, Fnum_HFT 

def HFT_Det(confHFT):# detector coupling efficiency
    #det_eff_HFT = np.array([[0.68,0.68,0.68],[0.68,0.68,0.68],[0.75,0.85,0.75]])
    det_eff_HFT = np.array([[0.68,0.68,0.68],[0.68,0.68,0.68],[0.75,0.75,0.75]])
  
    return det_eff_HFT 

##### common optics #####
def Sap_HWP():#Sapphire HWP for HFT
    t_hwp = 15.e-3 #thickness
    n_hwp = 3.24 #refractive index
    tan_hwp = 5.e-5 #loss tangent
    ref_hwp_sap = 0.03 #reflection
    return t_hwp, n_hwp, tan_hwp, ref_hwp_sap

def Mir():#Mirror 
    epsilon = 8.854e-12 
    rho = 1.39e-8 #resistivity
    rms = 2.e-6 #sirface roughness
    return epsilon, rho, rms

def Si_Lens():#Field and Objective Lenses
    t_lens1 = 20.e-3
    t_lens2 = 20.e-3
    t_lens3 = 20.e-3
    t_lens4 = 20.e-3
   # t_lens = 20.e-3
    n_lens = 3.4
    tan_lens = 5.e-5
    ref_lens = 0.03
    return t_lens1, t_lens2,t_lens3,t_lens4, n_lens, tan_lens, ref_lens

def HDPE_Lens():#Field and Objective Lenses
    t_lens1 = 30.e-3
    t_lens2 = 45.e-3
    t_lens3 = 25.e-3
    t_lens4 = 30.e-3
   # n_lens = 1.57
    n_lens = 1.52
   # tan_lens = 5.e-5
    tan_lens = 3.e-4
    ref_lens = 0.03
     
    return t_lens1, t_lens2,t_lens3,t_lens4,n_lens, tan_lens, ref_lens


def Fil():#2K filter
    t_fil = 5.e-3
    n_fil = 1.5
    tan_fil = 2.3e-4
    ref_fil = 0.05
    return t_fil, n_fil, tan_fil, ref_fil

def Len():# detector lenslet
    t_len = 9.e-3
    n_len = 3.4
    tan_len = 5.e-5
    ref_len = 0.05 
    return t_len, n_len, tan_len, ref_len
  
