import numpy as np
import function as f
import fp as fp
import opt as op
import matplotlib.pyplot as plt

########################## Telescope Configrations #############################
confLFT = 0
confHFT = 0
################################################################################
t=3.*365.*24.*60.*60.*0.72;# 3 years ovservation time including cosmic ray loss (0.85) and ADR duty cycle (0.85)
Freq = np.array([40., 50., 60., 68., 78., 89., 100., 119., 140., 166., 195., 235., 280, 337., 402.]);
m=4
n=3
num=100000
############################# Optics Temperatures ################################
T_cmb, T_hwp, T_apt, T_mir, T_fil, T_len, T_lens, T_baf = op.Temp_Opt()
Tr_hwp,Tr_mir,Tr_fil,Tr_len,Tr_lens = op.Temp_Ref_Opt()

################################ FP parameters ##########################################
freqLFT, bandLFT, dpixLFT, npixLFT, NEPreadLFT = fp.LFT_FP(confLFT)
freqHFT, bandHFT, dpixHFT, npixHFT, NEPreadHFT = fp.HFT_FP(confHFT)

################################# Optics parameters ##########################################
#LFT
hwp_emiss_LFT, ref_hwp_LFT = op.LFT_Hwp(confLFT)
bf_LFT, Fnum_LFT = op.LFT_Apt(confLFT) 
det_eff_LFT = op.LFT_Det(confLFT) 

#HFT
hwp_emiss_HFT, ref_hwp_HFT = op.HFT_Hwp(confHFT)
bf_HFT, Fnum_HFT = op.HFT_Apt(confHFT) 
det_eff_HFT = op.HFT_Det(confHFT) 

#Sapphire HWP for HFT
t_hwp, n_hwp, tan_hwp, ref_hwp_sap = op.Sap_HWP()
                       
#Mirror 
epsilon, rho, rms = op.Mir()

#Field and Objective Lenses
t_lens, n_lens, tan_lens, ref_lens = op.Lens()

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

