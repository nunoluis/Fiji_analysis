# Fiji_analysis
macros and python scripts to analyse microscopy data

## plot_profile_time_lapse.js
(replace extension for .ijm to run it inside imagej/Fiji)
imageJ macro to plot intensities from selection (p.eg. line) from stack/timelapse.
outputs file "plot_data.csv" which can be visualise with "" in python

## imageJ -> plot visualiser
takes as input the .csv file created from macro "plot_profile_time_lapse.js" and outputs .ens vector plot
