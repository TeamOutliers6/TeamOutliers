# Visceral Fat and Lung Cancer

This is a healthcare related project where **Image Processing** and **Deep learning** models along with **Computer Vision libraries**  are used for image segmentation and area calculation of fat regions to calculate the *Visceral Fat Index (VFI)* in the CT scan images of 30 patients. 

The details of each folder is as below :

## Date-Preprocessing
The 30 raw input dataset images were pre-processed by removing the region of interest, thresholding and adjusting the brightness and contrast to make it more clear before using it for the segmentation. The breakdown of the files are as follows:
- **Extracting ROI.ipynb**
  The central region of the raw images is the region of interest that contains the fat, bone and muscles. This code is used to extarct just the central region of interest (ROI).   In order to run this code the file **contour_lib.py** is required to be imported.
  
- **L3_deblur&threshold.ipynb**
  The central region extracted from the raw input images is further cleaned by applying thresholding technique and removing the blurrness to make the image more clear and        understandable for segmentation.
## Deep Learning Segmentation Models
## ProjectFlow_Diagram



## Raw_Input_Images 
## StreamLit Library
## VAT Segmented Outputs
## VFI for 30 images.xlsx


