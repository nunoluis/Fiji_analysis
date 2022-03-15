# Fiji_analysis
macros and python scripts to analyse microscopy data

Tips on markdown styles and formating [here](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

## plot_profile_time_lapse.js
(replace extension for .ijm to run it inside imagej/Fiji)
imageJ macro to plot intensities from selection (p.eg. line) from stack/timelapse.
outputs file "plot_data.csv" which can be visualise with "" in python

## plot_from_macro.py - imageJ -> plot visualiser
takes as input the .csv file created from macro "plot_profile_time_lapse.js" and outputs .ens vector plot

## curve_fit_inhib_response.py
made for Sarah inhibition response assays. Can be model for curve_fit approaches, when changing the objective equation model to whatever is required.
It takes a .csv file and go through columns for data. In this case, the x values are repeated, so it skips 3 columns per loop. Output are parameters for curve fitting, plus experimental points overlayed on the model curve, re-plotted with the generated parameters.

## large_file_split.js
- from virtual file iterates through time lapse frames and generates max_projection for selected channel

##anim_hist
template for simple animation. Trying to get 2 plots overlaied, and clearing the figure in between frames.
