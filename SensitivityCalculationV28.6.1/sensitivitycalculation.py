import numpy as np
import function as f
import fp as fp
import opt 
import numpy as np
import MFT_opt as MFT_opt
import HFT_opt as HFT_opt

pi = f.pi
k_b = f.k_b
c= f.c
h= f.h


########################### Psat factor##########################
Pfac = 2.5
########################### Observation Time Efficiency ##########################
DC = 0.85 # Observation duty cycle
CR = 0.95 # Cosmic ray dead time
CT = 0.95 # Contingency

#######################################################################
Freq = np.array([40., 50., 60., 68., 78., 89., 100., 119., 140., 166., 195., 235., 280, 337., 402.]);
m1=4   
n1=3
n2=5 # nb of bands (HFT)
n3=5 # nb of bands (MFT)

num=10000

############################# Optics Temperatures ################################

T_bath, T_cmb, T_hwp_LFT,T_apt_LFT, T_mir, T_fil, T_FPhood, T_baf, Tr_hwp,Tr_mir,Tr_fil,Tr_det = opt.Temp_Opt()

################################ FP parameters ##########################################
freqLFT, bandLFT, dpixLFT, npixLFT = fp.LFT_FP()

################################# Opics parameters ##########################################
#LFT
hwp_eff_LFT, ref_hwp_LFT, hwp_emiss_LFT, pol_hwp_LFT, df_LFT = opt.LFT_Hwp()
Spill_fp, Spill_as, Spill_ts, Spill_hm, Apt_eff = opt.LFT_Spill()
bf_LFT, F_LFT = opt.LFT_Apt()
det_eff_LFT = opt.LFT_Det() 

#HFT

################################# HFT parameters ##########################################
T_bath_HFT, T_len_HFT, T_hood_HFT, T_fil_HFT, T_L1_HFT, T_L2_HFT, T_abs_HFT, T_apt_HFT, T_hwp_HFT, T_baf_HFT, det_eff_HFT, freq_HFT, band_HFT, dpix_HFT, npix_HFT,ref_len_HFT, t_fil_HFT, n_fil_HFT, tan_fil_HFT, ref_fil_HFT, emiss_L1_HFT, emiss_L2_HFT, ref_L1_HFT, ref_L2_HFT, bf_HFT, Fnum_HFT, hwp_emiss_HFT, ref_hwp_HFT, pol_hwp_HFT, pol_dil_HFT, apt_spill_HFT, L1_spill_HFT, L2_spill_HFT, total_spill_HFT, spill_5Kenv_HFT, spill_2Khood_HFT = HFT_opt.HFT_param()

################################# MFT parameters ##########################################
T_bath_MFT, T_len_MFT, T_hood_MFT, T_fil_MFT, T_L1_MFT, T_L2_MFT, T_abs_MFT, T_apt_MFT, T_hwp_MFT, T_baf_MFT, det_eff_MFT, freq_MFT, band_MFT, dpix_MFT, npix_MFT,ref_len_MFT, t_fil_MFT, n_fil_MFT, tan_fil_MFT, ref_fil_MFT, emiss_L1_MFT, emiss_L2_MFT, ref_L1_MFT, ref_L2_MFT, bf_MFT, Fnum_MFT, hwp_emiss_MFT, ref_hwp_MFT, pol_hwp_MFT, pol_dil_MFT, apt_spill_MFT, L1_spill_MFT, L2_spill_MFT, spill_5Kenv_MFT, total_spill_MFT, spill_2Khood_MFT = MFT_opt.MFT_param()    

                   
#Mirror 
epsilon, rho, rms = opt.Mir()


#2K filter
t_fil, n_fil, tan_fil, ref_fil =opt.Fil()

# detector lenslet
t_len, n_len, tan_len, ref_len =opt.Len()
       
