import numpy as np

##################################### FP parameters ##########################################
def LFT_FP():
    freqLFT = np.array([[40., 60., 78.],[50., 68., 89.],[68., 89., 119.],[78., 100., 140.]]) # freqency band
    bandLFT = np.array([[0.3, 0.23, 0.23],[0.3, 0.23, 0.23],[0.23, 0.23, 0.3],[0.23, 0.23, 0.3]]) # band width
    #dpixLFT = np.array([[24., 24., 24.],[24., 24., 24.],[16., 16., 16.],[16., 16., 16.]]) # pixel size
    dpixLFT = np.array([[33., 33., 33.],[33., 33., 33.],[16., 16., 16.],[16., 16., 16.]]) # pixel size
    #npixLFT = np.array([[18., 18., 18.],[18., 18., 18.],[72., 72., 72.],[72., 72., 72.]]) # number of pixels
    npixLFT = np.array([[32., 32., 32.],[32., 32., 32.],[72., 72., 72.],[72., 72., 72.]]) # number of pixels
    return freqLFT, bandLFT, dpixLFT, npixLFT

# def HFT_FP():
#     freqHFT = np.array([[100., 119., 140., 166., 195.],[195., 235., 280., 337., 402.]])
#     bandHFT = np.array([[0.23, 0.3, 0.3,0.3,0.3],[0.3,0.3,0.3, 0.3, 0.23]])
#     dpixHFT = np.array([[12., 12., 12.,12., 12.],[6.6, 6.6, 6.6, 6.6, 5.7]]) 
#     npixHFT = np.array([[183.,244.,183.,244.,183.],[127., 127., 127.,127.,169.]]) 
#     return freqHFT, bandHFT, dpixHFT, npixHFT
