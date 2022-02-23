# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Matthew Hamilton and Jasjot Parnar
# Date: November 21, 2020
# Description: Contains all functions that perform imagine manipulation.

# import helper functions 
import cmpt120imageProj as cmpt
import numpy

# ---BASIC---
# VERTICAL FLIP
def flip_vert(img):
    height = len(img[0])
    width = len(img)
    for x in range(width):
        for y in range(height//2):
          copy = img[x][y]
          img[x][y] = img[x][height-y-1]
          img[x][height-y-1] = copy
    return img

# HORIZONTAL FLIP
def flip_horiz(img):
 height = len(img[0])
 width = len(img)
 for y in range(height):
        for x in range(width//2):
          copy = img[x][y]
          img[x][y] = img[width-x-1][y]
          img[width-x-1][y] = copy
 return img

# inverts colors.
def invert(img):
  for x in range(len(img)):
    for y in range(len(img[0])):
      pixel = img[x][y]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      invR = 255 - r
      invG = 255 - g
      invB = 255 - b
      img[x][y] = [invR, invG, invB]
  return img

# ---INTERMEDIATE---

# remove red colour channel
def red(img):
  for x in range(len(img)):
    for y in range(len(img[0])):
      pixel = img[x][y]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      r = 0
      img[x][y] = [r, g, b]
  return img

# remove green colour channel
def green(img):
  for x in range(len(img)):
    for y in range(len(img[0])):
      pixel = img[x][y]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      g = 0 
      img[x][y] = [r, g, b]
  return img

# remove blue colour channel
def blue(img):
  for x in range(len(img)):
    for y in range(len(img[0])):
      pixel = img[x][y]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      b = 0
      img[x][y] = [r, g, b]
  return img

# change the image to greyscale
def greyscale(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            total = r+g+b
            av = total/3
            greyR = av
            greyG = av
            greyB = av
            img[x][y] = [greyR, greyG, greyB]
    return img

# change the colour to sepia filter 
def serpia(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel = img[x][y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            sepiaR = (r * .393) + (g *.769) + (b * .189)
            if sepiaR>255:
              sepiaR = 255
            sepiaG = (r * .349) + (g *.686) + (b * .168)
            if sepiaG>255:
              sepiaG = 255
            sepiaB = (r * .272) + (g *.534) + (b * .131)
            if sepiaB>255:
              sepiaB = 255
            img[x][y] = [sepiaR, sepiaG, sepiaB]
    return img

# decrease the image brightness (by 10) 
def decrease_light(img):
      for x in range(len(img)):
          for y in range(len(img[0])):
            pixel = img[x][y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            newR = r-10
            if newR<0:
              newR=0
            newG = g-10
            if newG<0:
              newG=0
            newB = b-10
            if newB<0:
              newB=0
            img[x][y] = [newR, newG, newB]
      return img

# increase the brightness (by 10)
def increase_light(img):
      for x in range(len(img)):
          for y in range(len(img[0])):
            pixel = img[x][y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            newR = r+10
            if newR>255:
              newR=255
            newG = g+10
            if newG>255:
              newG=255
            newB = b+10
            if newB>255:
              newB=255
            img[x][y] = [newR, newG, newB]
      return img

#---ADVANCED---

# Rotate the image left 
def rotate_left(img):
    width = len(img)
    height = len(img[0])
    rotateL = cmpt.createBlackImage(height,width)
    for x in range(width):
        for y in range(height):
            rotateL[y][width-x-1] = img[x][y]
    return rotateL 

# Rotate the image right 
def rotate_right(img):
    width = len(img)
    height = len(img[0])
    rotateR = cmpt.createBlackImage(height,width)
    for x in range(width):
        for y in range(height):
            rotateR[height-y-1][x] = img[x][y]
    return rotateR

# Pixelates the image 
def pixelate(img):
  red = 0
  blue = 0
  green = 0

  height = len(img[0])
  height = height - height%4
  width = len(img)
  width = width - width%4

  for y in range(0, height, 4):
    for x in range(0, width, 4):
      for a in range(4):
        for b in range(4):
          red = img[x+a][y+b][0]
          blue = img[x+a][y+b][1]
          green = img[x+a][y+b][2]
      for a in range(4):
         for b in range(4):
              img[x+a][y+b][0] = red
              img[x+a][y+b][1] = blue
              img[x+a][y+b][2] = green

      red = 0
      blue = 0
      green = 0

  return img

# Binarize the image 
def binarize(img):
  width = len(img)
  height = len(img[0])
  size = width*height

  redVal = 0
  threshold = 0

  img = greyscale(img)
  
  #Calculate initial threshold value
  for x in range(len(img)):
    for y in range(len(img[0])):
      redVal += img[x][y][0]

  threshold = int(redVal/(size))

  #Initialize and run while loop
  run = True

  while run:
    backgroundImageTotal = 0
    forgroundImageTotal = 0
    newThreshTotal = 0
    
    for x in range(len(img)):
     for y in range(len(img[0])):
      if img[x][y][0] < threshold:
          backgroundImageTotal += img[x][y][0]
      else:
          forgroundImageTotal += img[x][y][0]
    
    backgroundImageTotal = int(backgroundImageTotal/(size))
    forgroundImageTotal = int(forgroundImageTotal/(size)
      )
    newThreshTotal = int((backgroundImageTotal+forgroundImageTotal)/2)
    
    if newThreshTotal < 10:
      run = False
    else:
      threshold = newThreshTotal
    
    for x in range(width):
      for y in range(height):
        if img[x][y][0] >= newThreshTotal:
          img[x][y] = 255,255,255          
        else:
          img[x][y] = 0,0,0
          
    return img
    
