import numpy as np
import function as f
import fp as fp
import opt 
import numpy as np

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
m2=2
n2=5

num=10000

############################# Optics Temperatures ################################

T_bath, T_cmb, T_hwp_LFT,T_hwp_HFT,T_apt_LFT, T_apt_HFT, T_mir, T_fil, T_FPhood, T_len, T_lens, T_baf, Tr_hwp,Tr_mir,Tr_fil,Tr_len,Tr_lens,Tr_horn,Tr_det = opt.Temp_Opt()

################################ FP parameters ##########################################
freqLFT, bandLFT, dpixLFT, npixLFT = fp.LFT_FP()
freqHFT, bandHFT, dpixHFT, npixHFT = fp.HFT_FP()

################################# Opics parameters ##########################################
#LFT
hwp_eff_LFT, ref_hwp_LFT, hwp_emiss_LFT, pol_hwp_LFT, df_LFT = opt.LFT_Hwp()
Spill_fp, Spill_as, Spill_ts, Spill_hm, Apt_eff = opt.LFT_Spill()
bf_LFT, F_LFT = opt.LFT_Apt()
det_eff_LFT = opt.LFT_Det() 

#HFT
hwp_emiss_HFT, ref_hwp_HFT, pol_hwp_HFT, df_HFT = opt.HFT_Hwp() # MM-HWP
bf_HFT, Fnum_HFT = opt.HFT_Apt() 
det_eff_HFT = opt.HFT_Det() 
ref_horn = 0.05 # reflectance of feedhorn
emiss_L1, emiss_L2, ref_L1, ref_L2 = opt.HFT_Lens()
                   
#Mirror 
epsilon, rho, rms = opt.Mir()


#2K filter
t_fil, n_fil, tan_fil, ref_fil =opt.Fil()

# detector lenslet
t_len, n_len, tan_len, ref_len =opt.Len()
       
