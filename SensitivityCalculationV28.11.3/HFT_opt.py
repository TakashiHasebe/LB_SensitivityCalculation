import numpy as np

#################################################################
#################################################################
############################ V28.5.1 ############################
#################################################################
#################################################################

def HFT_param(): 

############################# HFT optics Temperatures ############################################
    T_bath_HFT = 0.1     # bolometer operation temp
    T_len_HFT = 0.1      # detector lenslet temp
    T_hood_HFT = 2.      # Detector hood
    T_fil_HFT = 2.       # filter temp
    T_L1_HFT = 5.        # lens temp
    T_L2_HFT = 5.        # lens temp
    T_abs_HFT = 5.       # Absorbers temp
    T_apt_HFT = 5.       # aperture temp
    T_hwp_HFT = 20.      # HWP temp
    T_baf_HFT = 5.       # baffle temp

################################# HFT Detectors parameters ##########################################
   # det_eff_HFT = np.array([0.76,0.76,0.76,0.76,0.76])    # Detector efficiency including lenslets & horns
    det_eff_HFT = np.array([0.75,0.75,0.75,0.75,0.75])    # Detector efficiency including lenslets & horns
    ref_det_HFT = np.array([0.1,0.1,0.1,0.1,0.1])    # Detector reflection to cold stop
    abs_det_HFT = np.array([0.15,0.15,0.15,0.15,0.15])    # Detector absorption at inner surface of the feedhorn or microstripline
    
    freq_HFT = np.array([195., 235., 280., 337., 402.])
    band_HFT = np.array([0.3,0.3,0.3, 0.3, 0.23])
    dpix_HFT = np.array([6.6, 6.6, 6.6, 6.6, 5.7])
    npix_HFT = np.array([127., 127., 127.,127.,169.])
    ref_len_HFT = 0.05  #reflectance
    # t_len_HFT = np.array([[9.e-3,9.e-3]]) #thickness
    # n_len_HFT = np.array([[3.4,3.4]]) #refractive index
    # tan_len_HFT = np.array([[5.e-5,5.e-5]]) #loss tangent
    # ref_len_HFT = 0.05,0.05  #reflectance

################################# HFT Filters parameters ##########################################
    t_fil_HFT = 5.e-3 #thickness
    n_fil_HFT = 1.5 #refractive index
    tan_fil_HFT = 2.3e-4 # loss tangent
    ref_fil_HFT = 0.05 # reflectance

################################# HFT Lenses parameters ##########################################
    emiss_L1_HFT = np.array([0.039, 0.044, 0.049, 0.058, 0.069]) #emissivity of first lens
    emiss_L2_HFT = np.array([0.038, 0.041, 0.045, 0.051, 0.060]) #emissivity of second lens
    ref_L1_HFT   = np.array([0.024, 0.024, 0.024, 0.024, 0.024]) #reflectance of first lens
    ref_L2_HFT   = np.array([0.024, 0.024, 0.024, 0.024, 0.024]) #reflectance of second lens

################################# HFT Aperture parameters ##########################################
    bf_HFT   = np.array([3.1, 3.1, 3.1, 3.1, 3.1]) # beam waist factor
    Fnum_HFT = np.array([2.5, 2.5, 2.5, 2.5, 2.5]) # F number

################################# HFT HWP parameters ##########################################
    hwp_emiss_HFT = np.array([0.053, 0.033, 0.025, 0.020, 0.023]) #emissivity
    ref_hwp_HFT   = np.array([0.025, 0.021, 0.025, 0.013, 0.009]) #reflectance
    pol_hwp_HFT   = np.array([0.981, 0.966, 0.955, 0.977, 0.984]) # polarization efficiency
    pol_dil_HFT   = np.array([1., 1., 1., 1., 1.]) # HWP rotation dilution factor
                            #0.972, 0.972, 0.972, 0.972, 0.972

################################# HFT Spill 5K/2K parameters ##########################################
#assuming -30dB sidelobe level with theta^-3 fanction
    apt_spill_HFT = np.array([8.93e-2, 3.76e-2, 1.47e-2, 1.57e-2, 1.53e-2])
    spill_5K_HFT = np.array([1.40e-2, 1.14e-2, 1.59e-2, 2.17e-2, 2.19e-2])
    spill_2K_HFT = np.array([2.17e-3, 3.08e-3, 4.29e-3, 6.03e-3, 6.36e-3])    
    sky_eff_HFT = np.array([7.47e-1, 8.21e-1, 8.40e-1, 7.94e-1, 7.14e-1])

    ref1_5K_HFT = np.array([4.90e-3, 9.99e-4, 3.72e-6, 6.41e-4, 2.18e-3])# 1st order reflection terminated to 5K
    ref1_2K_HFT = np.array([8.01e-4, 3.74e-4, 2.14e-4, 6.22e-4, 1.36e-3])# 1st order reflection terminated to 2K
    ref1_FP_HFT = np.array([3.82e-2, 1.20e-2, 9.48e-5, 2.03e-2, 7.39e-2])# 1st order reflection terminated to FP

    ref2_sky_HFT = np.array([5.73e-4, 5.76e-5, 5.55e-11, 1.53e-4, 2.11e-3])# 2nd order reflection goes to sky
    ref2_5K_HFT = np.array([2.27e-4, 3.63e-5, 4.64e-8, 1.13e-4, 7.87e-4])# 2nd order reflection terminated to 5K
    ref2_2K_HFT = np.array([0, 0, 0, 0, 0])# 2nd order reflection terminated to 2K
    ref2_apt_HFT = np.array([4.85e-5, 3.61e-6, 4.23e-11, 6.38e-6, 8.62e-5])# 2nd order reflection terminated to stop

    return  T_bath_HFT, T_len_HFT, T_hood_HFT, T_fil_HFT, T_L1_HFT, T_L2_HFT, T_abs_HFT, T_apt_HFT, T_hwp_HFT, T_baf_HFT, det_eff_HFT, ref_det_HFT, abs_det_HFT, freq_HFT, band_HFT, dpix_HFT, npix_HFT,ref_len_HFT, t_fil_HFT, n_fil_HFT, tan_fil_HFT, ref_fil_HFT, emiss_L1_HFT, emiss_L2_HFT, ref_L1_HFT, ref_L2_HFT, bf_HFT, Fnum_HFT, hwp_emiss_HFT, ref_hwp_HFT, pol_hwp_HFT, pol_dil_HFT, apt_spill_HFT, spill_5K_HFT, spill_2K_HFT, sky_eff_HFT , ref1_5K_HFT, ref1_2K_HFT, ref1_FP_HFT, ref2_sky_HFT, ref2_5K_HFT, ref2_2K_HFT, ref2_apt_HFT


  
