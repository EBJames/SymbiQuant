import cv2
import pickle
import numpy as np
import copy
import hashlib

_COLORS = np.array(
    [
        0.000, 0.447, 0.741,
        0.850, 0.325, 0.098,
        0.929, 0.694, 0.125,
        0.494, 0.184, 0.556,
        0.466, 0.674, 0.188,
        0.301, 0.745, 0.933,
        0.635, 0.078, 0.184,
        1.000, 0.000, 0.000,
        1.000, 0.500, 0.000,
        0.749, 0.749, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 1.000,
        0.667, 0.000, 1.000,
        0.333, 0.667, 0.000,
        0.333, 1.000, 0.000,
        0.667, 0.333, 0.000,
        0.667, 0.667, 0.000,
        0.667, 1.000, 0.000,
        1.000, 0.333, 0.000,
        1.000, 0.667, 0.000,
        1.000, 1.000, 0.000,
        0.000, 0.667, 0.500,
        0.000, 1.000, 0.500,
        0.333, 0.000, 0.500,
        0.333, 0.667, 0.500,
        0.333, 1.000, 0.500,
        0.667, 0.000, 0.500,
        0.667, 0.333, 0.500,
        0.667, 1.000, 0.500,
        1.000, 0.000, 0.500,
        1.000, 0.333, 0.500,
        1.000, 0.667, 0.500,
        1.000, 1.000, 0.500,
        0.000, 0.333, 1.000,
        0.000, 0.667, 1.000,
        0.000, 1.000, 1.000,
        0.333, 0.000, 1.000,
        0.333, 0.333, 1.000,
        0.333, 0.667, 1.000,
        0.333, 1.000, 1.000,
        0.667, 0.000, 1.000,
        0.667, 0.333, 1.000,
        0.667, 0.667, 1.000,
        0.667, 1.000, 1.000,
        1.000, 0.000, 1.000,
        1.000, 0.333, 1.000,
        1.000, 0.667, 1.000,
        0.667, 0.000, 0.000,
        0.833, 0.000, 0.000,
        1.000, 0.000, 0.000,
        0.000, 0.667, 0.000,
        0.000, 0.833, 0.000,
        0.000, 0.000, 0.667,
        0.000, 0.000, 0.833,
        0.000, 0.000, 1.000,
    ]
).astype(np.float32).reshape(-1, 3)

def __add_all_masks(image, masks, color):
        mask_image = copy.deepcopy(image)
        for i in range(len(masks)):
            for (a,b) in masks[i]:
                mask_image[a,b,:] = mask_image[a,b,:]*0.5 + color[i]*255*0.5
        return mask_image

def get_segimg(im_file, result_file, output_file):
	image = cv2.imread(im_file)
	with open(result_file, 'rb') as dbfile:      
	            result = pickle.load(dbfile)
	masks = result['masks']
	assigned_colors = [_COLORS[int(hashlib.sha256(str(masks[i]).encode('utf-8')).hexdigest(), 16) % 55] for i in range(len(masks))]
	segimage = __add_all_masks(image, masks, assigned_colors)
	cv2.imwrite(output_file, segimage)

def get_cellcount(result_file):
	with open(result_file, 'rb') as dbfile:      
	            result = pickle.load(dbfile)
	return len(result['masks'])

'''
# get new segmentation images:
input_path = '/home/xupan/Projects/Buchnearer/test_image_by_age'
for f in os.listdir(input_path):
    age_folder = join(input_path, f)
    for im in os.listdir(age_folder):
        if im[-1] == 'g':
            print(im)
            result_file = ... # find result here (maybe from "age_foler" & "im").
            output_file = join(im,'_corrected.png') # change this
            get_segimg(im, result_file, output_file)
'''

'''
# get cell count:
count_file = ...
input_path = '/home/xupan/Projects/Buchnearer/test_image_by_age'
for f in os.listdir(input_path):
    age_folder = join(input_path, f)
    for result in os.listdir(age_folder):
        if im[-1] == 'g':
            count = get_cellcount(result)
            with open(count_file, 'w') as f:
                f.write(im + str(count) +'\n')
'''