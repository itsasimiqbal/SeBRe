![alt text](https://media.springernature.com/w440/springer-static/cover-hires/journal/42256/1/6)

# SeBRe 2.0 PyTorch support (2023 - New)!

#### SeBRe (*Se*gmenting *B*rain *Re*gions) is a high-throughput Mask R-CNN [[1](https://arxiv.org/abs/1703.06870)]-based toolbox to generate brain atlas through deep learning by instance segmentation of complex brain regions.

#### *Nature Machine Intelligence* article: [Asim Iqbal, et al. Developing a brain atlas through deep learning. Nature Machine Intelligence](https://rdcu.be/bGefW)
#### *arXiv* preprint: [SeBRe](https://arxiv.org/abs/1807.03440)

The Colab version of SeBRe is available here to train and test on your custom dataset: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1teNZGTeu3LU4jloSwVNvmcDmKxUwEaJf?usp=sharing)

# SeBRe 1.0 TensorFlow support!

## Download:
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
Following are the Python/library versions on which the SeBRe 1.0 code is tested to work fine:
- Python (3.5.2)
- Tensorflow (1.6.0)
- Keras (2.1.6)
- skimage (0.13.0)
- Numpy (1.13.3)
- Scipy (1.2.2)

## SeBRe demo:
The block diagram of our system is demonstrated below:

![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_block_diagram.png)

Run the notebook [SeBRe_FINAL.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_FINAL.ipynb) to reproduce the results in SeBRe's paper. Make sure to install the necessary libraries in your machine before running the code. A step-by-step explanation of feature processing in SeBRe is provided in [SeBRe_feature_processing.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_feature_processing.ipynb) notebook.

## To train SeBRe on your (custom) dataset:

__1__. Collect images of brain regions (or sub-regions) and place each of them in a separate folder with the following naming convention e.g. ```section_img_0.jpg, section_img_1.jpg, ...```

__2__. Draw ground-truth (binary) masks on Regions of Interest (ROIs) e.g. cortex, hippocampus, etc. using an annotation software such as Napari [[2](https://napari.org/)] and assign a unique color code to each ROI. In the figure below, mouse brain section is shown before (a) and after (d) annotation by human expert. A zoomed-in examples of cortex (b) and hindbrain (c) are shown to precisely match the boundaries of masks with the corresponding ROIs. 
![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/Supp_figure_1.png)

__3__. Run the notebook [custom_dataset_create.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/custom_dataset_create.ipynb) to generate the binary (black and white) masks to train SeBRe deep neural network (DNN). The notebook will generate the file names in SeBRe-readable format, place them in the brain region corresponding folders e.g. ```section_masks_0/section_masks_0_m_1.png, sections_masks_0_m_2.png, ...```

![alt text](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_Masks.png)

__4__. Modify and run the notebook [SeBRe_training.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_training.ipynb) to train the SeBRe DNN on your (custom) dataset.

__5__. Modify and run the notebook [SeBRe_FINAL.ipynb](https://github.com/itsasimiqbal/SeBRe/blob/master/SeBRe_FINAL.ipynb) to test the SeBRe DNN on your (custom) dataset.

## Sahni Lab Data:
This data was used to train models on brainstem images. Optimizations made to the model and to the data are reflected in this repository and the following datasets.

[1] [Training Data v1](https://drive.google.com/drive/folders/1zChrCERZjf-MvDK-nhNs_lEI5WlSkKh1?usp=share_link)
[2] [Training Data v2 (optimized for medulla)](https://drive.google.com/drive/folders/1oDAH5UlplUD08RXswktuuBsDD-vMXfAq?usp=share_link)

## References:

[1] https://arxiv.org/abs/1703.06870

[2] https://napari.org/

## Cite:
If you use any part of this code for your work, please cite the following:

```
Asim Iqbal, Romesa Khan, and Theofanis Karayannis. "Developing a brain atlas through deep learning." 
Nature Machine Intelligence 1.6 (2019): 277-287.
```
