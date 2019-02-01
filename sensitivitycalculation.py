import numpy as np
import function as f
import fp as fp
import opt as op
import matplotlib.pyplot as plt

pi = f.pi
k_b = f.k_b
c= f.c
h= f.h

########################## Telescope Configrations #############################
confLFT = 0
confHFT = 2


########################### Duty cycle ##########################
DC = 1.0


#######################################################################
t=3.*365.*24.*60.*60.*0.95*0.95*DC;# 3 years ovservation time including cosmic ray loss (0.95), margin (0.95) and sub-K cooler duty cycle
Freq = np.array([40., 50., 60., 68., 78., 89., 100., 119., 140., 166., 195., 235., 280, 337., 402.]);
m=4
n=3
num=10000
############################# Optics Temperatures ################################
T_bath,T_cmb, T_hwp_LFT,T_hwp_HFT, T_apt, T_mir, T_fil, T_len, T_lens, T_baf, Tr_hwp,Tr_mir,Tr_fil,Tr_len,Tr_lens = op.Temp_Opt()
# = op.Temp_Ref_Opt()

T_len = T_bath
T_horn = T_bath
Tr_len = T_baf
Tr_horn = T_baf
################################ FP parameters ##########################################
freqLFT, bandLFT, dpixLFT, npixLFT, NEPreadLFT = fp.LFT_FP(confLFT)
freqHFT, bandHFT, dpixHFT, npixHFT, NEPreadHFT = fp.HFT_FP(confHFT)

################################# Optics parameters ##########################################
#LFT
hwp_emiss_LFT, ref_hwp_LFT, hwp_holder_LFT = op.LFT_Hwp(confLFT)
bf_LFT, Fnum_LFT = op.LFT_Apt(confLFT) 
det_eff_LFT = op.LFT_Det(confLFT) 

#HFT
hwp_emiss_HFT, ref_hwp_HFT = op.HFT_Hwp(confHFT)
bf_HFT, Fnum_HFT = op.HFT_Apt(confHFT) 
det_eff_HFT = op.HFT_Det(confHFT) 
ref_horn = 0.05

#Sapphire HWP for HFT
t_hwp, n_hwp, tan_hwp, ref_hwp_sap = op.Sap_HWP()
                       
#Mirror 
epsilon, rho, rms = op.Mir()

#Field and Objective Lenses
t_lens1,t_lens2, t_lens3, t_lens4,n_lens, tan_lens, ref_lens = op.HDPE_Lens()

#2K filter
t_fil, n_fil, tan_fil, ref_fil =op.Fil()