def LFT_MHFT_sensitivity_calculator(Freq=Freq, DC=DC, CR =CR, CT=CT, Pfac= Pfac, T_bath=T_bath, T_baf=T_baf, T_fil=T_fil, T_FPhood=T_FPhood, T_apt_LFT=T_apt_LFT, T_apt_MFT=T_apt_MFT, T_apt_HFT=T_apt_HFT, T_hwp_LFT=T_hwp_LFT, T_hwp_HFT=T_hwp_HFT, det_eff_LFT=det_eff_LFT,  det_eff_HFT=det_eff_HFT):

    t=3.*365.*24.*60.*60.*DC*CR*CT;# 3 years ovservation time including cosmic ray loss (CR), contingency (CT) and observation duty cycle (DC)


    ####################### LFT noise calculation ############################
    p_opt_arr = np.zeros(num)
    nep_opt_arr = np.zeros(num)
    dpdt_arr = np.zeros(num)
    NETarrLFT=([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])

#    print "Freq [GHz] , Popt [pW] , NEPph [aW/rtHz] , NEPg [aW/rtHz] , NEPread [aW/rtHz] , NEPint [aW/rtHz] , NEPext [aW/rtHz] , NEPdet [aW/rtHz] , NETdet [microK/rtHz] , NETarr [microK/rtHz] "


    for i in range(0,m1):
        for j in range(0,n1):
            freq_l, freq_h = f.FreqRange(freqLFT[i][j],bandLFT[i][j])
            hwp_eff = hwp_eff_LFT[i][j]
            spill_fp = Spill_fp[i][j] #Spillover at FP hood
            spill_as = Spill_as[i][j] #Spillover at aperture stop
            spill_ts = Spill_ts[i][j] #Spillover at telescope shield
            spill_hm = Spill_hm[i][j] #Spillover at HWP mount
            apt_eff = Apt_eff[i][j]
            
            for k in range(0,num):
                freq = freq_l+(freq_h - freq_l)*k/(num-1)
                
                pm_emiss, pm_eff, pm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
                sm_emiss, sm_eff, sm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
                fil_emiss, fil_eff = f.Trm(t_fil, n_fil, tan_fil, freq*1.e9, ref_fil)
                ref_len = 0.05
                len_emiss, len_eff = f.Trm(t_len, n_len, tan_len, freq*1.e9, ref_len)

                p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*det_eff_LFT[i][j]

                p_hwp = f.BB(freq*1.e9,T_hwp_LFT)*hwp_emiss_LFT[i][j]*apt_eff*pm_eff*sm_eff*fil_eff*det_eff_LFT[i][j]
                p_hwp_ref = f.BB(freq*1.e9,Tr_hwp)*ref_hwp_LFT[i][j]*apt_eff*pm_eff*sm_eff*fil_eff*det_eff_LFT[i][j]
                p_hwp = p_hwp + p_hwp_ref

          
                p_pm = f.BB(freq*1.e9,T_mir)*pm_emiss*sm_eff*fil_eff*det_eff_LFT[i][j]
                p_pm_ref = f.BB(freq*1.e9,Tr_mir)*pm_loss*sm_eff*fil_eff*det_eff_LFT[i][j]
                p_pm = p_pm + p_pm_ref
                

                p_sm = f.BB(freq*1.e9,T_mir)*sm_emiss*fil_eff*det_eff_LFT[i][j]
                p_sm_ref = f.BB(freq*1.e9,Tr_mir)*sm_loss*fil_eff*det_eff_LFT[i][j]
                p_sm = p_sm + p_sm_ref

                p_fp =  f.BB(freq*1.e9,T_FPhood)*spill_fp*fil_eff*det_eff_LFT[i][j]
                p_as = f.BB(freq*1.e9,T_apt_LFT)*spill_as*fil_eff*det_eff_LFT[i][j]
                p_ts =  f.BB(freq*1.e9,T_baf)*spill_ts*fil_eff*det_eff_LFT[i][j]
                p_hm =  f.BB(freq*1.e9,T_hwp_LFT)*spill_hm*fil_eff*det_eff_LFT[i][j]
                
                 
                p_fil = f.BB(freq*1.e9,T_fil)*fil_emiss*det_eff_LFT[i][j]
                p_fil_ref = f.BB(freq*1.e9,Tr_fil)*ref_fil*det_eff_LFT[i][j]
                p_fil = p_fil + p_fil_ref
                
                p_det = f.BB(freq*1.e9,Tr_det)*(1-det_eff_LFT[i][j])
         
                p_opt = p_cmb + p_hwp +  p_pm + p_sm + p_fp + p_as + p_ts + p_hm + p_fil + p_det 

                eff = hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*det_eff_LFT[i][j]*pol_hwp_LFT[i][j]*df_LFT[i][j]
                
                p_opt_arr[k] = p_opt
                nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
                nep_opt_arr[k] = nep_opt
                dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
                dpdt_arr[k] = dpdt

            Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW

            Psat = Pfac*Popt    
           
            NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
            NEPth = np.sqrt(4.*k_b*Psat*1.e-12*T_bath*(3.+1.)**2./(2.*3.+3.)*(1.71**(2.*3.+3.)-1.)/((1.71**(3.+1.)-1.)**2.))*1.e18
            NEPread = np.sqrt(Popt/0.5)*3.5
            NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPread**2.)
            NEPext = np.sqrt(0.32)*np.sqrt(NEPint**2.)
            NEPdet = np.sqrt(NEPint**2. + NEPext**2.)
            
            DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
            NETdet = NEPdet*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
            NETarrLFT[i][j] = NETdet/np.sqrt(2.*npixLFT[i][j]*0.8)  

