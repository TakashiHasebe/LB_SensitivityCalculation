import numpy as np

#################################################################
#################################################################
############################ V28.5.1 ############################
#################################################################
#################################################################


def MFT_param(): 

############################# MFT optics Temperatures ############################################
    T_bath_MFT = 0.1     # bolometer operation temp
    T_len_MFT = 0.1      # detector lenslet temp
    T_hood_MFT = 2.      # Detector hood
    T_fil_MFT = 2.       # filter temp
    T_L1_MFT = 5.        # lens temp
    T_L2_MFT = 5.        # lens temp
    T_abs_MFT = 5.       # Absorbers temp
    T_apt_MFT = 5.       # aperture temp
    T_hwp_MFT = 20.      # HWP temp
    T_baf_MFT = 5.       # baffle temp

################################# MFT Detectors parameters ##########################################
    det_eff_MFT = np.array([0.69, 0.69, 0.69,0.69,0.69])     # Detector efficiency including lenslets & horns
    freq_MFT = np.array([100., 119., 140., 166., 195.])
    band_MFT = np.array([0.23, 0.3, 0.3,0.3,0.3])
    dpix_MFT = np.array([12., 12., 12.,12., 12.])
    npix_MFT = np.array([183.,244.,183.,244.,183])
    ref_len_MFT = 0.05  #reflectance
    # t_len_MFT = np.array([9.e-3,9.e-3]) #thickness
    # n_len_MFT = np.array([3.4,3.4]) #refractive index
    # tan_len_MFT = np.array([5.e-5,5.e-5]) #loss tangent
    # ref_len_MFT = 0.05,0.05  #reflectance


################################# Filters parameters ##########################################
    t_fil_MFT = 5.e-3 #thickness
    n_fil_MFT = 1.5 #refractive index
    tan_fil_MFT = 2.3e-4 # loss tangent
    ref_fil_MFT = 0.05 # reflectance

################################# MFT Lenses parameters ##########################################
    emiss_L1_MFT = np.array([0.033, 0.035, 0.037, 0.040, 0.043]) # emissivity of first lens MFT
    emiss_L2_MFT = np.array([0.034, 0.036, 0.037, 0.039, 0.043]) # emissivity of second lens MFT
    ref_L1_MFT   = np.array([0.021, 0.021, 0.021, 0.021, 0.021]) # reflectance of first lens MFT
    ref_L2_MFT   = np.array([0.021, 0.021, 0.021, 0.021, 0.021]) # reflectance of second lens MFT

################################# MFT Aperture parameters ##########################################
    bf_MFT   = np.array([2.75,2.75,2.75,2.75,2.75]) # beam waist factor MFT
    Fnum_MFT = np.array([2.4,2.4,2.4,2.4,2.4]) # F number MFT

################################# MFT HWP parameters ##########################################
    hwp_emiss_MFT = np.array([0.035, 0.024, 0.019, 0.015, 0.014]) # emissivity MFT
    ref_hwp_MFT   = np.array([0.010, 0.019, 0.024, 0.012, 0.010]) # reflectance MFT
    pol_hwp_MFT   = np.array([0.987, 0.955, 0.938, 0.956, 0.984]) # polarization efficiency MFT
    pol_dil_MFT   = np.array([1., 1., 1., 1., 1.])                # HWP rotation dilution factor MFT 
                            #0.988, 0.988, 0.988, 0.988, 0.988

################################# MFT Spill 5K/2K parameters ##########################################
    apt_spill_MFT = np.array([0.102, 0.047, 0.017, 0.005, 0.002])
    L1_spill_MFT = np.array([0.0130, 0.0040, 0.0009, 0.0002, 0.0005])
    L2_spill_MFT = np.array([0.0160, 0.0080, 0.0035, 0.0012, 0.0000])    
    total_spill_MFT = np.array([0.128, 0.058, 0.022, 0.006, 0.003])
    spill_5Kenv_MFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Estimated at 5% in a first order with a naive geometric estimate MFT
    spill_2Khood_MFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Estimated at 5% in a first order with a naive geometric estimate MFT

    return  T_bath_MFT, T_len_MFT, T_hood_MFT, T_fil_MFT, T_L1_MFT, T_L2_MFT, T_abs_MFT, T_apt_MFT, T_hwp_MFT, T_baf_MFT, det_eff_MFT, freq_MFT, band_MFT, dpix_MFT, npix_MFT,ref_len_MFT, t_fil_MFT, n_fil_MFT, tan_fil_MFT, ref_fil_MFT, emiss_L1_MFT, emiss_L2_MFT, ref_L1_MFT, ref_L2_MFT, bf_MFT, Fnum_MFT, hwp_emiss_MFT, ref_hwp_MFT, pol_hwp_MFT, pol_dil_MFT, apt_spill_MFT, L1_spill_MFT, L2_spill_MFT, total_spill_MFT, spill_5Kenv_MFT, spill_2Khood_MFT



# def MFT_Len([]):# detector lenslet [ MFT , MFT ]
#     t_len_MFT = np.array([[9.e-3,9.e-3]]) #thickness [MFT,MFT]
#     n_len_MFT = np.array([[3.4,3.4]]) #refractive index [MFT,MFT]
#     tan_len_MFT = np.array([[5.e-5,5.e-5]]) #loss tangent [MFT,MFT]
#     ref_len_MFT = np.array([[0.05,0.05]])  #reflectance [MFT,MFT]
#     return t_len_MFT, n_len_MFT, tan_len_MFT, ref_len_MFT
  