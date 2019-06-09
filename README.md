Developing a Brain Atlas through Deep Learning

To run SeBRe demo:
Run the following notebook to reproduce the results of SeBRe results.

![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/Figure_1.png)

To train SeBRe on your (custom) dataset:
1. Collect brain sections and place each of them in a separate folder with the following naming convention e.g. 
2. Draw ground-truth (binary) masks on Regions of Interest (ROIs) e.g. cortex, hippocampus, etc. using a scalar vector graphics (SVG) software such as Boxy SVG [Ref], RectLabel [Ref], Inkscape [Ref], etc. and assign a unique color code to each ROI.
3. Run the following notebook to generate the binary (black and white) masks to train SeBRe deep neural network (DNN). The notebook will generate the file names in SeBRe-readable format.
4. Run the following notebook to train the SeBRe DNN on your dataset.
5. Run the following notebook to test the SeBRe DNN on your dataset.
