import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,5),dpi=300) #required to save as .eps

working_directory = "/Users/nunoluis/Downloads/"
fname = working_directory + "plot_data.csv"

data = np.loadtxt(fname, delimiter=",", skiprows=1)

x = data[:,0]
i = np.size(data, 1)

for col in np.arange(i):
    if col > 1:
        y = data[:, col]
        #plt.scatter(x, y) # you can comment in if points are needed
        plt.plot(x, y, label = "col_" + str(col))

plt.xlabel("Time (min)")
plt.ylabel("Photoconverted Dendra intensity (arbitrary units)")
plt.title('Mitochondria movement')
plt.legend()

plt.savefig("_plot.eps", format = "eps") #if you want to save the plot to the save location of data uncomment line

plt.show() # always needs to be at the end, after plt.savefig() otherwise fig is not saved correctly