#            print round(freqLFT[i][j],2)," , ",round(Popt,8)," , ",round(NEPopt,8)," , ",round(NEPth,8)," , ",round(NEPread,8)," , ",round(NEPint,8)," , ",round(NEPext,8)," , ",round(NEPdet,8)," , ",round(NETdet,8)," , ",round(NETarrLFT[i][j],8)

####################### MFT noise calculation ############################

    NETarrMFT=([0.,0.,0.,0.,0])

    for j in range(0,n3):

        freq_l, freq_h = f.FreqRange(freq_MFT[j],band_MFT[j])

        for k in range(0,num):
            freq = freq_l+(freq_h - freq_l)*k/(num)
            hwp_eff = 1.- hwp_emiss_MFT[j] - ref_hwp_MFT[j]
        
            apt_emiss, apt_eff = f.Aperture(dpix_MFT[j]*1.e-3, bf_MFT[j], Fnum_MFT[j], freq*1.e9)
            #apt_eff = apt_eff_MFT[j]

            L1_eff = 1. - emiss_L1_MFT[j] - ref_L1_MFT[j]
            L2_eff = 1. - emiss_L2_MFT[j] - ref_L2_MFT[j]

            fil_emiss, fil_eff = f.Trm(t_fil_MFT, n_fil_MFT, tan_fil_MFT, freq*1.e9, ref_fil_MFT)

            p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_MFT[j] # 

            # HWP => BB20KxE_HWP + [%BB5K + BB 5KxE_L1+BB5KxE_HWPxR_L1]xR_HWP
            p_hwp = f.BB(freq*1.e9,T_hwp_MFT)*hwp_emiss_MFT[j]*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_MFT[j]
            p_hwp_ref = (f.BB(freq*1.e9,T_L1_MFT)*emiss_L1_MFT[j]+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff+f.BB(freq*1.e9,T_hwp_MFT)*hwp_emiss_MFT[j]*apt_eff+f.BB(freq*1.e9,T_apt_MFT)*apt_spill_MFT[j])*ref_L1_MFT[j])*ref_hwp_MFT[j]*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_MFT[j]
            p_hwp = p_hwp + p_hwp_ref

            #p_apt = f.BB(freq*1.e9,T_apt_MFT)*apt_emiss*L1_eff*L2_eff*fil_eff*det_eff_MFT[j]
            p_apt = f.BB(freq*1.e9,T_apt_MFT)*apt_spill_MFT[j]*L1_eff*L2_eff*fil_eff*det_eff_MFT[j]

            #L1 => BB5Kx(E_L1+L1_Spill)+[BB5KxL1_Spill+BB5KxE_L2+(CMBxTr+BB5KxE_L1xTr+BB20KxE_HWPxTr+BB5KxE_CASxTr)xR_L2]xR_L1
            p_L1 = f.BB(freq*1.e9,T_L1_MFT)*(emiss_L1_MFT[j]+L1_spill_MFT[j])*L2_eff*fil_eff*det_eff_MFT[j]
            p_L1_ref = (f.BB(freq*1.e9,T_abs_MFT)*L1_spill_MFT[j]+f.BB(freq*1.e9,T_L2_MFT)*emiss_L2_MFT[j]+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff+f.BB(freq*1.e9,T_hwp_MFT)*hwp_emiss_MFT[j]*apt_eff*L1_eff+f.BB(freq*1.e9,T_apt_MFT)*apt_spill_MFT[j]*L1_eff+f.BB(freq*1.e9,T_L1_MFT)*emiss_L1_MFT[j])*ref_L2_MFT[j])*ref_L1_MFT[j]*L2_eff*fil_eff*det_eff_MFT[j]
            p_L1 = p_L1 + p_L1_ref
            
            #L2 => BB5Kx(E_L2+L2_Spill) + [BB2KxL2_Spill+BB2KxE_Fil + (CMBxTr + BB5KxE_L1xTr + BB5KxE_L2xTr + BB20KxE_HWPxTr + BB5KxE_CASxTr)xR_Fil]xR_L2
            p_L2 = f.BB(freq*1.e9,T_L2_MFT)*(emiss_L2_MFT[j]+L2_spill_MFT[j])*fil_eff*det_eff_MFT[j]
            p_L2_ref = (f.BB(freq*1.e9,T_hood_MFT)*L2_spill_MFT[j]+f.BB(freq*1.e9,T_fil_MFT)*fil_emiss+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff*L2_eff+f.BB(freq*1.e9,T_hwp_MFT)*hwp_emiss_MFT[j]*apt_eff*L1_eff*L2_eff+f.BB(freq*1.e9,T_apt_MFT)*apt_spill_MFT[j]*L1_eff*L2_eff+f.BB(freq*1.e9,T_L1_MFT)*emiss_L1_MFT[j]*L2_eff)*ref_fil_MFT)*ref_L2_MFT[j]*fil_eff*det_eff_MFT[j]
            p_L2 = p_L2 + p_L2_ref

            #Fil => BB2KxFil +[BB0.1KxE_Len + %BB2K + (CMBxTr + BB5KxE_L1xTr + BB5KxE_L2xTr + BB20KxE_HWPxTr + BB5KxE_CASxTr)xR_FLen]xR_Fil
            p_fil = f.BB(freq*1.e9,T_fil_MFT)*fil_emiss*det_eff_MFT[j]
            p_fil_ref = (f.BB(freq*1.e9,T_hood_MFT)*spill_2Khood_MFT[j]+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff*L2_eff*fil_eff+f.BB(freq*1.e9,T_hwp_MFT)*hwp_emiss_MFT[j]*apt_eff*L1_eff*L2_eff*fil_eff+f.BB(freq*1.e9,T_apt_MFT)*apt_spill_MFT[j]*L1_eff*L2_eff*fil_eff+f.BB(freq*1.e9,T_L1_MFT)*emiss_L1_MFT[j]*L2_eff*fil_eff+f.BB(freq*1.e9,T_L2_MFT)*emiss_L2_MFT[j]*fil_eff+f.BB(freq*1.e9,T_fil_MFT)*fil_emiss)*ref_len_MFT)*ref_fil_MFT*det_eff_MFT[j]
            p_fil = p_fil + p_fil_ref

            p_det = f.BB(freq*1.e9,T_bath_MFT)*(1-det_eff_MFT[j])

            p_opt = p_cmb + p_hwp + p_apt + p_L1 + p_L2 + p_fil + p_det 
            p_opt_arr[k] = p_opt

            eff = hwp_eff*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_MFT[j]*pol_hwp_MFT[j]


            nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
            nep_opt_arr[k] = nep_opt

            dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
            dpdt_arr[k] = dpdt

            # if(freq_MFT[j] == freq):
            #     print ("p_hwp=",p_hwp,"p_apt=",p_apt,"p_L1=",p_L1,"p_L2=",p_L2,"p_fil=",p_fil,"p_det=",p_det, "p_opt=",p_opt)

        Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
        Psat = Pfac*Popt
        
        NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
        NEPth = np.sqrt(4.*k_b*Psat*1.e-12*T_bath_MFT*(3.+1.)**2./(2.*3.+3.)*(1.71**(2.*3.+3.)-1.)/((1.71**(3.+1.)-1.)**2.))*1.e18
        NEPread = np.sqrt(Popt/0.5)*3.5
        NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPread**2.)
        NEPext = np.sqrt(0.32)*np.sqrt(NEPint**2.)
        NEPdet = np.sqrt(NEPint**2. + NEPext**2.)
        DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
        NETdet = NEPdet*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
        NETarrMFT[j] = NETdet/np.sqrt(2.*npix_MFT[j]*0.8)  

