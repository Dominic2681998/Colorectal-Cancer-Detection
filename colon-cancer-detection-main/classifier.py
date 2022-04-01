from matplotlib import image
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
from keras.layers import Conv2D,MaxPool2D,Dropout,Flatten,BatchNormalization,GlobalAvgPool2D
from keras.models import Sequential
from keras.preprocessing.image import load_img,img_to_array,ImageDataGenerator
import cv2
from scipy.ndimage.filters import convolve
from skimage import io
from skimage.filters import median 

def load(imgname):
    colorimage=cv2.imread("static/uploads/"+imgname)
    colorimage = cv2.medianBlur(colorimage, 3)#median filter
    #CLAHE
    clahe_model = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    colorimage_b = clahe_model.apply(colorimage[:,:,0])
    colorimage_g = clahe_model.apply(colorimage[:,:,1])
    colorimage_r = clahe_model.apply(colorimage[:,:,2])
    colorimage_clahe = np.stack((colorimage_b,colorimage_g,colorimage_r), axis=2)
    image=cv2.resize(colorimage_clahe,(224,224))
    return image



def classify(imgname):
    
    model = keras.models.load_model('model/newmodel.h5')
    image=load(imgname)
    #image =load_img("static/uploads/"+imgname,target_size=(224,224))
    input_arr=img_to_array(image)/255#dividing the imag by 255 to normalise the image
    input_arr=np.expand_dims(input_arr,axis=0)
    pred=(model.predict(input_arr)[0][0] > 0.5).astype("int32")
    return pred

#def classify(imgname):

    #image = read_image("static/uploads/"+imgname)
    

   # p = predict_x(x)
    
    #return p


