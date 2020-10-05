# import the opencv library
import cv2
import time
import os.path

# define a video capture object
vid = cv2.VideoCapture(0)
count1 = time.time()
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if os.path.isfile('stopframe') :
        break
    nowtime = time.time()

    if nowtime > count1 + 1.0:
        count1 = nowtime
        cv2.imwrite('test.jpg', frame)
        print('Image Captured')
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

#import numpy as np
#import os
#import PIL
#import PIL.Image
#import tensorflow as tf
#import tensorflow_datasets as tfds
#
#print(tf.__version__)

#import pathlib
#dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
#data_dir = tf.keras.utils.get_file(origin=dataset_url,
#                                   fname='flower_photos',
#                                   untar=True)
#data_dir = pathlib.Path(data_dir)
#print(data_dir)