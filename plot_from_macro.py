#install ffmpeg package to save animations:
#conda install -c conda-forge ffmpeg-python

#tutorial on animations:
# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize=(5,5),dpi=300) #required to save as .eps
plt.ylim([0,60])

working_directory = "/Users/nunoluis/Desktop/"
fname_C1 = working_directory + "plot_data_C1_normalized.csv"
fname_C2 = working_directory + "plot_data_C2_normalized.csv"

data_actin = np.loadtxt(fname_C1, delimiter=",", skiprows=1)
data_mito = np.loadtxt(fname_C2, delimiter=",", skiprows=1)

x = data_actin[:,1]

def init():
    y = x * 0
    return plt.plot(x, y)
    

def animate(i):
    fig.clear()
    #plt.ylim([0,200])
    y_actin = data_actin[:, i+2]
    y_mito = data_mito[:, i+2]
    plt.plot(x, y_mito, color = "green")
    plt.plot(x, y_actin, color = "red")
    #plt.scatter(x, y) # you can comment in if points are needed
    legend = (i + 1) * 15
    plt.xlabel("Distance in microns")
    plt.ylabel("gray intensity")
    plt.title('actin distribution on short axis')
    plt.plot()
    return plt.plot()

#plt.plot(x, y, label = str(legend) + "0_min")

#plt.legend()

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=25, interval=100, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=3, extra_args=['-vcodec', 'libx264'])

#plt.savefig(working_directory + "_plot.eps", format = "eps") #if you want to save the plot to the save location of data uncomment line

plt.show() # always needs to be at the end, after plt.savefig() otherwise fig is not saved correctly
