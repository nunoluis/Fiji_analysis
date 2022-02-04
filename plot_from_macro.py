import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,5),dpi=300) #required to save as .eps

working_directory = "/Users/nunoluis/Desktop/_mef2g4mitDx2_25hAPF_27C_int1min_APC1_Multichannel tZ-Stack_20211214_01_/stack1/"
fname = working_directory + "plot_data.csv"
background_file = working_directory + "background_data.csv"

data = np.loadtxt(fname, delimiter=",", skiprows=1)
background = np.loadtxt(background_file, delimiter=",", skiprows=1)

x = data[:,0]
i = np.size(data, 1)

for col in np.arange(i):
    if col > 1:
        noise = background[col-2, 2]
        y = data[:, col]
        corrected_y = y - noise
        #plt.scatter(x, y) # you can comment in if points are needed
        plt.plot(x, corrected_y, label = str(col-2) + "0_min")

plt.xlabel("Time (min)")
plt.ylabel("Photoconverted Dendra intensity (arbitrary units)")
plt.title('Mitochondria movement')
plt.legend()

plt.savefig("_plot.eps", format = "eps") #if you want to save the plot to the save location of data uncomment line

plt.show() # always needs to be at the end, after plt.savefig() otherwise fig is not saved correctly
