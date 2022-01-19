//To be edited here BEFORE running macro:

interval_acquired=10; //change for time lapse interval during acquisition in minutes
interval_analysis=10; //change for interval time steps wanted for analysis, in minutes (1 point every 1min, every 10min, etc)
duration_analysis = 60; //change for total interval to be considered for analysis, in minutes

//macro starts
frame_step=interval_analysis/interval_acquired;
frames = duration_analysis / interval_acquired;


filePath = getDirectory("Choose the directory where to save the Results"); //where to save Results table

waitForUser("Make sure a line selection has been made on the image stack"); //user confirms a line has been drawn

//to edit depending on which channel to analyse
//a=getTitle();
//run("Split Channels");
//selectWindow("C2-" + a); //to select the channel for analysis

//make sure file is formatted correctly so that "frames"  refers to time lapse
//if "slices" leads to time step, switch above order of "slices" and "frames";
//should look like "getDimensions(width, height, channels, frames, slices);"
getDimensions(width, height, channels, frames, slices);
print(frames);

//below is to cycle through all ROI determined by the Ridge Detection plugin and measure
//the distances between bright dots in the GFP channel
for (frame=0 ; frame<frames; frame=frame+frame_step) {
	//wait for user input to draw the line
	Roi.setPosition(frame);
	roiManager("Add");
}	

roiManager("Multi Plot");	
plot=getTitle();
print(plot);
Plot.showValues();
plot_data = filePath + "plot_data.csv";
Table.save(plot_data);
//	close(plot);
//	close(peaksinplot);


//note to self:
//https://forum.image.sc/t/saving-results-from-plot-values-into-arrays-in-imagej-macro/10438/21
