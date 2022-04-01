import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
from keras.layers import Conv2D,MaxPool2D,Dropout,Flatten,BatchNormalization,GlobalAvgPool2D
from keras.models import Sequential
from keras.preprocessing.image import load_img,img_to_array,ImageDataGenerator






def classify(imgname):
    
    model = keras.models.load_model('model/bestmodel.h5')
    image =load_img("static/uploads/"+imgname,target_size=(224,224))
    input_arr=img_to_array(image)/255#dividing the imag by 255 to normalise the image
    input_arr=np.expand_dims(input_arr,axis=0)
    pred=(model.predict(input_arr)[0][0] > 0.5).astype("int32")
    return pred

#def classify(imgname):

    #image = read_image("static/uploads/"+imgname)
    

   # p = predict_x(x)
    
    #return p


