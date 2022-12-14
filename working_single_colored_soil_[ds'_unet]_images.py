# -*- coding: utf-8 -*-
"""WORKING SINGLE COLORED SOIL  [DS' UNET] Images.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17oBQZqnpEVNjmlFCookhHRAG7AEQLmH2

**RESET**
"""

from google.colab import drive
drive.mount('/content/drive')

RESET = True
import os
import shutil

# path for all the training images
TRAINING_IMAGES_PATH = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/msl/images/edr/"
# path for all the trianing labels (black and white masks)
TRAINING_MASKS_PATH = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/msl/labels/train/"
# path for all the testing images
TESTING_IMAGES_PATH = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/msl/images/edr/"
# path for all the testing labels (black and white masks)
TESTING_MASKS_PATH = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/msl/labels/test/masked-gold-min1-100agree/"
## LIMIT FOR THE NUMBER OF IMAGES TO BE LOADED

LIMIT = 1200
VALIDATION = int(LIMIT * 0.75)

def move_training_masks_back_RESET(pathDir):
    for name in os.listdir(path="/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/train_masks/"):
        add_path = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/train_masks/" + name
        print(add_path)
        shutil.move(add_path, pathDir)

    
def move_training_images_back_RESET(pathDir):
    for name in os.listdir(path="/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/train_images/"):
        add_path = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/train_images/" + name
        shutil.move(add_path, pathDir)

def move_validation_masks_back_RESET(pathDir):
    for name in os.listdir(path="/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_masks/"):
        add_path = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_masks/" + name
        shutil.move(add_path, pathDir)

    
def move_validation_images_back_RESET(pathDir):
    for name in os.listdir(path="/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_images/"):
        add_path = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_images/" + name
        shutil.move(add_path, pathDir)

def reset():
  move_training_masks_back_RESET(TRAINING_MASKS_PATH)
  move_training_images_back_RESET(TRAINING_IMAGES_PATH)
  move_validation_masks_back_RESET(TRAINING_MASKS_PATH)
  move_validation_images_back_RESET(TRAINING_IMAGES_PATH)

if RESET:
  reset()

"""***Importing Libraries and Initial Setup***"""

import torch
import torch.nn as nn
import torchvision.transforms.functional as TF

import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms

import numpy as np

counter = 0

# list to store the names above 
TRAINING_IMAGES_NAMES = list()
VALIDATION_IMAGES_NAMES = list()

counter = 0
for name in os.listdir(path=TRAINING_MASKS_PATH):
  add = name[:-4]
  counter += 1
  if counter == LIMIT:
    break
  if counter < VALIDATION:
      TRAINING_IMAGES_NAMES.append(add)
  else:
      VALIDATION_IMAGES_NAMES.append(add)

len(VALIDATION_IMAGES_NAMES)

counter = 0

# list to store the names above
TESTING_IMAGES_NAMES = list()

for name in os.listdir(path=TESTING_MASKS_PATH):
  add = name[:-11]
  TESTING_IMAGES_NAMES.append(add)
  counter += 1
  if counter == LIMIT:
    break

TESTING_IMAGES_NAMES

"""**Preprocessing Methods**

"""

def show_histogram(img):
  plt.hist(img.ravel(),256,[0,256]); plt.show()

import torchvision.transforms as transforms

# -------------- TRAINING DATA -------------------------
training_images = list()
training_masks = list()


def get_training_masks(pathDir):
    for name in TRAINING_IMAGES_NAMES:
        img = Image.open(pathDir + name + '.png')
        training_masks.append(img)
      


def get_training_images(pathDir):
    for name in TRAINING_IMAGES_NAMES:
        img = Image.open(pathDir + name + '.JPG')
        training_images.append(img)


# ------------------- VALIDATION DATA ------------------------

validation_images = list()
validation_masks = list()

def get_validation_masks(pathDir):
    for name in VALIDATION_IMAGES_NAMES:
        img = Image.open(pathDir + name + '.png')
        validation_masks.append(img)
      

def get_validation_images(pathDir):
    for name in VALIDATION_IMAGES_NAMES:
        img = Image.open(pathDir + name + '.JPG')
        validation_images.append(img)



# ---------------- TESTING DATA ------------------
testing_images = list()
testing_masks = list()

def get_testing_masks(pathDir):
    for name in TESTING_IMAGES_NAMES:
        img = Image.open(pathDir + name + '_merged.png')
        testing_masks.append(img)

def get_testing_images(pathDir):
    for name in TESTING_IMAGES_NAMES:
        img = Image.open(pathDir + name + '.JPG')
        testing_images.append(img)

# get_training_masks(TRAINING_MASKS_PATH) 
# get_training_images(TRAINING_IMAGES_PATH)

# get_validation_masks(TRAINING_MASKS_PATH) 
# get_validation_images(TRAINING_IMAGES_PATH)

# get_testing_masks(TESTING_MASKS_PATH)
# get_testing_images(TESTING_IMAGES_PATH)

"""**MOVE DATA**

"""

import shutil
# ------------------ RUN ONLY ONCE -----------------------
def move_training_masks(pathDir):
    for name in TRAINING_IMAGES_NAMES:
        shutil.move(pathDir + name + '.png', "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/train_masks")

    
def move_training_images(pathDir):
    for name in TRAINING_IMAGES_NAMES:
        shutil.move(pathDir + name + '.JPG', "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/train_images")

def move_validation_masks(pathDir):
    for name in VALIDATION_IMAGES_NAMES:
        shutil.move(pathDir + name + '.png', "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_masks")

    
def move_validation_images(pathDir):
    for name in VALIDATION_IMAGES_NAMES:
        shutil.move(pathDir + name + '.JPG', "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_images")

move_training_masks(TRAINING_MASKS_PATH)
move_training_images(TRAINING_IMAGES_PATH)

move_validation_masks(TRAINING_MASKS_PATH)
move_validation_images(TRAINING_IMAGES_PATH)

def change_pixel_values_mask(pix):
  zero_soil = 0
  one_br = 0
  two_sand = 0
  three_bigr = 0
  white = 0
  pixel_ttoal = 0

  BROWN_SOIL = True #[0] 
  BLUE_BR = False #[0, 0, 255]
  YELLOW_SAND = False #[255, 255, 0]
  RED_BIGR = False #[255, 0, 0]

  for y in range(IMG_HEIGHT):
    for x in range(IMG_WIDTH):
      pixel_ttoal = pixel_ttoal + 1
      pixel = pix[x, y]
      if pixel[0] == 0:
        zero_soil = zero_soil + 1
        pix[x, y] = BROWN_SOIL
      elif pixel[0] == 1:
        one_br = one_br + 1
        pix[x, y] = BLUE_BR
      elif pixel[0] == 2:
        two_sand = two_sand + 1
        pix[x, y] = YELLOW_SAND
      elif pixel[0] == 3:
        three_bigr = three_bigr + 1
        pix[x, y] = RED_BIGR
      elif pixel[0] == 255:
        white = white + 1

      
      

  print("Soil BROWN [0]: " + str(zero_soil) + " pixels")
  print("Bedrock BLUE [1]: " + str(one_br) + " pixels")
  print("Sand YELLOW [2]: " + str(two_sand) + " pixels")
  print("Bigrock RED [3]: " + str(three_bigr) + " pixels")
  print("None [255]: " + str(white) + " pixels")
  print("Total Pixels: " + str(pixel_ttoal) + " pixels")
  print("Added Total: " + str(zero_soil + one_br + two_sand + three_bigr + white) + " pixels\n")
  return pix

def change_mask_to_bool(img):
  ret = np.full((128, 128, 1), True)
  for y in range(IMG_HEIGHT):
    for x in range(IMG_WIDTH): 
      pix = img[x, y]
      if pix[0] == 0:
        ret[x, y] = True
      else:
        ret[x, y] = False
  return ret

def get_pixel(pix):
  for y in range(IMG_HEIGHT):
    for x in range(IMG_WIDTH):
      print("(" + str(x) + ", " + str(y) + "): " + str(pix[x,y]))
  print("\n")

def get_distribution(img):
  zero_soil = 0
  one_br = 0
  two_sand = 0
  three_bigr = 0
  white = 0
  pixel_ttoal = 0

  BROWN_SOIL = True #[0] 
  BLUE_BR = False #[0, 0, 255]
  YELLOW_SAND = False #[255, 255, 0]
  RED_BIGR = False #[255, 0, 0]

  for y in range(IMG_HEIGHT):
    for x in range(IMG_WIDTH):
      pixel_ttoal = pixel_ttoal + 1
      pixel = img[x, y]
      if pixel[0] == 0:
        zero_soil = zero_soil + 1
      elif pixel[0] == 1:
        one_br = one_br + 1
      elif pixel[0] == 2:
        two_sand = two_sand + 1
      elif pixel[0] == 3:
        three_bigr = three_bigr + 1
      elif pixel[0] == 255:
        white = white + 1

      
      

  print("Soil BROWN [0]: " + str(zero_soil) + " pixels")
  print("Bedrock BLUE [1]: " + str(one_br) + " pixels")
  print("Sand YELLOW [2]: " + str(two_sand) + " pixels")
  print("Bigrock RED [3]: " + str(three_bigr) + " pixels")
  print("None [255]: " + str(white) + " pixels")
  print("Total Pixels: " + str(pixel_ttoal) + " pixels")
  print("Added Total: " + str(zero_soil + one_br + two_sand + three_bigr + white) + " pixels\n")
  return img

def get_bool_distribution(img):
  zero_soil = 0
  white = 0
  pixel_ttoal = 0

  for y in range(IMG_HEIGHT):
    for x in range(IMG_WIDTH):
      pixel_ttoal = pixel_ttoal + 1
      pixel = img[x, y]
      if pixel[0] == True:
        zero_soil = zero_soil + 1
      elif pixel[0] == False:
        white = white + 1

      
      

  print("Soil BROWN [0]: " + str(zero_soil) + " pixels")
  print("None [255]: " + str(white) + " pixels")
  print("Total Pixels: " + str(pixel_ttoal) + " pixels")
  print("Added Total: " + str(zero_soil + white) + " pixels\n")
  return img

def display_img(img, cmap=None):
  fig = plt.figure(figsize=(5, 5))
  ax = fig.add_subplot(111)
  ax.imshow(img, cmap)

def display_boolean_mask(img):
  newImg = np.zeros((IMG_WIDTH,IMG_HEIGHT,IMG_CHANNELS)) * 255
  for y in range(IMG_HEIGHT):
    for x in range(IMG_WIDTH):
      pixel = img[x, y][0]
      if pixel == False:
        newImg[x, y] = (255, 255, 255)
      else:
        newImg[x, y] = (0, 0, 0)
  imshow(newImg)
  plt.show()
  return newImg

TRAINING_DATA_IMAGES = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/TRAIN/train_images/"
TRAINING_DATA_MASKS = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/TRAIN/train_masks/"
VALIDATION_DATA_IMAGES = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_images/"
VALIDATION_DATA_MASKS = "/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/validation_masks/"

TRAINING_DATA = '/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/'
TEST_DATA = '"/content/drive/MyDrive/Energy Analytics/ai4mars-dataset-merged-0.1/DATASET/"'

import random
import numpy as np
 
from tqdm import tqdm 

from skimage.io import imread, imshow
from skimage.transform import resize
import matplotlib.pyplot as plt

seed = 42
np.random.seed = seed

IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_CHANNELS = 3

TRAIN_PATH = TRAINING_DATA 
TEST_PATH = VALIDATION_DATA_IMAGES

train_ids = TRAINING_IMAGES_NAMES
test_ids = VALIDATION_IMAGES_NAMES

X_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
Y_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, 1), dtype=np.bool)
original_Y = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)

