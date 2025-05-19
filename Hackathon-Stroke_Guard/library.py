from tqdm import tqdm
import zipfile
import os
from ultralytics import YOLO
import shutil
import random
import cv2
import numpy as np
import yaml
import matplotlib.pyplot as plt
from IPython.display import Audio, display
from glob import glob
from IPython.display import display, clear_output
import PIL.Image

!pip freeze > requirements.txt # yolov11n.pt 파일 생성 확인
!yolo predict
