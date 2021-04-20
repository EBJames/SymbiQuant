# !pip install pyyaml==5.1 

import torch, torchvision
print(torch.__version__, torch.cuda.is_available())
# !gcc --version
assert torch.__version__.startswith("1.7")
# !pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.7/index.html
# 
# '''
# !git clone https://github.com/facebookresearch/detectron2 detectron2_repo
# !pip install -e detectron2_repo
# '''

import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import cv2
# from google.colab.patches import cv2_imshow
import os
from os.path import isfile, join
import matplotlib.pyplot as plt
import math
import random
import re
# from google.colab import files


# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import ColorMode
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
# !git clone https://github.com/EBJames/Buchnearer.git
# from google.colab import drive
# drive.mount('/content/drive')
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.DATASETS.TRAIN = ("Buchnearer",)
cfg.DATASETS.TEST = ()   # no metrics implemented for this dataset
cfg.DATALOADER.NUM_WORKERS = 8 #number of cores loading an image at once - higher = faster, but more memory
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")  # initialize from model zoo
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.01 #If learn rate goes too low I get memory problems. I should look into optimization
cfg.SOLVER.MAX_ITER = 40000 #80000 is the most I've run, it doesn't cause much difference, I could even step this back to ~10-20. I should run a loss curve though.
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 1024   #reset from 100 in tutorial, #1024 in 20201103
#cfg.MODEL.ROI_HEADS.POSITIVE_FRACTION = 0.5 #default is 0.25 decides the fraction of ROIs that are foreground vs background
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1 
cfg.TEST.DETECTIONS_PER_IMAGE = 3000
cfg.SOLVER.CHECKPOINT_PERIOD = 1000

cfg.MODEL.ANCHOR_GENERATOR.SIZES = [[32], [64], [128], [128]]
cfg.MODEL.ANCHOR_GENERATOR.ASPECT_RATIOS = [[1.0]]
cfg.MODEL.RPN.IN_FEATURES = ["p2", "p3", "p4", "p5"]

# cfg.MODEL.ANCHOR_GENERATOR.SIZE = [[8], [16], [32], [64], [128]]
# cfg.MODEL.ANCHOR_GENERATOR.ASPECT_RATIOS = [[1.0]]
# cfg.MODEL.ANCHOR_GENERATOR.STRIDES=[1, 1, 1, 1, 1]
# cfg.OUTPUT_DIR = "/content/drive/My Drive/Buchnearer"

# cfg.MODEL.WEIGHTS = "/content/drive/My Drive/Buchnearer/model_20200618"
# cfg.MODEL.WEIGHTS = "/content/drive/My Drive/Buchnearer/zoomed_only_20201113.pth"
# cfg.MODEL.WEIGHTS = "/content/drive/My Drive/Buchnearer/20201124_split_cell_train.pth"
cfg.MODEL.WEIGHTS = "/home/xupan/Projects/Buchnearer/20210410_30000.pth"

''' 
I haven't got this loading from previous models yet, 
from detectron2.config import get_cfg
from detectron2.engine import DefaultTrainer
cfg = get_cfg()
cfg.MODEL.WEIGHTS = "/content/model_20200618"
'''
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set the testing threshold for this model, higher = more certainty but worse inclusion, lower = less certainty, but better inclusion
cfg.TEST.DETECTIONS_PER_IMAGE = 5000 #max number of objects per image. 5000 should be overkill, I think there are rarely more than 2000
cfg.DATASETS.TEST = ("Buchnearer", )

# cfg.MODEL.ANCHOR_GENERATOR.SIZE = [[32], [64], [128], [256], [512]]
# cfg.MODEL.ANCHOR_GENERATOR.ASPECT_RATIOS = [[1.0]]
# cfg.MODEL.ANCHOR_GENERATOR.STRIDES=[1, 1, 1, 64, 64]

predictor = DefaultPredictor(cfg)

#evaluator = COCOEvaluator("Buch_test", cfg,
#                          False, output_dir=cfg.OUTPUT_DIR)
#val_loader = build_detection_test_loader(cfg, "Buch_test")
#inference_on_dataset(trainer.model, val_loader, evaluator)

from Buchnearer import Buchnearer_detector
input_path = '/home/xupan/Projects/Buchnearer/test_image_by_age'
for f in os.listdir(input_path):
    age_folder = join(input_path, f)
    for im in os.listdir(age_folder):
        if im[-1] == 'g':
            print(im)
            output_path = join(age_folder,'Prediction')
            Buchnearer_detector(join(age_folder, im),join(output_path, im),predictor, visualize=True, save_result=True)