# detector lenslet
t_len, n_len, tan_len, ref_len =op.Len()
####################### LFT noise calculation ############################
p_opt_arr = np.zeros(num)
nep_opt_arr = np.zeros(num)
dpdt_arr = np.zeros(num)
NETarrLFT=([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
NETarrLFTmargin=([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])

print "Freq [GHz] , Popt [pW] , NEPph [aW/rtHz] , NEPg [aW/rtHz] , NEPread [aW/rtHz] , NEPdet [aW/rtHz] , NETdet [microK/rtHz] , NETarr [microK/rtHz] , NETarrmargin [microK/rtHz]"
#print "Freq [GHz] , p_cmb , p_hwp, p_apt, p_pm, p_sm, p_fil, p_len, p_opt, p_20K"

for i in range(0,m):
    for j in range(0,n):
        freq_l, freq_h = f.FreqRange(freqLFT[i][j],bandLFT[i][j])
        hwp_eff = f.Hwp(hwp_emiss_LFT[i][j], ref_hwp_LFT[i][j])
        
        for k in range(0,num):
            freq = freq_l+(freq_h - freq_l)*k/num
            hwp_emiss_ref = hwp_emiss_LFT[i][j] + ref_hwp_LFT[i][j]*f.BB(freq*1.e9, Tr_hwp)/f.BB(freq*1.e9, T_hwp_LFT)
            apt_emiss, apt_eff = f.Aperture(dpixLFT[i][j]*1.e-3, bf_LFT, Fnum_LFT, freq*1.e9)
            spill20K = hwp_holder_LFT[i][j]
            spill5K, eff5K = f.Aperture(dpixLFT[i][j]*1.e-3, bf_LFT, 1.64, freq*1.e9)
            spill2K = 1.- apt_eff - spill5K 
            pm_emiss, pm_eff, pm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
            pm_emiss_ref = pm_emiss + pm_loss*f.BB(freq*1.e9, Tr_mir)/f.BB(freq*1.e9, T_mir)
            sm_emiss, sm_eff, sm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
            sm_emiss_ref = sm_emiss + sm_loss*f.BB(freq*1.e9, Tr_mir)/f.BB(freq*1.e9, T_mir)
            fil_emiss, fil_eff = f.Trm(t_fil, n_fil, tan_fil, freq*1.e9, ref_fil)
            fil_emiss_ref = fil_emiss + ref_fil*f.BB(freq*1.e9, Tr_fil)/f.BB(freq*1.e9, T_fil)
            len_emiss, len_eff = f.Trm(t_len, n_len, tan_len, freq*1.e9, ref_len)
            len_emiss_ref = len_emiss + ref_len*f.BB(freq*1.e9, Tr_len)/f.BB(freq*1.e9, T_len)

            ###### reflection effect ##### 
            hwp_emiss = hwp_emiss_ref
            len_emiss = len_emiss_ref
            fil_emiss = fil_emiss_ref
            pm_emiss = pm_emiss_ref
            sm_emiss = sm_emiss_ref
            
            ##############################
            p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT
            p_hwp = f.BB(freq*1.e9,T_hwp_LFT)*hwp_emiss*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT
            p_apt = (f.BB(freq*1.e9,T_apt)*spill2K + f.BB(freq*1.e9,T_baf)*spill5K)*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT
            p_20K = f.BB(freq*1.e9,20)*spill20K*fil_eff*len_eff*det_eff_LFT
            p_pm = f.BB(freq*1.e9,T_mir)*pm_emiss*sm_eff*fil_eff*len_eff*det_eff_LFT
            p_sm = f.BB(freq*1.e9,T_mir)*sm_emiss*fil_eff*len_eff*det_eff_LFT
            p_fil = f.BB(freq*1.e9,T_fil)*fil_emiss*len_eff*det_eff_LFT
            p_len = f.BB(freq*1.e9,T_len)*len_emiss*det_eff_LFT
            p_opt = p_cmb + p_hwp + p_apt + p_pm + p_sm + p_fil + p_len + p_20K

           # if freq==freqLFT[i][j]:
           #     print round(freq,2),", ",round(p_cmb*1.e24, 3),", ",round(p_hwp*1.e24, 3),", ",round(p_apt*1.e24, 3),", ",round(p_pm*1.e24, 3),", ",round(p_sm*1.e24, 3),", ",round(p_fil*1.e24, 3),", ",round(p_len*1.e24, 3),", ",round(p_opt*1.e24, 3),", ",round(p_20K*1.e24, 3)
          
            p_opt_arr[k] = p_opt
            nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
            nep_opt_arr[k] = nep_opt
            eff = hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_LFT
            dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
            dpdt_arr[k] = dpdt
                
        Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
        NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
        NEPth = np.sqrt(4.*k_b*2.5*Popt*1.e-12*T_bath*(3.+1.)**2./(2.*3.+3.)*(1.71**(2.*3.+3.)-1.)/((1.71**(3.+1.)-1.)**2.))*1.e18
        NEPread = np.sqrt(0.21*(NEPopt**2.+NEPth**2.))
        NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPread**2.)
        DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
        NETdet = NEPint*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
        NETarrLFT[i][j] = NETdet/np.sqrt(2.*npixLFT[i][j])  
        NETarrLFTmargin[i][j] = NETdet*1.15/np.sqrt(2.*npixLFT[i][j]*0.8)  

        print round(freqLFT[i][j],2)," , ",round(Popt,2)," , ",round(NEPopt,2)," , ",round(NEPth,2)," , ",round(NEPread,2)," , ",round(NEPint,2)," , ",round(NETdet,2)," , ",round(NETarrLFT[i][j],2)," , ",round(NETarrLFTmargin[i][j],2)

##########################################################################

####################### HFT noise calculation ############################

NETarrHFT=([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
NETarrHFTmargin=([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])

for i in range(0,n):
    for j in range(0,n):

        freq_l, freq_h = f.FreqRange(freqHFT[i][j],bandHFT[i][j])
        hwp_eff = f.Hwp(hwp_emiss_HFT[i][j], ref_hwp_HFT[i][j])
        
        for k in range(0,num):
            freq = freq_l+(freq_h - freq_l)*k/num
            hwp_emiss_ref = hwp_emiss_HFT[i][j] + ref_hwp_HFT[i][j]*f.BB(freq*1.e9, Tr_hwp)/f.BB(freq*1.e9, T_hwp_HFT)
            apt_emiss, apt_eff = f.Aperture(dpixHFT[i][j]*1.e-3, bf_HFT[i][j], Fnum_HFT, freq*1.e9)
            
            if (confHFT == 0): # Reflective Option 
                pm_emiss, pm_eff, pm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
                pm_emiss_ref = pm_emiss + pm_loss*f.BB(freq*1.e9, Tr_mir)/f.BB(freq*1.e9, T_mir)
                sm_emiss, sm_eff, sm_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
                sm_emiss_ref = sm_emiss + sm_loss*f.BB(freq*1.e9, Tr_mir)/f.BB(freq*1.e9, T_mir)
                
            if (confHFT == 2): # Split Refractive Option 
                
                if(i==0 or i==1):# MFT lens
                     pm_emiss, pm_eff = f.Trm(t_lens1, n_lens, tan_lens, freq*1.e9, ref_lens)
                     pm_emiss_ref = pm_emiss + ref_lens*f.BB(freq*1.e9, Tr_lens)/f.BB(freq*1.e9, T_lens)
                     sm_emiss, sm_eff = f.Trm(t_lens2, n_lens, tan_lens, freq*1.e9, ref_lens)
                     sm_emiss_ref = sm_emiss + ref_lens*f.BB(freq*1.e9, Tr_lens)/f.BB(freq*1.e9, T_lens)
                if(i==2) :# HFT lens
                     pm_emiss, pm_eff = f.Trm(t_lens3, n_lens, tan_lens, freq*1.e9, ref_lens)
                     pm_emiss_ref = pm_emiss + ref_lens*f.BB(freq*1.e9, Tr_lens)/f.BB(freq*1.e9, T_lens)
                     sm_emiss, sm_eff = f.Trm(t_lens4, n_lens, tan_lens, freq*1.e9, ref_lens)
                     sm_emiss_ref = sm_emiss + ref_lens*f.BB(freq*1.e9, Tr_lens)/f.BB(freq*1.e9, T_lens)
                    
               
            fil_emiss, fil_eff = f.Trm(t_fil, n_fil, tan_fil, freq*1.e9, ref_fil)
            fil_emiss_ref = fil_emiss + ref_fil*f.BB(freq*1.e9, Tr_fil)/f.BB(freq*1.e9, T_fil)
            
            if (i==0 or i==1): # lens coupled detetor
                len_emiss, len_eff = f.Trm(t_len, n_len, tan_len, freq*1.e9, ref_len)
                len_emiss_ref = len_emiss + ref_len*f.BB(freq*1.e9, Tr_len)/f.BB(freq*1.e9, T_len)

            else: # horn coupled detector
                len_emiss = 0.
                len_eff = 1.-ref_horn
                len_emiss_ref = len_emiss + ref_horn*f.BB(freq*1.e9, Tr_horn)/f.BB(freq*1.e9,T_len)

           # print "Freq=",round(freq,2)," , HDPEemiss=",round(mir_emiss,2)

            ###### reflection effect ##### 
            hwp_emiss = hwp_emiss_ref
            len_emiss = len_emiss_ref
            fil_emiss = fil_emiss_ref
            pm_emiss = pm_emiss_ref
            sm_emiss = sm_emiss_ref
            ##############################
            p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
            p_hwp = f.BB(freq*1.e9,T_hwp_HFT)*hwp_emiss_HFT[i][j]*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
            p_apt = f.BB(freq*1.e9,T_apt)*apt_emiss*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
            p_pm = f.BB(freq*1.e9,T_mir)*pm_emiss*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
            p_sm = f.BB(freq*1.e9,T_mir)*sm_emiss*fil_eff*len_eff*det_eff_HFT[i][j]
            p_fil = f.BB(freq*1.e9,T_fil)*fil_emiss*len_eff*det_eff_HFT[i][j]
            p_len = f.BB(freq*1.e9,T_len)*len_emiss*det_eff_HFT[i][j]
            p_opt = p_cmb + p_hwp + p_apt + p_pm + p_sm + p_fil + p_len
            eff = hwp_eff*apt_eff*pm_eff*sm_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                   
            p_opt_arr[k] = p_opt
            nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
            nep_opt_arr[k] = nep_opt
            dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
            dpdt_arr[k] = dpdt

           # if freq==freqHFT[i][j]:
            #    print round(freq,2),", ",round(p_cmb*1.e24, 3),", ",round(p_hwp*1.e24, 3),", ",round(p_apt*1.e24, 3),", ",round(p_pm*1.e24, 3),", ",round(p_sm*1.e24, 3),", ",round(p_fil*1.e24, 3),", ",round(p_len*1.e24, 3),", ",round(p_opt*1.e24, 3)
                 
        Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
        NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
        NEPth = np.sqrt(4.*k_b*2.5*Popt*1.e-12*T_bath*(3.+1.)**2./(2.*3.+3.)*(1.71**(2.*3.+3.)-1.)/((1.71**(3.+1.)-1.)**2.))*1.e18
        NEPread = np.sqrt(0.21*(NEPopt**2.+NEPth**2.))
        NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPread**2.)
        DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
        NETdet = NEPint*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
        NETarrHFT[i][j] = NETdet/np.sqrt(2.*npixHFT[i][j])  
        NETarrHFTmargin[i][j] = NETdet*1.15/np.sqrt(2.*npixHFT[i][j]*0.8)  


        print round(freqHFT[i][j],2)," , ",round(Popt,2)," , ",round(NEPopt,2)," , ",round(NEPth,2)," , ",round(NEPread,2)," , ",round(NEPint,2)," , ",round(NETdet,2)," , ",round(NETarrHFT[i][j],2)," , ",round(NETarrHFTmargin[i][j],2)

NETarr = np.zeros(15)        
NETarr[0]= NETarrLFTmargin[0][0];
NETarr[1]= NETarrLFTmargin[1][0];
NETarr[2]= NETarrLFTmargin[0][1];
  
NETarr[3]= np.sqrt(1./(1./pow(NETarrLFTmargin[1][1],2.) + 1./pow(NETarrLFTmargin[2][0],2.)));
NETarr[4]= np.sqrt(1./(1./pow(NETarrLFTmargin[0][2],2.) + 1./pow(NETarrLFTmargin[3][0],2.)));
NETarr[5]= np.sqrt(1./(1./pow(NETarrLFTmargin[1][2],2.) + 1./pow(NETarrLFTmargin[2][1],2.)));
NETarr[6]= np.sqrt(1./(1./pow(NETarrLFTmargin[3][1],2.) + 1./pow(NETarrHFTmargin[0][0],2.)));
NETarr[7]= np.sqrt(1./(1./pow(NETarrLFTmargin[2][2],2.) + 1./pow(NETarrHFTmargin[1][0],2.)));
NETarr[8]= np.sqrt(1./(1./pow(NETarrLFTmargin[3][2],2.) + 1./pow(NETarrHFTmargin[0][1],2.)));

NETarr[9]= NETarrHFTmargin[1][1];
NETarr[10]= NETarrHFTmargin[0][2];
NETarr[11]= NETarrHFTmargin[1][2];
NETarr[12]= NETarrHFTmargin[2][0];
NETarr[13]= NETarrHFTmargin[2][1];
NETarr[14]= NETarrHFTmargin[2][2];

Sensitivity =  f.Sigma( NETarr, t);
Sum_sens = 0

print "T_HWP= [",T_hwp_LFT,T_hwp_HFT,"] K,", "T_stop= ",T_apt,"K, Duty cycle= ",DC," T_bath= ",T_bath

print "Freq [GHz] , NETarr [microK/rtHz] , Sensitivity [microK -arcmin]"
for i in range (0,15):
    Sum_sens = Sum_sens + 1./(Sensitivity[i]**2.) 
    print Freq[i]," , ",round(NETarr[i],2)," , ",round(Sensitivity[i],2)   
Ave_sens = np.sqrt(1./Sum_sens)   
print "Averaged_sensitivity = ",round(Ave_sens,2)


############################# Plot ####################################
fig = plt.figure(figsize=(10, 6))
plt.grid(which='major',color='black',linestyle='-')
plt.grid(which='minor',color='black',linestyle='-')
plt.xscale("log")
plt.xlabel('Frequency [GHz]',fontsize=18)
plt.ylabel('Sensitivity [$\mu$K-arcmin]',fontsize=18)
plt.tick_params(labelsize=18)
ax = fig.add_subplot(111)
ax.plot(Freq, Sensitivity, "o-", color="k", label="")
ax.set_xlim(30., 450.)
ax.set_ylim(0., 40.)
#ax.legend(loc="upper left")
plt.show()
    