def LFT_MHFT_sensitivity_calculator(Freq=Freq, DC=DC, CR =CR, CT=CT, Pfac= Pfac, T_bath=T_bath, T_baf=T_baf, T_fil=T_fil, T_FPhood=T_FPhood, T_apt_LFT=T_apt_LFT, T_apt_HFT=T_apt_HFT, T_hwp_LFT=T_hwp_LFT, T_hwp_HFT=T_hwp_HFT, det_eff_LFT=det_eff_LFT,  det_eff_HFT=det_eff_HFT):

    t=3.*365.*24.*60.*60.*DC*CR*CT;# 3 years ovservation time including cosmic ray loss (CR), contingency (CT) and observation duty cycle (DC)


    ####################### LFT noise calculation ############################
    p_opt_arr = np.zeros(num)
    p_cmb_arr = np.zeros(num)
    p_apt_arr = np.zeros(num)
    p_hwp_arr = np.zeros(num)
    p_lens_arr = np.zeros(num)
    p_len_arr = np.zeros(num)
    p_fil_arr = np.zeros(num)
    p_fp_arr = np.zeros(num)
    p_as_arr = np.zeros(num)
    p_ts_arr = np.zeros(num)
    p_hm_arr = np.zeros(num)
    nep_opt_arr = np.zeros(num)
    dpdt_arr = np.zeros(num)
    NETarrLFT=([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])

    print "Freq [GHz] , Popt [pW] , NEPph [aW/rtHz] , NEPg [aW/rtHz] , NEPread [aW/rtHz] , NEPint [aW/rtHz] , NEPext [aW/rtHz] , NEPdet [aW/rtHz] , NETdet [microK/rtHz] , NETarr [microK/rtHz] "


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
                #freq = freq_l+(freq_h - freq_l)*k/num  
                #eff_apt, spill_apt = f.Aperture(dpixLFT[i][j]*1e-3,bf_LFT,F_LFT,freq*1.e9)-apt_eff #Spillover at cold aperture stop

                #if ( Spill_ts[i][j]-spill_apt >= 0.):
                    #spill_ts = Spill_ts[i][j]-spill_apt
                #else :
                    #spill_ts = 0.
                
                pm_emiss, pm_eff, pm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
                sm_emiss, sm_eff, sm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
                fil_emiss, fil_eff = f.Trm(t_fil, n_fil, tan_fil, freq*1.e9, ref_fil)
                ref_len = 0.05
                len_emiss, len_eff = f.Trm(t_len, n_len, tan_len, freq*1.e9, ref_len)

                p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT[i][j]

                p_hwp = f.BB(freq*1.e9,T_hwp_LFT)*hwp_emiss_LFT[i][j]*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT[i][j]
                p_hwp_ref = f.BB(freq*1.e9,Tr_hwp)*ref_hwp_LFT[i][j]*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT[i][j]
                p_hwp = p_hwp + p_hwp_ref

          
                #p_fb = f.BB(freq*1.e9,T_baf)*spill_fb*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT[i][j]

                p_pm = f.BB(freq*1.e9,T_mir)*pm_emiss*sm_eff*fil_eff*len_eff*det_eff_LFT[i][j]
                p_pm_ref = f.BB(freq*1.e9,Tr_mir)*pm_loss*sm_eff*fil_eff*len_eff*det_eff_LFT[i][j]
                p_pm = p_pm + p_pm_ref
                

                p_sm = f.BB(freq*1.e9,T_mir)*sm_emiss*fil_eff*len_eff*det_eff_LFT[i][j]
                p_sm_ref = f.BB(freq*1.e9,Tr_mir)*sm_loss*fil_eff*len_eff*det_eff_LFT[i][j]
                p_sm = p_sm + p_sm_ref

                p_fp =  f.BB(freq*1.e9,T_FPhood)*spill_fp*fil_eff*len_eff*det_eff_LFT[i][j]
                p_as = f.BB(freq*1.e9,T_apt_LFT)*spill_as*fil_eff*len_eff*det_eff_LFT[i][j]
                p_ts =  f.BB(freq*1.e9,T_baf)*spill_ts*fil_eff*len_eff*det_eff_LFT[i][j]
                p_hm =  f.BB(freq*1.e9,T_hwp_LFT)*spill_hm*fil_eff*len_eff*det_eff_LFT[i][j]
                
                 
                p_fil = f.BB(freq*1.e9,T_fil)*fil_emiss*len_eff*det_eff_LFT[i][j]
                p_fil_ref = f.BB(freq*1.e9,Tr_fil)*ref_fil*len_eff*det_eff_LFT[i][j]
                p_fil = p_fil + p_fil_ref
                
                p_len = f.BB(freq*1.e9,T_len)*len_emiss*det_eff_LFT[i][j]
                p_len_ref = f.BB(freq*1.e9,Tr_len)*ref_len*det_eff_LFT[i][j]
                p_len = p_len + p_len_ref
                
                p_det = f.BB(freq*1.e9,Tr_det)*(1-det_eff_LFT[i][j])
         
                p_opt = p_cmb + p_hwp +  p_pm + p_sm + p_fp + p_as + p_ts + p_hm + p_fil + p_det 

                eff = hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*det_eff_LFT[i][j]*pol_hwp_LFT[i][j]*df_LFT[i][j]
                
                p_opt_arr[k] = p_opt
                p_cmb_arr[k] = p_cmb
                p_hwp_arr[k] = p_hwp
                #p_apt_arr[k] = p_apt
                p_lens_arr[k] = p_pm + p_sm
                p_fil_arr[k] = p_fil
                p_len_arr[k] = p_len
                p_fp_arr[k] = p_fp
                p_as_arr[k] = p_fp
                p_ts_arr[k] = p_ts
                p_hm_arr[k] = p_hm

                nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
                nep_opt_arr[k] = nep_opt
                dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
                dpdt_arr[k] = dpdt

                #if(freq == freqLFT[i][j]):
                   # print round(freqLFT[i][j],2)," , ",round(spill_apt,3)," , ",round(spill_ts,3)," , ",round(spill_fb,3)," , ",round(spill_hm,3)," , ",round(apt_eff,3)
                   # print round(freqLFT[i][j],2)," , ",round(hwp_eff,3)," , ",round(spill_apt,3)," , ",round(spill_ts,3)," , ",round(spill_fb,3)," , ",round(spill_hm,3)," , ",round(apt_eff,3)," ,",round(pm_eff,8)," , ",round(sm_eff,8)," , ",round(fil_eff,8)," , ",round(len_eff,8)," , ",round(det_eff_LFT[i][j],3)," , ",round(pol_hwp_LFT[i][j],3)," , ",round(df_LFT[i][j],3)

            Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            #Pcmb = np.sum(p_cmb_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            #Phwp = np.sum(p_hwp_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            #Papt = np.sum(p_apt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            #Plens = np.sum(p_lens_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            #Pfil = np.sum(p_fil_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            #Plen = np.sum(p_len_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            #Phm = np.sum(p_hm_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW

            Psat = Pfac*Popt    
           
            NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
            NEPth = np.sqrt(4.*k_b*Psat*1.e-12*T_bath*(3.+1.)**2./(2.*3.+3.)*(1.71**(2.*3.+3.)-1.)/((1.71**(3.+1.)-1.)**2.))*1.e18
            #NEPread = np.sqrt(0.21*(NEPopt**2.+NEPth**2.))
            NEPread = np.sqrt(Popt/0.5)*3.5
            NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPread**2.)
            NEPext = np.sqrt(0.32)*np.sqrt(NEPint**2.)
            NEPdet = np.sqrt(NEPint**2. + NEPext**2.)
            
            DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
            NETdet = NEPdet*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
            NETarrLFT[i][j] = NETdet/np.sqrt(2.*npixLFT[i][j]*0.8)  

            print round(freqLFT[i][j],2)," , ",round(Popt,8)," , ",round(NEPopt,8)," , ",round(NEPth,8)," , ",round(NEPread,8)," , ",round(NEPint,8)," , ",round(NEPext,8)," , ",round(NEPdet,8)," , ",round(NETdet,8)," , ",round(NETarrLFT[i][j],8)


    ####################### MHFT noise calculation ############################

    NETarrHFT=([[0.,0.,0.,0.,0],[0.,0.,0.,0.,0.]])

    for i in range(0,m2):
        for j in range(0,n2):

            freq_l, freq_h = f.FreqRange(freqHFT[i][j],bandHFT[i][j])
            
            for k in range(0,num):
                freq = freq_l+(freq_h - freq_l)*k/(num-1)
                hwp_eff = 1.- hwp_emiss_HFT[i][j] - ref_hwp_HFT[i][j]
            
                apt_emiss, apt_eff = f.Aperture(dpixHFT[i][j]*1.e-3, bf_HFT[i][j], Fnum_HFT[i][j], freq*1.e9)
                
                pm_emiss = emiss_L1[i][j]
                sm_emiss = emiss_L2[i][j]
                pm_eff = 1. - pm_emiss - ref_L1[i][j]
                sm_eff = 1. - sm_emiss - ref_L2[i][j]
                 
                  
                fil_emiss, fil_eff = f.Trm(t_fil, n_fil, tan_fil, freq*1.e9, ref_fil)
                
                if (i==0): # lens coupled detetor
                    len_emiss, len_eff = 0., 1.
                    ref_len = 0.

                else: # horn coupled detector
                    len_emiss = 0.
                    len_eff = 1.-ref_horn
                    ref_len = ref_horn
                  
                p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                
                p_hwp = f.BB(freq*1.e9,T_hwp_HFT)*hwp_emiss_HFT[i][j]*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                p_hwp_ref = f.BB(freq*1.e9,Tr_hwp)*ref_hwp_HFT[i][j]*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                p_hwp = p_hwp + p_hwp_ref
                
                p_apt = f.BB(freq*1.e9,T_apt_HFT)*apt_emiss*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                
                p_pm = f.BB(freq*1.e9,T_mir)*pm_emiss*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                p_pm_ref = f.BB(freq*1.e9,Tr_mir)*ref_L1[i][j]*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                p_pm = p_pm + p_pm_ref
                
                p_sm = f.BB(freq*1.e9,T_mir)*sm_emiss*fil_eff*len_eff*det_eff_HFT[i][j]
                p_sm_ref = f.BB(freq*1.e9,Tr_mir)*ref_L2[i][j]*fil_eff*len_eff*det_eff_HFT[i][j]
                p_sm = p_sm + p_sm_ref
                
                p_fil = f.BB(freq*1.e9,T_fil)*fil_emiss*len_eff*det_eff_HFT[i][j]
                p_fil_ref = f.BB(freq*1.e9,Tr_fil)*ref_fil*len_eff*det_eff_HFT[i][j]
                p_fil = p_fil + p_fil_ref
                
                p_len = f.BB(freq*1.e9,T_len)*len_emiss*det_eff_HFT[i][j]
                p_len_ref = f.BB(freq*1.e9,Tr_len)*ref_len*det_eff_HFT[i][j]
                p_len = p_len + p_len_ref
                
                p_det = f.BB(freq*1.e9,Tr_det)*(1-det_eff_HFT[i][j])
         
                p_opt = p_cmb + p_hwp + p_apt + p_pm + p_sm + p_fil + p_len + p_det 

                eff = hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]*pol_hwp_HFT[i][j]*df_HFT[i][j]
                     
                p_opt_arr[k] = p_opt
                p_cmb_arr[k] = p_cmb
                p_hwp_arr[k] = p_hwp
                p_apt_arr[k] = p_apt
                p_lens_arr[k] = p_pm + p_sm
                p_fil_arr[k] = p_fil
                p_len_arr[k] = p_len

                nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
                nep_opt_arr[k] = nep_opt
                dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
                dpdt_arr[k] = dpdt
                     
            Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            Pcmb = np.sum(p_cmb_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            Phwp = np.sum(p_hwp_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            Papt = np.sum(p_apt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            Plens = np.sum(p_lens_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            Pfil = np.sum(p_fil_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            Plen = np.sum(p_len_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
            
            Psat = Pfac*Popt
            
            NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
            NEPth = np.sqrt(4.*k_b*Psat*1.e-12*T_bath*(3.+1.)**2./(2.*3.+3.)*(1.71**(2.*3.+3.)-1.)/((1.71**(3.+1.)-1.)**2.))*1.e18
            #NEPread = np.sqrt(0.21*(NEPopt**2.+NEPth**2.))
            NEPread = np.sqrt(Popt/0.5)*3.5
            NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPread**2.)
            NEPext = np.sqrt(0.32)*np.sqrt(NEPint**2.)
            NEPdet = np.sqrt(NEPint**2. + NEPext**2.)
            DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
            NETdet = NEPdet*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
            NETarrHFT[i][j] = NETdet/np.sqrt(2.*npixHFT[i][j]*0.8)  


            print round(freqHFT[i][j],2)," , ",round(Popt,8)," , ",round(NEPopt,8)," , ",round(NEPth,8)," , ",round(NEPread,8)," , ",round(NEPint,8)," , ",round(NEPext,8)," , ",round(NEPdet,8)," , ",round(NETdet,8)," , ",round(NETarrHFT[i][j],8)
       

    NETarr = np.zeros(15)        
    NETarr[0]= NETarrLFT[0][0]; #40 GHz
    NETarr[1]= NETarrLFT[1][0]; #50 GHz
    NETarr[2]= NETarrLFT[0][1]; #60 GHz
      
    NETarr[3]= np.sqrt(1./(1./pow(NETarrLFT[1][1],2.) + 1./pow(NETarrLFT[2][0],2.)));#68 GHz
    NETarr[4]= np.sqrt(1./(1./pow(NETarrLFT[0][2],2.) + 1./pow(NETarrLFT[3][0],2.)));#78 GHz
    NETarr[5]= np.sqrt(1./(1./pow(NETarrLFT[1][2],2.) + 1./pow(NETarrLFT[2][1],2.)));#89 GHz
    NETarr[6]= np.sqrt(1./(1./pow(NETarrLFT[3][1],2.) + 1./pow(NETarrHFT[0][0],2.)));#100 GHz
    NETarr[7]= np.sqrt(1./(1./pow(NETarrLFT[2][2],2.) + 1./pow(NETarrHFT[0][1],2.)));#119 GHz
    NETarr[8]= np.sqrt(1./(1./pow(NETarrLFT[3][2],2.) + 1./pow(NETarrHFT[0][2],2.)));#140 GHz

    NETarr[9]= NETarrHFT[0][3];#166 GHz
    NETarr[10]= np.sqrt(1./(1./pow(NETarrHFT[0][4],2.) + 1./pow(NETarrHFT[1][0],2.)));#195 GHz
    NETarr[11]= NETarrHFT[1][1];#235 GHz
    NETarr[12]= NETarrHFT[1][2];#280 GHz
    NETarr[13]= NETarrHFT[1][3];#335 GHz
    NETarr[14]= NETarrHFT[1][4];#402 GHz

    Sensitivity =  f.Sigma( NETarr, t);
    Sum_sens = 0

    print "Freq [GHz] , NETarr [microK/rtHz] , Sensitivity [microK -arcmin]"

    for i in range (0,15):
        Sum_sens = Sum_sens + 1./(Sensitivity[i]**2.) 
        print Freq[i]," , ",round(NETarr[i],2)," , ",round(Sensitivity[i],2)
    Ave_sens = np.sqrt(1./Sum_sens)   

    print "Averaged_sensitivity = ",round(Ave_sens,2)

    print "T_HWP= [",T_hwp_LFT,T_hwp_HFT,"] K,", "T_stop= [",T_apt_LFT,T_apt_HFT,"] K, Duty cycle= ",DC," T_bath= ",T_bath

    return Freq, NETarr, Sensitivity

