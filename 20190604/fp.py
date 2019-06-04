import numpy as np

##################################### FP parameters ##########################################
def LFT_FP(confLFT):
    if confLFT == 0:
        freqLFT = np.array([[40., 60., 78.],[50., 68., 89.],[68., 89., 119.],[78., 100., 140.]])
        bandLFT = np.array([[0.3, 0.23, 0.23],[0.3, 0.23, 0.23],[0.23, 0.23, 0.3],[0.23, 0.23, 0.3]])
        dpixLFT = np.array([[24., 24., 24.],[24., 24., 24.],[16., 16., 16.],[16., 16., 16.]]) #baseline
        npixLFT = np.array([[32., 32., 32.],[32., 32., 32.],[72., 72., 72.],[72., 72., 72.]])#baseline
        NEPreadLFT =([[3.67, 4.06, 3.98],[4.09, 3.94, 4.03],[4.15, 4.32, 3.63]]);
    return freqLFT, bandLFT, dpixLFT, npixLFT, NEPreadLFT

def HFT_FP(confHFT):
    if confHFT == 0: # F3.5 small FP
        freqHFT = np.array([[100., 140., 195.],[119., 166., 235.],[280., 337., 402.]])
        bandHFT = np.array([[0.23, 0.3, 0.3],[0.3, 0.3, 0.3],[0.3, 0.3, 0.23]])
        dpixHFT = np.array([[12., 12., 12.],[12., 12., 12.],[6., 6., 6.]])
        npixHFT = np.array([[108.,108.,108.],[108.,108.,108.],[161.,161.,161.]]);
        NEPreadHFT =([[3.67, 4.06, 3.98],[4.09, 3.94, 4.03],[4.15, 4.32, 3.63]]);
        
    if confHFT == 1: # F2.2 split optionA
        freqHFT = np.array([[100., 140., 195.],[119., 166., 235.],[280., 337., 402.]])
        bandHFT = np.array([[0.23, 0.3, 0.3],[0.3, 0.3, 0.3],[0.3, 0.3, 0.23]])
        dpixHFT = np.array([[12., 12., 12.],[17., 17., 17.],[5., 5., 5.]])
        npixHFT = np.array([[111.,111.,111.],[76.,76.,76.],[169.,169.,169.]]);
        NEPreadHFT =([0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.]);
        
    if confHFT == 2: # F3.0 split optionA
        freqHFT = np.array([[100., 119., 140., 166., 195.],[195., 235., 280., 337., 402.]])
        bandHFT = np.array([[0.23, 0.3, 0.3,0.3,0.3],[0.3,0.3,0.3, 0.3, 0.23]])
        dpixHFT = np.array([[12., 12., 12.,12., 12.],[6.6, 6.6, 6.6, 6.6, 5.7]]) # MFT small pixel
        npixHFT = np.array([[183.,244.,183.,244.,183.],[127., 127., 127.,127.,169.]]); # MFT small pixel
        NEPreadHFT =([0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.]);
   
    return freqHFT, bandHFT, dpixHFT, npixHFT, NEPreadHFT
