  

import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import os
import os.path
import sys
from PIL import Image
source_image = ""
# read the test image
# def imagePath(pathName):
def image():
    try:
        source_image = cv2.imread(sys.argv[1])
    except:
        source_image = cv2.imread('p1.png')
    # print(pathName)
    prediction = 'n.a.'

# checking whether the training data is ready
    PATH = './training.data'

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print ('training data is ready, classifier is loading...')
        print ('training data is being created...')
        open('training.data', 'w')
        color_histogram_feature_extraction.training()
        print ('training data is ready, classifier is loading...')

# get the prediction
    color_histogram_feature_extraction.color_histogram_of_test_image(source_image)
    prediction = knn_classifier.main('training.data', 'test.data')
    print('Detected color is:', prediction)
    cv2.putText(
    source_image,
    'Prediction: ' + prediction,
    (15, 45),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    200,
    )

# Display the resulting frame
# cv2.imshow('color classifier', source_image)
# Image.fromarray(source_image).show()
# cv2.namedWindow("output", cv2.WINDOW_AUTOSIZE)        # Create window with freedom of dimensions
    cv2.resizeWindow("output", 1000, 1000)              # Resize window to specified dimensions
# im = cv2.imread("earth.jpg")                        # Read image
    cv2.imshow("output", source_image)
    cv2.waitKey(0)
image()