"""---------- Start of Data Processing ----------------"""

print('Resizing training images and masks')
# Training Images Resize
for n, id_ in tqdm(enumerate(train_ids), total=len(train_ids)):   
    path = TRAIN_PATH
    img = cv2.imread(path + 'train_images/' + id_ + '.JPG')[:,:, :IMG_CHANNELS]  
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_NEAREST)
    X_train[n] = img  #Fill empty X_train with values from img

# Training masks resize
for n, id_ in tqdm(enumerate(train_ids), total=len(train_ids)):   
    path = TRAIN_PATH
    img = cv2.imread(path + 'train_masks/' + id_ + '.png')[:,:, :IMG_CHANNELS]
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_NEAREST)
    original_Y[n] = img
    img = change_mask_to_bool(img)
    Y_train[n] = img  #Fill empty X_train with values from img



# test images resizing
X_test = np.zeros((len(test_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
sizes_test = []
print('Resizing test images') 
for n, id_ in tqdm(enumerate(test_ids), total=len(test_ids)):
    path = TEST_PATH + '/' + id_
    img = cv2.imread(path + '.JPG')[:,:,:IMG_CHANNELS]
    sizes_test.append([img.shape[0], img.shape[1]])
    img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
    X_test[n] = img

Y_test = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
# Testing masks resize
for n, id_ in tqdm(enumerate(test_ids), total=len(test_ids)):   
    path = VALIDATION_DATA_MASKS
    print(path + id_ + '.png')
    img = cv2.imread(path + id_ + '.png')[:,:, :IMG_CHANNELS]
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_NEAREST)
    Y_test[n] = img


print('Done!')

image_x = random.randint(0, len(train_ids))
imshow(X_train[image_x])
plt.show()
imshow(np.squeeze(original_Y[image_x]))
plt.show()

test = Y_train[image_x]

get_distribution(original_Y[image_x])
get_bool_distribution(test)
imshow(np.squeeze(original_Y[image_x]))
plt.show()
display_boolean_mask(test)

test[0, 0][0]

Y_train[0].shape

"""--- Start of the Model ----"""

#Build the model
import tensorflow as tf

inputs = tf.keras.layers.Input((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
s = tf.keras.layers.Lambda(lambda x: x / 255)(inputs)

#Contraction path
c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(s)
c1 = tf.keras.layers.Dropout(0.1)(c1)
c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c1)
p1 = tf.keras.layers.MaxPooling2D((2, 2))(c1)

c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p1)
c2 = tf.keras.layers.Dropout(0.1)(c2)
c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c2)
p2 = tf.keras.layers.MaxPooling2D((2, 2))(c2)
 
c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p2)
c3 = tf.keras.layers.Dropout(0.2)(c3)
c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c3)
p3 = tf.keras.layers.MaxPooling2D((2, 2))(c3)
 
