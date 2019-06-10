

# Developing Brain Atlas through Deep Learning
#### SeBRe (Segmenting Brain Regions) is a high-throughput Mask R-CNN [[1](https://arxiv.org/abs/1703.06870)]-based toolbox to generate brain atlas through deep learning.

#### [Iqbal, Asim, Romesa Khan, and Theofanis Karayannis. "Developing Brain Atlas through Deep Learning." arXiv preprint arXiv:1807.03440 (2018).](https://arxiv.org/abs/1807.03440)

# Download:
#### Clone the SeBRe repository by running the following command in your terminal window:
```
git clone https://github.com/itsasimiqbal/SeBRe.git
```
#### Additionally, download the (.zip) files by visiting the following link:
```
https://drive.google.com/open?id=1g_894zM_mSJGfudzzfnw-ZpN-rQ4qQdz
```
You would need ```DATASETSubmit.zip```, ```myDATASET.zip``` and ```SeBRe_FINAL_WEIGHTS.h5.zip``` to run the code in your machine. If you'd like to use the mouse and human brain atlas datasets used in our paper then also download and unzip ```SeBRe_Datasets.zip```. Once you've downloaded your files then unzip them in your folder by running the following commands:

```
unzip DATASETSubmit.zip
unzip myDATASET.zip
unzip SeBRe_FINAL_WEIGHTS.h5.zip
```
## SeBRe demo:
The block diagram of our system is demonstrated below:

![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_block_diagram.png)

Run the notebook [SeBRe_FINAL.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_FINAL.ipynb) to reproduce the results in SeBRe's paper. Make sure to install the necessary libraries in your machine before running the code. A step-by-step explanation of feature processing in SeBRe is provided in [SeBRe_feature_processing.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_feature_processing.ipynb) notebook.

![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/FP_SeBRe.png)
![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/FP_SeBRe_1.png)
![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/FP_SeBRe_2.png)

## To train SeBRe on your (custom) dataset:

__1__. Collect images of brain regions (or sub-regions) and place each of them in a separate folder with the following naming convention e.g. ```section_img_0.jpg, section_img_1.jpg, ...```

__2__. Draw ground-truth (binary) masks on Regions of Interest (ROIs) e.g. cortex, hippocampus, etc. using a scalar vector graphics (SVG) software such as Boxy SVG [[2](https://boxy-svg.com/)], RectLabel [[3](https://rectlabel.com/)], Inkscape [[4](https://inkscape.org/)], etc. and assign a unique color code to each ROI. In the figure below, mouse brain section is using before (a) and after (d) annotation by human expert. A zoomed-in examples of cortex (b) and hindbrain (c) are shown to precisely match the boundaries of masks with the corresponding ROIs. 
![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/Supp_figure_1.png)

__3__. Run the notebook [custom_dataset_create.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/custom_dataset_create.ipynb) to generate the binary (black and white) masks to train SeBRe deep neural network (DNN). The notebook will generate the file names in SeBRe-readable format, place them in the brain region corresponding folders e.g. ```section_masks_0/section_masks_0_m_1.png, sections_masks_0_m_2.png, ...```

![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_Masks.png)

__4__. Modify and run the notebook [SeBRe_training.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_training.ipynb) to train the SeBRe DNN on your (custom) dataset.

__5__. Modify and run the notebook [SeBRe_FINAL.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_FINAL.ipynb) to test the SeBRe DNN on your (custom) dataset.

## References:

[1] https://arxiv.org/abs/1703.06870

[2] https://boxy-svg.com/

[3] https://rectlabel.com/

[4] https://inkscape.org/
