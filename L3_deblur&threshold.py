#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/content/gdrive')


# In[ ]:


get_ipython().run_line_magic('cd', '/content/gdrive/My Drive/')


# **Rutuja's attempt for Open CV**

# In[ ]:


pip install --upgrade pip


# In[ ]:


pip install opencv-python


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Thresholding images. Follow these steps after removing the blurred region as discussed.
import cv2 
import matplotlib.pyplot as plt
from PIL import ImageEnhance
from PIL import Image
from google.colab.patches import cv2_imshow
import seaborn as sns
import numpy as np
import pandas as pd
img = cv2.imread("sarcopenia-ai-master/Deblurred_Outputs/deblur30.jpg", 0)
blackAndWhiteImage = cv2.threshold(img, 118, 255,  cv2.THRESH_BINARY_INV +  cv2.THRESH_TOZERO )[1]
# x = cv2_imshow(blackAndWhiteImage)
cv2.imwrite('threshd.jpg', blackAndWhiteImage)

x = Image.open('threshd.jpg')
enhancer = ImageEnhance.Brightness(x)

enhanced_im = enhancer.enhance(3)
enhanced_im.save('sarcopenia-ai-master/Threshold_Outputs_Modified/thresh30.jpg')
enhanced_im
# cv2_imshow(blackAndWhiteImage)
# cv2.waitKey(0)
# cnts = cv2.findContours(blackAndWhiteImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# for c in cnts:
#     cv2.drawContours(blackAndWhiteImage, [c], -1, (0, 255, 0), 7)

# cv2_imshow(blackAndWhiteImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# In[ ]:


#!pip install scikit-image
from skimage import color
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
img = color.rgb2gray(io.imread('sarcopenia-ai-master/Rutuja_Outputs/output2.jpg'))
#print(np.shape(img))
fig = plt.figure(dpi=110)
plt.imshow(img, vmin=0.3, vmax=0.75, cmap='gray')
plt.axis('off')
plt.savefig('filter.jpg', transparent=True, bbox_inches='tight', pad_inches=0)


# In[ ]:


from PIL import ImageEnhance
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
xi = Image.open('filter.jpg')

enhancer = ImageEnhance.Contrast(xi)

enhanced_im = enhancer.enhance(1
                              )

enhanced_im.save('filter2.jpg')
enhanced_im


# In[ ]:


from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread('filter2.jpg')
print(img.shape)
imb = cv2.GaussianBlur(img, (1,1), 0)
print(imb.shape)

cv2.imwrite('sarcopenia-ai-master/Deblurred_Outputs/deblur6.jpg', img)


# In[ ]:




