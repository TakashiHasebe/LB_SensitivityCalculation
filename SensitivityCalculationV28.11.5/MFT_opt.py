import numpy as np

#################################################################
#################################################################
############################ V28.9.0 ############################
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
    #T_apt_MFT = 5.       # aperture temp
    T_apt_MFT = 2.       # aperture temp
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
   # apt_spill_MFT = np.array([0.102, 0.047, 0.017, 0.005, 0.002])
    apt_spill_MFT = np.array([7.41e-2, 3.79e-2, 2.75e-2, 2.64e-2, 2.46e-2])
    spill_5K_MFT = np.array([6.34e-2, 6.30e-2, 6.19e-2, 5.97e-2, 5.68e-2])
    spill_2K_MFT = np.array([6.41e-2, 6.32e-2, 6.24e-2, 6.16e-2, 6.10e-2])    
    sky_eff_MFT = np.array([6.77e-1, 7.36e-1, 7.54e-1, 7.34e-1, 6.83e-1])

    ref1_5K_MFT = np.array([2.65e-3, 5.33e-4, 2.71e-6, 3.69e-4, 9.81e-4])# 1st order reflection terminated to 5K
    ref1_2K_MFT = np.array([2.41e-3, 1.65e-3, 1.60e-3, 2.48e-3, 3.33e-3])# 1st order reflection terminated to 2K
    ref1_FP_MFT = np.array([3.20e-2, 9.77e-3, 1.41e-4, 1.64e-2, 6.14e-2])# 1st order reflection terminated to FP

    ref2_sky_MFT = np.array([4.01e-4, 3.92e-5, 5.70e-11, 1.04e-4, 1.55e-3])# 2nd order reflection goes to sky
    ref2_5K_MFT = np.array([1.63e-4, 2.62e-5, 1.36e-8, 5.50e-5, 3.76e-4])# 2nd order reflection terminated to 5K
    ref2_2K_MFT = np.array([0, 0, 0, 0, 0])# 2nd order reflection terminated to 2K
    ref2_apt_MFT = np.array([6.55e-5, 4.59e-6, 3.55e-11, 7.75e-6, 9.16e-5])# 2nd order reflection terminated to stop
 
    return  T_bath_MFT, T_len_MFT, T_hood_MFT, T_fil_MFT, T_L1_MFT, T_L2_MFT, T_abs_MFT, T_apt_MFT, T_hwp_MFT, T_baf_MFT, det_eff_MFT, freq_MFT, band_MFT, dpix_MFT, npix_MFT,ref_len_MFT, t_fil_MFT, n_fil_MFT, tan_fil_MFT, ref_fil_MFT, emiss_L1_MFT, emiss_L2_MFT, ref_L1_MFT, ref_L2_MFT, bf_MFT, Fnum_MFT, hwp_emiss_MFT, ref_hwp_MFT, pol_hwp_MFT, pol_dil_MFT, apt_spill_MFT, spill_5K_MFT, spill_2K_MFT, sky_eff_MFT, ref1_5K_MFT, ref1_2K_MFT, ref1_FP_MFT, ref2_sky_MFT, ref2_5K_MFT, ref2_2K_MFT, ref2_apt_MFT
# def MFT_Len([]):# detector lenslet [ MFT , MFT ]
#     t_len_MFT = np.array([[9.e-3,9.e-3]]) #thickness [MFT,MFT]
#     n_len_MFT = np.array([[3.4,3.4]]) #refractive index [MFT,MFT]
#     tan_len_MFT = np.array([[5.e-5,5.e-5]]) #loss tangent [MFT,MFT]
#     ref_len_MFT = np.array([[0.05,0.05]])  #reflectance [MFT,MFT]
#     return t_len_MFT, n_len_MFT, tan_len_MFT, ref_len_MFT
  
