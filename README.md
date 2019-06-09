Iqbal, Asim, Romesa Khan, and Theofanis Karayannis. "Developing Brain Atlas through Deep Learning." arXiv preprint arXiv:1807.03440 (2018). [I'm an inline-style link](https://arxiv.org/abs/1807.03440)

To run SeBRe demo:
Run the following notebook to reproduce the results of SeBRe results.

![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_block_diagram.png)

To train SeBRe on your (custom) dataset:
1. Collect brain sections and place each of them in a separate folder with the following naming convention e.g. 

2. Draw ground-truth (binary) masks on Regions of Interest (ROIs) e.g. cortex, hippocampus, etc. using a scalar vector graphics (SVG) software such as Boxy SVG [Ref], RectLabel [Ref], Inkscape [Ref], etc. and assign a unique color code to each ROI. In the figure below, mouse brain section is using before (a) and after (d) annotation by human expert. A zoomed-in examples of cortex (b) and hindbrain (c) are shown to precisely match the boundaries of masks with the corresponding ROIs. 
![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/Supp_figure_1.png)

3. Run the following notebook to generate the binary (black and white) masks to train SeBRe deep neural network (DNN). The notebook will generate the file names in SeBRe-readable format.

4. Run the following notebook to train the SeBRe DNN on your dataset.

5. Run the following notebook to test the SeBRe DNN on your dataset.
