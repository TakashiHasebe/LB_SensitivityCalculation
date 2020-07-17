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
    apt_spill_HFT = np.array([2.57e-2, 1.32e-2, 5.66e-3, 5.90e-3, 5.79e-3])
    spill_5K_HFT = np.array([6.56e-2, 6.53e-2, 6.43e-2, 6.70e-2, 6.67e-2])
    spill_2K_HFT = np.array([6.33e-2, 6.24e-2, 6.16e-2, 6.56e-2, 6.79e-2])    
    sky_eff_HFT = np.array([7.50e-1, 8.18e-1, 8.42e-1, 8.13e-1, 7.55e-1])

    ref1_5K_HFT = np.array([2.80e-3, 5.93e-4, 4.12e-7, 4.32e-4, 1.18e-3])# 1st order reflection terminated to 5K
    ref1_2K_HFT = np.array([8.68e-4, 4.14e-4, 3.55e-4, 9.37e-4, 2.02e-3])# 1st order reflection terminated to 2K
    ref1_FP_HFT = np.array([3.52e-2, 1.09e-2, 1.41e-4, 1.81e-2, 6.76e-2])# 1st order reflection terminated to FP

    ref2_sky_HFT = np.array([4.89e-4, 4.81e-5, 6.91e-11, 1.25e-4, 1.85e-3])# 2nd order reflection goes to sky
    ref2_5K_HFT = np.array([1.58e-4, 2.76e-5, 1.50e-8, 6.58e-5, 4.93e-4])# 2nd order reflection terminated to 5K
    ref2_2K_HFT = np.array([2.25e-5, 1.72e-6, 1.11e-10, 3.84e-6, 4.54e-5])# 2nd order reflection terminated to 2K
    ref2_apt_HFT = np.array([7.62e-5, 5.34e-6, 4.12e-11, 9.53e-6, 1.18e-4])# 2nd order reflection terminated to stop

    return  T_bath_HFT, T_len_HFT, T_hood_HFT, T_fil_HFT, T_L1_HFT, T_L2_HFT, T_abs_HFT, T_apt_HFT, T_hwp_HFT, T_baf_HFT, det_eff_HFT, ref_det_HFT, abs_det_HFT, freq_HFT, band_HFT, dpix_HFT, npix_HFT,ref_len_HFT, t_fil_HFT, n_fil_HFT, tan_fil_HFT, ref_fil_HFT, emiss_L1_HFT, emiss_L2_HFT, ref_L1_HFT, ref_L2_HFT, bf_HFT, Fnum_HFT, hwp_emiss_HFT, ref_hwp_HFT, pol_hwp_HFT, pol_dil_HFT, apt_spill_HFT, spill_5K_HFT, spill_2K_HFT, sky_eff_HFT , ref1_5K_HFT, ref1_2K_HFT, ref1_FP_HFT, ref2_sky_HFT, ref2_5K_HFT, ref2_2K_HFT, ref2_apt_HFT


  
