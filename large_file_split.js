original = getTitle();
path = getDirectory("image");
slices = "1-15"; //here you set the z-stack interval to be used
channel = 1; //set the channel
frames = 61 //set total frame number from acquisition to process
title = "mef2_mDendra2__25hAPF_APC_";
print (title);

setBatchMode(true);

for (f = 1; f < frames + 1; f++) { //f here stands for the "frame" number, in the time lapse
	selectWindow(original);
	makeRectangle(660, 519, 1194, 1398);
	run("Duplicate...", "title=duplicate channels="+channel+" duplicate slices="+slices+" frames="+f);
	rename(title + "c" + channel + "_frame_" + f);
	new_title = getTitle();
	print (new_title);

//	for (i = 1; i <= nSlices; i++) {
//		selectWindow(new_title);
//    	setSlice(i);
//    	resetMinAndMax();
//		run("Enhance Contrast", "saturated=0.35");
//		run("Apply LUT", "slice");
//		
//	}

	selectWindow(new_title);
//	run("Enhance Contrast", "saturated=0.35");
//	run("Apply LUT", "stack"); //this applies the same intensity range within a 16-bit space
							   //changing to 8-bit before Z-projecting adds too much background noise
	run("Z Project...", "projection=[Max Intensity]");
//	run("8-bit");
	//run("Enhance Contrast", "saturated=0.35");
	save_path = path + "channel_" + channel + "/";
	File.makeDirectory(save_path);
	saveAs("tiff", save_path + "MAX_" + new_title);
	new = getTitle();
	print (new);
	close(new);
	//selectWindow(new_title);
	//run("Z Project...", "projection=[Standard Deviation]");
	//run("Enhance Contrast", "saturated=0.35");
	//run("8-bit");
	//saveAs("tiff", path + "STD_" + new_title);
	close(new_title + ".tif");
	close(new_title);

	// Display Window Titles
	//
	// Displays the titles of image and non-image windows.

  	list = getList("image.titles");
  	 if (list.length==0)
	    print("No image windows are open");
	 else {
	     print("Image windows:");
	     for (i=0; i<list.length; i++)
	        print("   "+list[i]);
	  }
	 print("");

	 list = getList("window.titles");
	  if (list.length==0)
	     print("No non-image windows are open");
	  else {
	     print("Non-image windows:");
	     for (i=0; i<list.length; i++)
	        print("   "+list[i]);
	  }
	  print("");
	run("Collect Garbage");
}
