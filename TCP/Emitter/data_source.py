# It should be changed to the actual image processing
# results from the raspberry
import cv2
import numpy as np
import Emitter_class

data = Emitter_class.emitter()

array = np.round(np.random.rand(2,2))
arr_str = np.array2string(array)

data.send(arr_str)