c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p3)
c4 = tf.keras.layers.Dropout(0.2)(c4)
c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c4)
p4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(c4)
 
c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p4)
c5 = tf.keras.layers.Dropout(0.3)(c5)
c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c5)

#Expansive path 
u6 = tf.keras.layers.Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c5)
u6 = tf.keras.layers.concatenate([u6, c4])
c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
c6 = tf.keras.layers.Dropout(0.2)(c6)
c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)
 
u7 = tf.keras.layers.Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c6)
u7 = tf.keras.layers.concatenate([u7, c3])
c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
c7 = tf.keras.layers.Dropout(0.2)(c7)
c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)
 
u8 = tf.keras.layers.Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c7)
u8 = tf.keras.layers.concatenate([u8, c2])
c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
c8 = tf.keras.layers.Dropout(0.1)(c8)
c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)
 
u9 = tf.keras.layers.Conv2DTranspose(16, (2, 2), strides=(2, 2), padding='same')(c8)
u9 = tf.keras.layers.concatenate([u9, c1], axis=3)
c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
c9 = tf.keras.layers.Dropout(0.1)(c9)
c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)
 
outputs = tf.keras.layers.Conv2D(1, (1, 1), activation='sigmoid')(c9)
 
model = tf.keras.Model(inputs=[inputs], outputs=[outputs])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

