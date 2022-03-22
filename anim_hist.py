import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#install the ffmpeg package to save the animation -> conda install -c conda-forge ffmpeg
# animations
# https://towardsdatascience.com/intro-to-dynamic-visualization-with-python-animations-and-interactive-plots-f72a7fb69245

fig = plt.figure(figsize=(5,5),dpi=300) #required to save as .eps
plt.ylim([0,60])

working_directory = "/Users/nunoluis/Desktop/"
fname_C1 = working_directory + "plot_data_C1.csv"
fname_C2 = working_directory + "plot_data_C2.csv"

data_actin = np.loadtxt(fname_C1, delimiter=",", skiprows=1)
data_mito = np.loadtxt(fname_C2, delimiter=",", skiprows=1)

x = data_actin[:,1]

def init():
    y = x * 0
    return plt.plot(x, y)
    

def animate(i):
    fig.clear()
    plt.ylim([0,60])
    y_actin = data_actin[:, i+2]
    y_mito = data_mito[:, i+2]
    #plt.plot(x, y_actin, color = "red")
    #plt.plot(x, y_mito, color = "green")
    #plt.scatter(x, y) # you can comment in if points are needed
    legend = (i + 1) * 15
    plt.xlabel("Distance in microns")
    plt.ylabel("grey intensity")
    plt.title('actin distribution on short axis')
    return plt.plot(x, y_mito, color = "green")

ani = animation.FuncAnimation(fig, animate, init_func = init, blit = True, frames = 25, interval = 200)

#plt.savefig(working_directory + "_plot.eps", format = "eps") #if you want to save the plot to the save location of data uncomment line

writer = animation.FFMpegWriter(fps=3, metadata=dict(artist='Me'), bitrate=1800)

ani.save("movie.mp4", writer=writer)

plt.show() # always needs to be at the end, after plt.savefig() otherwise fig is not saved correctly