for i in range(0,m):
    for j in range(0,n):
        freq_l, freq_h = f.FreqRange(freqLFT[i][j],bandLFT[i][j])
        hwp_eff = f.Hwp(hwp_emiss_LFT[i][j], ref_hwp_LFT[i][j])
        
        for k in range(0,num):
            freq = freq_l+(freq_h - freq_l)*k/num
            hwp_emiss_ref = hwp_emiss_LFT[i][j] + ref_hwp_LFT[i][j]*f.BB(freq*1.e9, Tr_hwp)/f.BB(freq*1.e9, T_hwp)
            apt_emiss, apt_eff = f.Aperture(dpixLFT[i][j]*1.e-3, bf_LFT, Fnum_LFT, freq*1.e9)
            spill5K, eff5K = f.Aperture(dpixLFT[i][j]*1.e-3, bf_LFT, 1.918, freq*1.e9)
            spill2K = eff5K - apt_eff
            mir_emiss, mir_eff, mir_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
            mir_emiss_ref = mir_emiss + mir_loss*f.BB(freq*1.e9, Tr_mir)/f.BB(freq*1.e9, T_mir)
            fil_emiss, fil_eff = f.Trm(t_fil, n_fil, tan_fil, freq*1.e9, ref_fil)
            fil_emiss_ref = fil_emiss + ref_fil*f.BB(freq*1.e9, Tr_fil)/f.BB(freq*1.e9, T_fil)
            len_emiss, len_eff = f.Trm(t_len, n_len, tan_len, freq*1.e9, ref_len)
            len_emiss_ref = len_emiss + ref_len*f.BB(freq*1.e9, Tr_len)/f.BB(freq*1.e9, T_len)

            ###### reflection effect ##### 
            hwp_emiss = hwp_emiss_ref
            len_emiss = len_emiss_ref
            fil_emiss = fil_emiss_ref
            mir_emiss = mir_emiss_ref
            ##############################
            p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*mir_eff*mir_eff*fil_eff*len_eff*det_eff_LFT
            p_hwp = f.BB(freq*1.e9,T_hwp)*hwp_emiss*apt_eff*mir_eff*mir_eff*fil_eff*len_eff*det_eff_LFT
            p_apt = (f.BB(freq*1.e9,T_apt)*spill2K + f.BB(freq*1.e9,T_baf)*spill5K)*mir_eff*mir_eff*fil_eff*len_eff*det_eff_LFT
            p_mir = f.BB(freq*1.e9,T_mir)*mir_emiss*(mir_eff*fil_eff*len_eff*det_eff_LFT + fil_eff*len_eff*det_eff_LFT)
            p_fil = f.BB(freq*1.e9,T_fil)*fil_emiss*len_eff*det_eff_LFT
            p_len = f.BB(freq*1.e9,T_len)*len_emiss*det_eff_LFT
            p_opt = p_cmb + p_hwp + p_apt + p_mir + p_fil + p_len
          
            p_opt_arr[k] = p_opt
            nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
            nep_opt_arr[k] = nep_opt
            eff = hwp_eff*apt_eff*mir_eff*mir_eff*fil_eff*len_eff*det_eff_LFT
            dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
            dpdt_arr[k] = dpdt
                
        Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
        NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
        NEPth = 7.31e-12*np.sqrt(Popt*1.e-12)*1.e18;
        NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPreadLFT[i][j]**2.)
        DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
        NETdet = NEPint*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
        NETarrLFT[i][j] = NETdet/np.sqrt(2.*npixLFT[i][j])  
        NETarrLFTmargin[i][j] = NETdet*1.15/np.sqrt(2.*npixLFT[i][j]*0.8)  

       # print("freq=",freqLFT[i][j],"Popt=",Popt,"NEPopt=",NEPopt,"NEPth=",NEPth,"NEPreadLFT=",NEPreadLFT[i][j],"NEPint=",NEPint,"NETdet=",NETdet,"NETarr=",NETarrLFT[i][j],"NETarrmargin=",NETarrLFTmargin[i][j])

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
            hwp_emiss_ref = hwp_emiss_HFT[i][j] + ref_hwp_HFT[i][j]*f.BB(freq*1.e9, Tr_hwp)/f.BB(freq*1.e9, T_hwp)
            apt_emiss, apt_eff = f.Aperture(dpixHFT[i][j]*1.e-3, bf_HFT[i][j], Fnum_HFT, freq*1.e9)
            
            if (confHFT == 0): # Reflective Option 
                mir_emiss, mir_eff, mir_loss = f.Mirror(freq*1.e9, rho, epsilon, rms)
                mir_emiss_ref = mir_emiss + mir_loss*f.BB(freq*1.e9, Tr_mir)/f.BB(freq*1.e9, T_mir)
                
            if (confHFT == 1): # Split Refractive Option 
                mir_emiss, mir_eff = f.Trm(t_lens, n_lens, tan_lens, freq*1.e9, ref_lens)
                mir_emiss_ref = mir_emiss + ref_lens*f.BB(freq*1.e9, Tr_lens)/f.BB(freq*1.e9, T_lens)
                
            fil_emiss, fil_eff = f.Trm(t_fil, n_fil, tan_fil, freq*1.e9, ref_fil)
            fil_emiss_ref = fil_emiss + ref_fil*f.BB(freq*1.e9, Tr_fil)/f.BB(freq*1.e9, T_fil)
            
            if (i==0 or i==1): # lens coupled detetor
                len_emiss, len_eff = f.Trm(t_len, n_len, tan_len, freq*1.e9, ref_len)
                len_emiss_ref = len_emiss + ref_len*f.BB(freq*1.e9, Tr_len)/f.BB(freq*1.e9, T_len)

            else: # horn coupled detector
                len_emiss = 0.
                len_eff = 1.
                len_emiss_ref = 0.

            ###### reflection effect ##### 
            hwp_emiss = hwp_emiss_ref
            len_emiss = len_emiss_ref
            fil_emiss = fil_emiss_ref
            mir_emiss = mir_emiss_ref
            ##############################
            p_cmb = f.BB(freq*1.e9,T_cmb)*hwp_eff*apt_eff*mir_eff*mir_eff*fil_eff*len_eff*det_eff_HFT[i][j]
            p_hwp = f.BB(freq*1.e9,T_hwp)*hwp_emiss_HFT[i][j]*apt_eff*mir_eff*mir_eff*fil_eff*len_eff*det_eff_HFT[i][j]
            p_apt = f.BB(freq*1.e9,T_apt)*apt_emiss*mir_eff*mir_eff*fil_eff*len_eff*det_eff_HFT[i][j]
            p_mir = f.BB(freq*1.e9,T_mir)*mir_emiss*(mir_eff*fil_eff*len_eff*det_eff_HFT[i][j] + fil_eff*len_eff*det_eff_HFT[i][j])
            p_fil = f.BB(freq*1.e9,T_fil)*fil_emiss*len_eff*det_eff_HFT[i][j]
            p_len = f.BB(freq*1.e9,T_len)*len_emiss*det_eff_HFT[i][j]
            p_opt = p_cmb + p_hwp + p_apt + p_mir + p_fil + p_len
            eff = hwp_eff*apt_eff*mir_eff*mir_eff*fil_eff*len_eff*det_eff_HFT[i][j]
                   
            p_opt_arr[k] = p_opt
            nep_opt = 2.*p_opt*f.h*freq*1.e9 + 2.*p_opt**2.
            nep_opt_arr[k] = nep_opt
            dpdt = f.dPdT(freq*1.e9, eff, T_cmb)
            dpdt_arr[k] = dpdt
                
        Popt = np.sum(p_opt_arr)*(freq_h-freq_l)*1.e9/num*1.e12 # in unit of pW
        NEPopt =np.sqrt(np.sum(nep_opt_arr)*(freq_h-freq_l)*1.e9/num)*1.e18 # in unit of aW
        NEPth = 7.31e-12*np.sqrt(Popt*1.e-12)*1.e18;
        NEPint = np.sqrt(NEPopt**2. + NEPth**2. + NEPreadHFT[i][j]**2.)
        DPDT = np.sum(dpdt_arr)*(freq_h-freq_l)*1.e9/num
        NETdet = NEPint*1.e-18/np.sqrt(2.)/DPDT*1.e6 # in unit of microK
        NETarrHFT[i][j] = NETdet/np.sqrt(2.*npixHFT[i][j])  
        NETarrHFTmargin[i][j] = NETdet*1.15/np.sqrt(2.*npixHFT[i][j]*0.8)  

       # print("freq=",freqHFT[i][j],"Popt=",Popt,"NEPopt=",NEPopt,"NEPth=",NEPth,"NEPreadHFT=",NEPreadHFT[i][j],"NEPint=",NEPint,"NETdet=",NETdet,"NETarr=",NETarrHFT[i][j],"NETarrmargin=",NETarrHFTmargin[i][j])

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
  
for i in range (0,15):
    print("freq=",Freq[i],"NETarr=",NETarr[i],"Sensitivity=",Sensitivity[i])

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
    
