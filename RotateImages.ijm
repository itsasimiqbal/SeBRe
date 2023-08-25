//Rotate images, first in 2° angles CW, then 2° angles CCW. Saves as R/filename_r*angle*

#@ File (label = "Input directory", style = "directory") input
suffix1 = ".jpg";
suffix2 = ".png";
suffix3 = ".tif";
ouput_format = ".jpg";

list = getFileList(input);

output = input;
//File.makeDirectory(output);
// if (!File.exists(output))
//  exit("Unable to create directory");

setBatchMode(true);
processFolder(input);

function processFolder(input) {
	list = getFileList(input);
	list = Array.sort(list);
	for (i = 0; i < list.length; i++) {
		if(File.isDirectory(input + File.separator + list[i]))
			processFolder(input + File.separator + list[i]);
		if(endsWith(list[i], suffix1) || endsWith(list[i], suffix2) || endsWith(list[i], suffix3))
			processFile(input, output, list[i]);
	}
}

function processFile(input, output, file) {
	print("Processing: " + input + File.separator + file);
	print("Saving to: " + output);
	open(file);

	format = substring(file, lastIndexOf(file, ".")+1, lengthOf(file));

	for (angle = 2; angle <= 20; angle=angle+2) {
		selectWindow(file);
		run("Duplicate...", "duplicate");
		run("Rotate... ", "angle="+angle+" grid=1 interpolation=Bilinear enlarge");
		
		saveAs(ouput_format, output+"//"+replace(file, "."+format,"_r"+angle+ouput_format));
		print("saved as -- "+output+"//"+replace(file, "."+format,"_r"+angle+ouput_format));
		close;	
	}

	for (angle = -2; angle >= -20; angle=angle-2) {
		print(angle);
		selectWindow(file);
		run("Duplicate...", " ");
		run("Rotate... ", "angle="+angle+" grid=1 interpolation=Bilinear enlarge");
		
		saveAs(ouput_format, output+"//"+replace(file, "."+format,"_r"+angle+ouput_format));
		print("saved as -- "+output+"//"+replace(file, "."+format,"_r"+angle+ouput_format));
		close;	
	}
	run("Close All");
		
}