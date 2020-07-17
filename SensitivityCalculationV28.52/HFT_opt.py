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
    det_eff_HFT = np.array([0.76,0.76,0.76,0.76,0.76])    # Detector efficiency including lenslets & horns
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
########################## HWP  ##############
    HWP_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # HWP seen by FP  => to be estimated
    abs1_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(CS-L1) reflected on HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs2_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(L1-L2) reflected on HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    Hood_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # 2K Hood reflected on HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT

    L1_HWP_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # L1 reflected on HWP seen by FP => to be estimated
    L2_HWP_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # L2 reflected on HWP seen by FP => to be estimated
    fil_HWP_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # filter reflected on HWP seen by FP => to be estimated

    abs1_L1_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(CS-L1) reflected on L1 then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    apt_L1_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # CS reflected on L1 then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    CMB_L1_HWP_spill_HFT  = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # Signal reflected on L1 then HWP seen by FP  => to be estimated

    abs2_L2_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(L1-L2) reflected on L2 then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs1_L2_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(CS-L1) reflected on L2 then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    apt_L2_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # CS reflected on L2 then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    CMB_L2_HWP_spill_HFT  = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # Signal reflected on L2 then HWP seen by FP  => to be estimated

    Hood_fil_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) #2K Hood reflected on filter seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs2_fil_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(L1-L2) reflected on filter then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs1_fil_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(CS-L1) reflected on filter then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    apt_fil_HWP_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # CS reflected on filter then HWP seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    CMB_fil_HWP_spill_HFT  = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # Signal reflected on filter then HWP seen by FP  => to be estimated

########################## APT  ##############
    apt_spill_HFT = np.array([0.130, 0.060, 0.020, 0.004, 0.003])

########################## L1   ###############
    L1_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # L1 seen by FP => to be estimated
    abs2_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(L1-L2) reflected on L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    Hood_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # 2K Hood reflected on L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    
    L2_L1_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # L2 reflected on L1 seen by FP => to be estimated
    fil_L1_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # filter reflected on L1 seen by FP => to be estimated

    abs2_L2_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(L1-L2) reflected on L2 then L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs1_L2_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(CS-L1) reflected on L2 then L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    apt_L2_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # CS reflected on L2 then L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    CMB_L2_L1_spill_HFT  = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # Signal reflected on L2 then L1 seen by FP  => to be estimated

    Hood_fil_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) #2K Hood reflected on filter then L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs2_fil_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(L1-L2) reflected on filter then L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs1_fil_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(CS-L1) reflected on filter then L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    apt_fil_L1_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # CS reflected on filter then L1 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    CMB_fil_L1_spill_HFT  = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # Signal reflected on filter then L1 seen by FP  => to be estimated

########################## L2   ###############
    L2_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # L2 seen by FP => to be estimated
    Hood_L2_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # 2K Hood reflected on L2 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    
    fil_L2_spill_HFT = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # filter reflected on L2 seen by FP => to be estimated

    Hood_fil_L2_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) #2K Hood reflected on filter then L2 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs2_fil_L2_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(L1-L2) reflected on filter then L2 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    abs1_fil_L2_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # Abs(CS-L1) reflected on filter then L2 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    apt_fil_L2_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) # CS reflected on filter then L2 seen by FP => Estimated at 5% in a first order with a naive geometric estimate HFT
    CMB_fil_L2_spill_HFT  = np.array([1.00, 1.00, 1.00, 1.00, 1.00]) # Signal reflected on filter then L2 seen by FP  => to be estimated

########################## FIL  ###############
    Hood_fil_spill_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) #2K Hood reflected on filter seen by FP => Estimated at 5% in a first order with a naive geometric estimate MFT


    return  T_bath_HFT, T_len_HFT, T_hood_HFT, T_fil_HFT, T_L1_HFT, T_L2_HFT, T_abs_HFT, T_apt_HFT, T_hwp_HFT, T_baf_HFT, det_eff_HFT, freq_HFT, band_HFT, dpix_HFT, npix_HFT,ref_len_HFT, t_fil_HFT, n_fil_HFT, tan_fil_HFT, ref_fil_HFT, emiss_L1_HFT, emiss_L2_HFT, ref_L1_HFT, ref_L2_HFT, bf_HFT, Fnum_HFT, hwp_emiss_HFT, ref_hwp_HFT, pol_hwp_HFT, pol_dil_HFT, HWP_spill_HFT, abs1_HWP_spill_HFT, abs2_HWP_spill_HFT, Hood_HWP_spill_HFT, L1_HWP_spill_HFT, L2_HWP_spill_HFT, fil_HWP_spill_HFT, abs1_L1_HWP_spill_HFT, apt_L1_HWP_spill_HFT, CMB_L1_HWP_spill_HFT, abs2_L2_HWP_spill_HFT, abs1_L2_HWP_spill_HFT, apt_L2_HWP_spill_HFT, CMB_L2_HWP_spill_HFT, Hood_fil_HWP_spill_HFT, abs2_fil_HWP_spill_HFT, abs1_fil_HWP_spill_HFT, apt_fil_HWP_spill_HFT, CMB_fil_HWP_spill_HFT, apt_spill_HFT, L1_spill_HFT, abs2_L1_spill_HFT, Hood_L1_spill_HFT, L2_L1_spill_HFT, fil_L1_spill_HFT, abs2_L2_L1_spill_HFT, abs1_L2_L1_spill_HFT, apt_L2_L1_spill_HFT, CMB_L2_L1_spill_HFT, Hood_fil_L1_spill_HFT, abs2_fil_L1_spill_HFT, abs1_fil_L1_spill_HFT, apt_fil_L1_spill_HFT, CMB_fil_L1_spill_HFT, L2_spill_HFT, Hood_L2_spill_HFT, fil_L2_spill_HFT, Hood_fil_L2_spill_HFT, abs2_fil_L2_spill_HFT, abs1_fil_L2_spill_HFT, apt_fil_L2_spill_HFT, CMB_fil_L2_spill_HFT, Hood_fil_spill_HFT 



    # L1_spill_HFT = np.array([0.0181, 0.0044, 0.0008, 0.0001, 0.0000])
    # L2_spill_HFT = np.array([0.0002, 0.0000, 0.0000, 0.0000, 0.0000])
    # total_spill_HFT = np.array([0.146, 0.064, 0.021, 0.004, 0.003])
    # spill_5Kenv_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) #Estimated at 5% in a first order with a naive geometric estimate
    # spill_2Khood_HFT = np.array([0.05, 0.05, 0.05, 0.05, 0.05]) #Estimated at 5% in a first order with a naive geometric estimate


  