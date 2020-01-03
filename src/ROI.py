# import sys
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import tensorflow as tf
# import cv2
# from normalization import word_normalization, letter_normalization
# import page
# import words
# #from normalization import word_normalization
#
# def roi_image(imagem):
#     crop = page.detection(imagem)
#     #implt(crop)
#     boxes = words.detection(crop)
#     lines = words.sort_words(boxes)
#
#     res = []
#     for line in lines:
#         [res.append(crop[y1:y2, x1:x2]) for (x1, y1, x2, y2) in line]
#
#     return res