################################
# #Modelcheckpoint
# checkpointer = tf.keras.callbacks.ModelCheckpoint('model_for_nuclei.h5', verbose=1, save_best_only=True)

# callbacks = [
#         tf.keras.callbacks.EarlyStopping(patience=2, monitor='val_loss'),
        # tf.keras.callbacks.TensorBoard(log_dir='logs')]

results = model.fit(X_train, Y_train, validation_split=0.1, batch_size=16, epochs=25)

####################################

####################################

idx = random.randint(0, len(X_train))


preds_train = model.predict(X_train[:int(X_train.shape[0]*0.9)], verbose=1)
preds_val = model.predict(X_train[int(X_train.shape[0]*0.9):], verbose=1)
preds_test = model.predict(X_test, verbose=1)

 
preds_train_t = (preds_train > 0.5).astype(np.uint8)
preds_val_t = (preds_val > 0.5).astype(np.uint8)
preds_test_t = (preds_test > 0.5).astype(np.uint8)

# Perform a sanity check on some random training samples
print("Original Training")
ix = random.randint(0, len(preds_train_t))
imshow(X_train[ix])
plt.show()
print("Predicted Training")
imshow(np.squeeze(preds_train_t[ix]))
plt.show()
print("Only Soil Mask")
display_boolean_mask(Y_train[ix])
print("All Terrain Mask")
imshow(np.squeeze(original_Y[ix]))
plt.show()
get_distribution(original_Y[ix])

# Perform a sanity check on some random training samples
print("Original Validation")
ix = random.randint(0, len(preds_val_t))
imshow(X_train[ix])
plt.show()
print("Predicted Validation")
imshow(np.squeeze(preds_val_t[ix]))
plt.show()
print("Only Soil Mask")
display_boolean_mask(Y_train[ix])
print("All Terrain Mask")
imshow(np.squeeze(original_Y[ix]))
plt.show()
get_distribution(original_Y[ix])

# Perform a sanity check on some random testing samples
ix = random.randint(0, len(preds_test_t))
imshow(X_test[ix])
plt.show()
imshow(np.squeeze(preds_test[ix]))
plt.show()