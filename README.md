# Visceral Fat and Lung Cancer
![](https://img.shields.io/badge/CODE-PYTHON-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/version-3.7.3-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Computer_Vision-4.5.1-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Domain-Healthcare-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

This is a healthcare related project where **Image Processing** and **Deep learning** models along with **Computer Vision libraries**  are used for image segmentation and area calculation of fat regions to calculate the *Visceral Fat Index (VFI)* in the CT scan images of 30 patients. 

The details of each folder is as below :
# Table of Contents

* [Data-Preprocessing](#Data-Preprocessing)
* [Deep_Learning_Segmentation_Models](#Deep_Learning_Segmentation_Models)
* [ProjectFlow_Diagram](#ProjectFlow_Diagram)
* [Raw_Input_Images](#Raw_Input_Images)
* [StreamLit-Library](#StreamLit-Library)
* [VAT_Segmented_Outputs](#VAT_Segmented_Outputs)
* [VFI_for_30_images.xlsx](#VFI_for_30_images.xlsx)


## Data-Preprocessing
The 30 raw input dataset images were pre-processed by removing the region of interest, thresholding and adjusting the brightness and contrast to make it more clear before using it for the segmentation. The breakdown of the files are as follows:
- **Extracting ROI.ipynb**
  The central region of the raw images is the region of interest that contains the fat, bone and muscles. This code is used to extarct just the central region of interest (ROI).   In order to run this code the file **_contour_lib.py_** is required to be imported.
  
- **L3_deblur&threshold.ipynb**
  The central region extracted from the raw input images is further cleaned by applying thresholding technique and removing the blurrness to make the image more clear and        understandable for segmentation.
  
  The complete images pre-processing workflow is as below :
  ![image](https://user-images.githubusercontent.com/79048779/116161387-a9a51780-a6c1-11eb-8d8d-d527872f7e34.png)


## Deep_Learning_Segmentation_Models
The clean and pre-processed images are used for segmentation of SAT and VAT in order to calculate the Visceral fat Index (VFI). The breakdown of each file inside this folder is as below :
- **K-Means Segmentation**
  This folder contains the *Kmeansegmentation.ipynb* file where segmentation was doene on ImageJ created images to segment the fat region from the bone, muscle and other elements.However VFI calculation was not successfull using this algorithm. 

- **Segmentation CNN**
  This was the second approach where Convolutional Neural Networks was used for VAT and SAT segmentation using Conv 1D and 2D. The files *SegCnn.ipynb* and *SegCnn_v3.ipynb* has a 1D CNN used with 1 imaged and 30 images respectively. The file *SegCnn_v4.ipynb* shows the code for 2D CNN used with 30 input images. This algorithm did not perform as expected and could not segment the SAT and the VAT.
  
- **Segmentation using CV**
  This was a successful approach where VAT was extracted from the image using **Computer Vision** which was then used for VFI calculation. It is the same code as the Extractionof Region of Interest use din data pre-processing and requires the file  **_contour_lib.py_** to be imported. Below is and example :
  ![image](https://user-images.githubusercontent.com/79048779/116163054-03f3a780-a6c5-11eb-9c74-12cc5a103857.png)

- **U-NET Algorithm**
  This folder contains the code for the VAT and SAT segmentation using a complex network called U-NET. This approach did not yield the results as expected.

## ProjectFlow_Diagram
The whole workflow of this project from the start to the end is shown in this project Flow Diagram. It contains the errors we faced during the implementation of various algorithms and also outcomes of the succesfull ones.
![image](https://user-images.githubusercontent.com/79048779/116178369-73788f80-a6e3-11eb-9dd0-470f4c16fe9f.png)


## Raw_Input_Images
This folder contains 30 raw input dataset images which was used for pre-processing and later segmentation.

![image](https://user-images.githubusercontent.com/79048779/116176493-3b238200-a6e0-11eb-89ee-74f8af5be2f3.png)


## StreamLit-Library

- StreamLit is an open source application framework in python library, which creates an easy way to share beautiful and custom web pages to deploy the images to get outputs. - It also allows the users to quickly build interactive web applications about their models.
- The main purpose of this approach is to provide graphical user interface, where it will create a webpage user interface where a common person with no background knowledge  on image processing can easily view or play around with these images. 
- It can also be considered as an easiest way of viewing the output images.

![image](https://user-images.githubusercontent.com/79048779/116176717-a2d9cd00-a6e0-11eb-8002-4c0d46597270.png)


## VAT_Segmented_Outputs

This folder contains the 30 VAT segmented images from the 30 input images, where we can clearly see the segmeted region with VAT. This can be clearly observed when raw image and segemented image is compared.

## VFI_for_30_images.xlsx

This file contains the VFI(Visceral Fat Index) which is calculated for the 30 images of the dataset. It can be seen in the file where it shows the calculated VFI using CV algorithm and VFI using ImageJ tool.
