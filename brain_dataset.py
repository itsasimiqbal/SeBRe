# Developing Brain Atlas through Deep Learning
# Asim Iqbal, Romesa Khan, Theofanis Karayannis

"Custom functions for loading Brain Dataset "

import utils
import os
import glob #for selecting png files in training images folder
from natsort import natsorted, ns #for sorting filenames in a directory
import skimage
from skimage import io
import numpy as np


########### Create training dataset:

class BrainDataset_Train(utils.Dataset):
    """Generates the brain section dataset. The dataset consists of locally stored 
    brain section images, to which file access is required.
    """

    #see utils.py for default def load_image() function; modify according to your dataset
    
    def load_brain(self): 
        """
        for naming image files follow this convention: '*_(image_id).jpg'
        """
        
        os.chdir('C:\\Users\\Asfandyar\\Documents\\Romesa\\Scene_Parsing\\Code\\Mask_RCNN\\NatMachIntell_Code_FINAL\\DATASETsubmit')
        
        self.add_class('brain','1','cortex:')
        self.add_class('brain','2','hippocampus:')
        self.add_class('brain','3','basal ganglia:')
        self.add_class('brain','4','thalamus:')
        self.add_class('brain','5','prethalamus:')
        self.add_class('brain','6','midbrain:')
        self.add_class('brain','7','hindbrain:')
        self.add_class('brain','8','telencephalic vesicle:')
        
        
        training_images_folder = 'mrcnn_train_dataset_images'
        os.chdir(training_images_folder)
        im_id = 0
        cwd = os.getcwd()
        img_list = glob.glob('*.jpg')
        img_list = natsorted(img_list, key=lambda y: y.lower())
        #print(img_list)
        for i in img_list:  #image_ids start at 0 (to keep correspondence with load_mask which begins at image_id=0)!
            img = skimage.io.imread(i) #grayscale = 0
            im_dims = np.shape(img)
            self.add_image("brain", image_id=im_id, path = cwd+'/'+glob.glob('*_'+str(im_id)+'.jpg')[0],height = im_dims[0], width = im_dims[1])#, depth = im_dims[2])
            im_id += 1
            #print(im_dims)
            
            
    
    def load_mask(self,image_id):
        """Load instance masks for the given image.
        Different datasets use different ways to store masks. This
        function converts the different mask format to one format
        in the form of a bitmap [height, width, instances].

        Returns:
        masks: A bool array of shape [height, width, instance count] with
            one mask per instance.
        class_ids: a 1D array of class IDs of the instance masks."""
        
        os.chdir('C:\\Users\\Asfandyar\\Documents\\Romesa\\Scene_Parsing\\Code\\Mask_RCNN\\NatMachIntell_Code_FINAL\\DATASETsubmit')
        #print(image_id)
        masks_folder = 'mrcnn_train_dataset_masks'
        os.chdir(masks_folder)
        subfolder = glob.glob('*_'+str(image_id))[0]#add 1 to image_id, to get to correct corresponding masks folder for a given image 
        #print(subfolder)
        os.chdir(subfolder) 
        
        info = self.image_info[image_id] 
        #print(info)
        mk_list = glob.glob('*.png')
        #print(mk_list)
        count = len(mk_list)
        mk_id = 0
        mask = np.zeros([info['height'], info['width'], count], dtype=np.uint8)
        #print(np.shape(mask))
        class_ids = np.zeros(count)
        
        for m in mk_list:
            bin_mask = skimage.io.imread(m,as_grey=True) # grayscale=0
            mk_size = np.shape(bin_mask)
            mask[:, :, mk_id]= bin_mask
            
            # Map class names to class IDs.
            class_ids[mk_id] = m[-5] #fifth last position from mask_image name = class_id #need to update(range) if class_ids become two/three-digit numbers 
            mk_id += 1
        return mask, class_ids.astype(np.int32)
    
    
    
    
    
    
########### Create validation dataset:   

class BrainDataset_Val(utils.Dataset):
    """Generates the brain section dataset. The dataset consists of locally stored 
    brain section images, to which file access is required.
    """

    #see utils.py for default def load_image() function; modify according to your dataset
    
    def load_brain(self): 
        """
        for naming image files follow this convention: '*_(image_id+1).jpg'
        """
        
        os.chdir('C:\\Users\\Asfandyar\\Documents\\Romesa\\Scene_Parsing\\Code\\Mask_RCNN\\NatMachIntell_Code_FINAL\\DATASETsubmit')
        
        self.add_class('brain','1','cortex:')
        self.add_class('brain','2','hippocampus:')
        self.add_class('brain','3','basal ganglia:')
        self.add_class('brain','4','thalamus:')
        self.add_class('brain','5','prethalamus:')
        self.add_class('brain','6','midbrain:')
        self.add_class('brain','7','hindbrain:')
        self.add_class('brain','8','telencephalic vesicle:')
        
        
        training_images_folder = 'mrcnn_val_dataset_images'
        os.chdir(training_images_folder)
        im_id = 0
        cwd = os.getcwd()
        img_list = glob.glob('*.jpg')
        img_list = natsorted(img_list, key=lambda y: y.lower())
        #print(img_list)
        for i in img_list:  #image_ids start at 0 (to keep correspondence with load_mask which begins at image_id=0)!
            img = skimage.io.imread(i) #grayscale = 0
            im_dims = np.shape(img)
            self.add_image("brain", image_id=im_id, path = cwd+'/'+glob.glob('*_'+str(im_id)+'.jpg')[0],height = im_dims[0], width = im_dims[1])#, depth = im_dims[2])
            im_id += 1
            #print(im_dims)
            
            
    
    def load_mask(self,image_id):
        """Load instance masks for the given image.
        Different datasets use different ways to store masks. This
        function converts the different mask format to one format
        in the form of a bitmap [height, width, instances].

        Returns:
        masks: A bool array of shape [height, width, instance count] with
            one mask per instance.
        class_ids: a 1D array of class IDs of the instance masks."""
        
        os.chdir('C:\\Users\\Asfandyar\\Documents\\Romesa\\Scene_Parsing\\Code\\Mask_RCNN\\NatMachIntell_Code_FINAL\\DATASETsubmit')
        #print(image_id)
        masks_folder = 'mrcnn_val_dataset_masks'
        os.chdir(masks_folder)
        subfolder = glob.glob('*_'+str(image_id))[0]#add 1 to image_id, to get to correct corresponding masks folder for a given image 
        #print(subfolder)
        os.chdir(subfolder) 
        
        info = self.image_info[image_id] 
        #print(info)
        mk_list = glob.glob('*.png')
        #print(mk_list)
        count = len(mk_list)
        mk_id = 0
        mask = np.zeros([info['height'], info['width'], count], dtype=np.uint8)
        #print(np.shape(mask))
        class_ids = np.zeros(count)
        
        for m in mk_list:
            bin_mask = skimage.io.imread(m,as_grey=True) 
            mk_size = np.shape(bin_mask)
            mask[:, :, mk_id]= bin_mask
            
            # Map class names to class IDs.
            class_ids[mk_id] = m[-5] #fifth last position from mask_image name = class_id #need to update(range) if class_ids become two/three-digit numbers 
            mk_id += 1
        return mask, class_ids.astype(np.int32)



