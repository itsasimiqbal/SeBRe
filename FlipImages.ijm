//Rotate images, first in 2° angles CW, then 2° angles CCW. Saves as R/filename_r*angle*

#@ File (label = "Input directory", style = "directory") input
suffix = ".png";
ouput_format = ".png";

output = "/Users/Dana/Desktop/Research/BSt/MASKS/BW-MASKS-4/FLIP/A1";


for (i = 0; i < list.length; i++) {
	if (i % 21 == 0) {
		File.makeDirectory(output + "/" + list[i]);
		 if (!File.exists(output))
		  exit("Unable to create directory");
	}
}

//setBatchMode(true);
//processFolder(input);
//
//
//function processFolder(input) {
//	list = getFileList(input);
//	list = Array.sort(list);
//	for (i = 0; i < list.length; i++) {
//		if(File.isDirectory(input + File.separator + list[i]))
//			processFolder(input + File.separator + list[i]);
//		if(endsWith(list[i], suffix))
//			processFile(input, output, list[i]);
//	}
//}
//
//function processFile(input, output, file) {
//	print("Processing: " + input + File.separator + file);
//	print("Saving to: " + output);
//	open(file);
//
//	format = substring(file, lastIndexOf(file, ".")+1, lengthOf(file));
//
//	for (angle = 20; angle <= 360; angle=angle+20) {
//		selectWindow(file);
//		run("Duplicate...", "duplicate");
//		run("Rotate... ", "angle="+angle+" grid=1 interpolation=Bilinear enlarge");
//		
//		saveAs(ouput_format, output+"//"+replace(file, "."+format,"_r"+angle+ouput_format));
//		print("saved as -- "+output+"//"+replace(file, "."+format,"_r"+angle+ouput_format));
//		close;	
//	}
//
//	for (angle = 20; angle <= 360; angle=angle+20) {
//		selectWindow(file);
//		run("Duplicate...", "duplicate");
//		run("Flip horizontally")
//		run("Rotate... ", "angle="+angle+" grid=1 interpolation=Bilinear enlarge");
//		
//		saveAs(ouput_format, output+"//"+replace(file, "."+format,"_hor_r"+angle+ouput_format));
//		print("saved as -- "+output+"//"+replace(file, "."+format,"_hor_r"+angle+ouput_format));
//		close;	
//	}
//
//	for (angle = 20; angle <= 360; angle=angle+20) {
//		selectWindow(file);
//		run("Duplicate...", "duplicate");
//		run("Flip vertically")
//		run("Rotate... ", "angle="+angle+" grid=1 interpolation=Bilinear enlarge");
//		
//		saveAs(ouput_format, output+"//"+replace(file, "."+format,"_ver_r"+angle+ouput_format));
//		print("saved as -- "+output+"//"+replace(file, "."+format,"_ver_r"+angle+ouput_format));
//		close;	
//	}
//	run("Close All");
//		
//}