import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#experimental data
working_dir = "/Users/nunoluis/Desktop/"
fname = "sarah_test.csv"

data_set = np.loadtxt(working_dir + fname, delimiter=";", skiprows=1)

# experimental data labels
sub_sets = ["cyc7b", "cyc8b", "cyc17", "cyc31"]

#to set same markers and colors for each loop, which is same experiment
markers = ["o", "v", "+", "x"]
markers_count = 0    #to initiate the cycling through the markers list above

#initiate figure for later ploting
fig = plt.figure(figsize=(5,5),dpi=300) #required to save as .eps

#start loop for each experiment, with duplicate point for "y"
#adjust value at end of loop to add to count for different replicate #
count = 0
for sub_set in sub_sets:
    x = data_set[:,0+count]
    y1 = data_set[:, 1+count]
    y2 = data_set[:, 2+count]
    y = np.average(np.vstack((y1, y2)), 0) #second position is for axis to where average, in this case the lines i.e."0"
    # function to fit for, the "objective"
    def objective(x, IC50, HillSlope, bottom, top):
        return bottom + (top-bottom)/(1+((10**(np.log10(IC50)))/(10**x))**HillSlope)
    
    #some tips: https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509
    # graphpad log(inhibitor) vs. response -- Variable slope Equation:
    # https://www.graphpad.com/guides/prism/latest/curve-fitting/reg_dr_inhibit_variable.htm
    
    #curve_fit
    pars, covx = curve_fit(objective, x, y)
    
    #get parameters "pars"
    IC50, HillSlope, bottom, top = pars    #need to be in same order of when def objective, after "x"
    
    # Get the standard deviations of the parameters (square roots of the diagonal of the covariance)
    stdevs = np.sqrt(np.diag(covx))
    IC50stdev, HillSlopestdev, bottomstdev, topstdev = stdevs
    
    print(sub_set)
    print("IC50="+str(round(IC50, 3))+" (+/-"+str(round(IC50stdev, 3))+")")
    print("HillSlope="+str(round(HillSlope, 3))+" (+/-"+str(round(HillSlopestdev, 3))+")")
    print("bottom="+str(round(bottom, 3))+" (+/-"+str(round(bottomstdev, 3))+")")
    print("top="+str(round(top, 3))+" (+/-"+str(round(topstdev, 3))+")")
    
    #generate values to plot same interval with model
    x_final = np.linspace(-2, 2, 30)
    y_final = bottom + (top-bottom)/(1+((10**(np.log10(IC50)))/(10**x_final))**HillSlope)
    
    #plot the model and the experimental points
    line = plt.plot(x_final, y_final, label = "fit") #so I can get_color for next plot I need to assign variable name
    color = line[-1].get_color() #here I use the list with the latest appended color for next plots
    plt.scatter(x, y1, label = sub_set, color=color, marker = markers[markers_count])
    plt.scatter(x, y2, label = sub_set, color=color, marker = markers[markers_count])
    count = count + 3
    markers_count = markers_count + 1

plt.xlabel("log (inhibitor/protein)")
plt.ylabel("% Hsad activity")
plt.title("cyc inhibitors - Xi50")
plt.legend()

plt.show()