####################### HFT noise calculation ############################

    NETarrHFT=([0.,0.,0.,0.,0])

    for j in range(0,n2):

        freq_l, freq_h = f.FreqRange(freq_HFT[j],band_HFT[j])

        for k in range(0,num):
            freq = freq_l+(freq_h - freq_l)*k/(num)
            hwp_eff = 1.- hwp_emiss_HFT[j] - ref_hwp_HFT[j]
        
            apt_emiss, apt_eff = f.Aperture(dpix_HFT[j]*1.e-3, bf_HFT[j], Fnum_HFT[j], freq*1.e9)
            #apt_eff = apt_eff_HFT[j]

            L1_eff = 1. - emiss_L1_HFT[j] - ref_L1_HFT[j]
            L2_eff = 1. - emiss_L2_HFT[j] - ref_L2_HFT[j]

            fil_emiss, fil_eff = f.Trm(t_fil_HFT, n_fil_HFT, tan_fil_HFT, freq*1.e9, ref_fil_HFT)

            p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_HFT[j] # 

            # HWP => BB20KxE_HWP + [%BB5K + BB 5KxE_L1+BB5KxE_HWPxR_L1]xR_HWP
            p_hwp = f.BB(freq*1.e9,T_hwp_HFT)*hwp_emiss_HFT[j]*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_HFT[j]
            p_hwp_ref = (f.BB(freq*1.e9,T_L1_HFT)*emiss_L1_HFT[j]+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff+f.BB(freq*1.e9,T_hwp_HFT)*hwp_emiss_HFT[j]*apt_eff+f.BB(freq*1.e9,T_apt_HFT)*apt_spill_HFT[j])*ref_L1_HFT[j])*ref_hwp_HFT[j]*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_HFT[j]
            p_hwp = p_hwp + p_hwp_ref

            #p_apt = f.BB(freq*1.e9,T_apt_HFT)*apt_emiss*L1_eff*L2_eff*fil_eff*det_eff_HFT[j]
            p_apt = f.BB(freq*1.e9,T_apt_HFT)*apt_spill_HFT[j]*L1_eff*L2_eff*fil_eff*det_eff_HFT[j]

            #L1 => BB5KxE_L1+[BB5KxE_L2+%BB5K+(CMBxTr+BB5KxE_L1xTr+BB20KxE_HWPxTr+BB5KxE_CASxTr)xR_L2]xR_L1
            p_L1 = f.BB(freq*1.e9,T_L1_HFT)*(emiss_L1_HFT[j]+L1_spill_HFT[j])*L2_eff*fil_eff*det_eff_HFT[j]
            p_L1_ref = (f.BB(freq*1.e9,T_abs_HFT)*L1_spill_HFT[j]+f.BB(freq*1.e9,T_L2_HFT)*emiss_L2_HFT[j]+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff+f.BB(freq*1.e9,T_hwp_HFT)*hwp_emiss_HFT[j]*apt_eff*L1_eff+f.BB(freq*1.e9,T_apt_HFT)*apt_spill_HFT[j]*L1_eff+f.BB(freq*1.e9,T_L1_HFT)*emiss_L1_HFT[j])*ref_L2_HFT[j])*ref_L1_HFT[j]*L2_eff*fil_eff*det_eff_HFT[j]
            p_L1 = p_L1 + p_L1_ref
            
            #L2 => BB5KxE_L2 + [BB2KxE_Fil + + %BB2K + (CMBxTr + BB5KxE_L1xTr + BB5KxE_L2xTr + BB20KxE_HWPxTr + BB5KxE_CASxTr)xR_Fil]xR_L2
            p_L2 = f.BB(freq*1.e9,T_L2_HFT)*(emiss_L2_HFT[j]+L2_spill_HFT[j])*fil_eff*det_eff_HFT[j]
            p_L2_ref = (f.BB(freq*1.e9,T_hood_HFT)*L2_spill_HFT[j]+f.BB(freq*1.e9,T_fil_HFT)*fil_emiss+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff*L2_eff+f.BB(freq*1.e9,T_hwp_HFT)*hwp_emiss_HFT[j]*apt_eff*L1_eff*L2_eff+f.BB(freq*1.e9,T_apt_HFT)*apt_spill_HFT[j]*L1_eff*L2_eff+f.BB(freq*1.e9,T_L1_HFT)*emiss_L1_HFT[j]*L2_eff)*ref_fil_HFT)*ref_L2_HFT[j]*fil_eff*det_eff_HFT[j]
            p_L2 = p_L2 + p_L2_ref

            #Fil => BB2KxFil +[BB0.1KxE_Len + %BB2K + (CMBxTr + BB5KxE_L1xTr + BB5KxE_L2xTr + BB20KxE_HWPxTr + BB5KxE_CASxTr)xR_FLen]xR_Fil
            p_fil = f.BB(freq*1.e9,T_fil_HFT)*fil_emiss*det_eff_HFT[j]
            p_fil_ref = (f.BB(freq*1.e9,T_hood_HFT)*spill_2Khood_HFT[j]+(f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*L1_eff*L2_eff*fil_eff+f.BB(freq*1.e9,T_hwp_HFT)*hwp_emiss_HFT[j]*apt_eff*L1_eff*L2_eff*fil_eff+f.BB(freq*1.e9,T_apt_HFT)*apt_spill_HFT[j]*L1_eff*L2_eff*fil_eff+f.BB(freq*1.e9,T_L1_HFT)*emiss_L1_HFT[j]*L2_eff*fil_eff+f.BB(freq*1.e9,T_L2_HFT)*emiss_L2_HFT[j]*fil_eff+f.BB(freq*1.e9,T_fil_HFT)*fil_emiss)*ref_len_HFT)*ref_fil_HFT*det_eff_HFT[j]
            p_fil = p_fil + p_fil_ref

            p_det = f.BB(freq*1.e9,T_bath_HFT)*(1-det_eff_HFT[j])

            p_opt = p_cmb + p_hwp + p_apt + p_L1 + p_L2 + p_fil + p_det 
            p_opt_arr[k] = p_opt

            eff = hwp_eff*apt_eff*L1_eff*L2_eff*fil_eff*det_eff_HFT[j]*pol_hwp_HFT[j]


            nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
            nep_opt_arr[k] = nep_opt

            dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
            dpdt_arr[k] = dpdt

            # if(freq_HFT[j] == freq):
            #     print ("p_hwp=",p_hwp,"p_apt=",p_apt,"p_L1=",p_L1,"p_L2=",p_L2,"p_fil=",p_fil,"p_det=",p_det, "p_opt=",p_opt)

        Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
        
        Psat = Pfac*Popt
        
        NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
        NEPth = np.sqrt(4.*k_b*Psat*1.e-12*T_bath_HFT*(3.+1.)**2./(2.*3.+3.)*(1.71**(2.*3.+3.)-1.)/((1.71**(3.+1.)-1.)**2.))*1.e18
        NEPread = np.sqrt(Popt/0.5)*3.5
        NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPread**2.)
        NEPext = np.sqrt(0.32)*np.sqrt(NEPint**2.)
        NEPdet = np.sqrt(NEPint**2. + NEPext**2.)
        DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
        NETdet = NEPdet*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
        NETarrHFT[j] = NETdet/np.sqrt(2.*npix_HFT[j]*0.8)  


    NETarr = np.zeros(15)        
    NETarr[0]= NETarrLFT[0][0]; #40 GHz
    NETarr[1]= NETarrLFT[1][0]; #50 GHz
    NETarr[2]= NETarrLFT[0][1]; #60 GHz
      
    NETarr[3]= np.sqrt(1./(1./pow(NETarrLFT[1][1],2.) + 1./pow(NETarrLFT[2][0],2.)));#68 GHz
    NETarr[4]= np.sqrt(1./(1./pow(NETarrLFT[0][2],2.) + 1./pow(NETarrLFT[3][0],2.)));#78 GHz
    NETarr[5]= np.sqrt(1./(1./pow(NETarrLFT[1][2],2.) + 1./pow(NETarrLFT[2][1],2.)));#89 GHz
    NETarr[6]= np.sqrt(1./(1./pow(NETarrLFT[3][1],2.) + 1./pow(NETarrMFT[0],2.)));#100 GHz
    NETarr[7]= np.sqrt(1./(1./pow(NETarrLFT[2][2],2.) + 1./pow(NETarrMFT[1],2.)));#119 GHz
    NETarr[8]= np.sqrt(1./(1./pow(NETarrLFT[3][2],2.) + 1./pow(NETarrMFT[2],2.)));#140 GHz

    NETarr[9]= NETarrMFT[3];#166 GHz
    NETarr[10]= np.sqrt(1./(1./pow(NETarrMFT[4],2.) + 1./pow(NETarrHFT[0],2.)));#195 GHz
    NETarr[11]= NETarrHFT[1];#235 GHz
    NETarr[12]= NETarrHFT[2];#280 GHz
    NETarr[13]= NETarrHFT[3];#335 GHz
    NETarr[14]= NETarrHFT[4];#402 GHz

    Sensitivity =  f.Sigma( NETarr, t);
    Sum_sens = 0

    print ("Freq [GHz] , NETarr [microK/rtHz] , Sensitivity [microK -arcmin]")

    for i in range (0,15):
        Sum_sens = Sum_sens + 1./(Sensitivity[i]**2.) 
        print (Freq[i]," , ",round(NETarr[i],2)," , ",round(Sensitivity[i],2))
    Ave_sens = np.sqrt(1./Sum_sens)   

    print ("Averaged_sensitivity = ",round(Ave_sens,2))

    print ("T_HWP= [",T_hwp_LFT,T_hwp_HFT,T_hwp_MFT,"] K,", "T_stop= [",T_apt_LFT,T_apt_MFT, T_apt_HFT,"] K, Duty cycle= ",DC," T_bath= ",T_bath)

    return Freq, Sensitivity

