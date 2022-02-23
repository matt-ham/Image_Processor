# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Matthew Hamilton and Jasjot Parmar
# Date: November 20, 2020
# Description: Image Processor that displays an image and manipulates that image depending on user input. 

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.display.init()
pygame.font.init()

# list of system options
system = ["Q: Quit", 
            "O: Open", 
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
          "1: Invert",
          "2: Flip Horizontal",
          "3: Flip Vertical",
          "4: Switch to Intermeidate Functions",
          "5: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [  
                  "1: Remove Red Channel",
                  "2: Remove Green Channel",
                  "3: Remove Blue Channel",
                  "4: Convert to Greyscale",
                  "5: Apply Serpia Filter",
                  "6: Decrease Brightness",
                  "7: Increase Brightness",
                  "8: Switch to Basic Functions",
                  "9: Switch to Advanced Functions"
              
                 ]

# list of advanced operation options
advanced = [  
              "1: Rotate Left",
              "2: Rotate Right",
              "3: Pixelate",
              "4: Binarize",
              "5: Switch to Basic Functions",
              "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):

    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q,O,S,R or 1-5) ")
        

    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice (Q,O,S,R or 1-9) ")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q,O,S,R or 1-6) ")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)


def handleUserInput(state, img):
  


  """
      Input:  state - a dictionary containing the state values of the application
              img - the 2d array of RGB values to be operated on
      Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
  """
  userInput = state["lastUserInput"].upper()
    
  #handle the system functionalities
  if userInput.isalpha(): # check if the input is an alphabet
      print("Log: Doing system functionalities " + userInput)
      if userInput == "q": # this case actually won't happen, it's here as an example
          print("Log: Quitting...")
      # ***add the rest to handle other system functionalities***
      elif userInput == "O":
        print("Log: Opening picture")
        tkinter.Tk().withdraw()
        openFilename = tkinter.filedialog.askopenfilename()
        img = cmpt120imageProj.getImage(openFilename)
        
        appStateValues["lastOpenFilename"] = openFilename
        cmpt120imageProj.showInterface(img, "Original Image",generateMenu(appStateValues))

      # if user input is S, save the image 
      elif userInput == "S":
        print("log: Saving current image")
        tkinter.Tk().withdraw()
        saveFilename = tkinter.filedialog.asksaveasfilename()
        appStateValues["lastSaveFilename"] = saveFilename
        cmpt120imageProj.saveImage(img, "newimage.jpg")
        cmpt120imageProj.showInterface(img, "Saved photo",generateMenu(appStateValues))
        
      # if user input = R, reload the image 
      elif userInput == "R":
        print("Log: Reload Original Image")
        orig = cmpt120imageProj.getImage(appStateValues["lastOpenFilename"])
        cmpt120imageProj.showInterface(orig, "orig", generateMenu(appStateValues))
        img = orig
            
  # or handle the manipulation functionalities based on which mode the application is in
  elif userInput.isdigit(): # has to be a digit for manipulation options
    print("Log: Doing manipulation functionalities " + userInput)
      # ***add the rest to handle other manipulation functionalities***

    # if the mode is basic, show basic menu
    if appStateValues["mode"] == "basic":
        print("basic")

        # if user input is 1, invert the image
        if userInput == "1":
            tkinter.Tk().withdraw()
            print("Inverting")
            img = cmpt120imageManip.invert(img)
            cmpt120imageProj.showInterface(img, "InvertedImage", generateMenu(appStateValues))

        # if user input is 2, flip the image horizontally 
        elif userInput == "2":
            print("Log: Flip Horiztonal")
            img = cmpt120imageManip.flip_horiz(img)
            cmpt120imageProj.showInterface(img, "Horiztonal Flip", generateMenu(appStateValues))
      
        # if user input is 3, flip the image vertically 
        elif userInput == "3":
            print("Log: Vertical Flip")
            img = cmpt120imageManip.flip_vert(img)
            cmpt120imageProj.showInterface(img, "Vertical Flip", generateMenu(appStateValues))

        # if user input is 4, show intermediate functions 
        elif userInput == "4":
            tkinter.Tk().withdraw()
            appStateValues["mode"] = "intermediate"
            cmpt120imageProj.showInterface(img, "Current Image", generateMenu(appStateValues))
      
        # if user input is 5, show advanced functions
        elif userInput == "5":
            tkinter.Tk().withdraw()
            appStateValues["mode"] = "advanced"
            cmpt120imageProj.showInterface(img, "Current Image", generateMenu(appStateValues))
        

        
    # if the mode is intermediate, show intermediate menu  
    elif appStateValues["mode"] == "intermediate":  
      
      # if user input is 1, remove red channel
      if userInput == "1":
        tkinter.Tk().withdraw()
        print("Log: Remove Red Channel")
        img = cmpt120imageManip.red(img)
        cmpt120imageProj.showInterface(img, "Red Removed", generateMenu(appStateValues))

      # if user input is 2, remove green channel   
      elif userInput == "2":
        print("Log: Remove Green Channel")
        img = cmpt120imageManip.green(img)
        cmpt120imageProj.showInterface(img, "Green Removed", generateMenu(appStateValues))

      # if user input is 3, remove blue channel
      elif userInput == "3":
        print("Log: Remove Blue Channel")
        img = cmpt120imageManip.blue(img)
        cmpt120imageProj.showInterface(img, "Blue Removed",generateMenu(appStateValues))

      # if user input is 4, convert image to greyscale
      elif userInput == "4":
        print("Log: Convert to Greyscale")
        img = cmpt120imageManip.greyscale(img)
        cmpt120imageProj.showInterface(img, "Greyscale",generateMenu(appStateValues))
    
      # if user input is 5, convert image to serpia filter 
      elif userInput == "5":
        print("Log: Applying Serpia Filter")
        img = cmpt120imageManip.serpia(img)
        cmpt120imageProj.showInterface(img, "Serpia", generateMenu(appStateValues))

      # if user input is 6, decrease image brightness  
      elif userInput == "6":
        print("Log Decrease Brightness")
        img = cmpt120imageManip.decrease_light(img)
        cmpt120imageProj.showInterface(img, "Light Decrease", generateMenu(appStateValues))

      # if user input is 6, increase image brightness  
      elif userInput == "7":
        print("Log Increase Brightness")
        img = cmpt120imageManip.increase_light(img)
        cmpt120imageProj.showInterface(img, "light increase",generateMenu(appStateValues))
    
      # if user input is 8, go back to basic mode 
      elif userInput == "8":
        tkinter.Tk().withdraw()
        appStateValues["mode"] = "basic"
        cmpt120imageProj.showInterface(img, "Basic Menu", generateMenu(appStateValues))

      # if user input is 9, go back to advanced mode 
      elif userInput == "9":
        tkinter.Tk().withdraw()
        appStateValues["mode"] = "advanced"
        cmpt120imageProj.showInterface(img, "Current Img", generateMenu(appStateValues))
    
    # if mode is advanced, show the advanced menu
    elif appStateValues["mode"] == "advanced":
      
      # if user input is 1, rotate the image left 
      if userInput == "1":
        tkinter.Tk().withdraw()
        img = cmpt120imageManip.rotate_left(img)
        cmpt120imageProj.showInterface(img, "rotated right", generateMenu(appStateValues))

      # if the user input is 2, rotate the image right 
      elif userInput == "2":
        img = cmpt120imageManip.rotate_right(img)
        cmpt120imageProj.showInterface(img, "rotated right image", generateMenu(appStateValues))

      # if the user input is 3, pixelate the image 
      elif userInput == "3":
        print("Log: Pixelating Image")
        img = cmpt120imageManip.pixelate(img)
        cmpt120imageProj.showInterface(img, "pixelate", generateMenu(appStateValues))

      # if user input is 4, binarize the image 
      elif userInput == "4":
        cmpt120imageManip.binarize(img)
        cmpt120imageProj.showInterface(img, "binarize image", generateMenu(appStateValues))
        
      # if user input is 5, go back to basic mode 
      elif userInput == "5":
        tkinter.Tk().withdraw()
        appStateValues["mode"] = "basic"
        cmpt120imageProj.showInterface(img, "Basic Menu", generateMenu(appStateValues))
      
      # if user input is 6, go back to intermediate mode 
      elif userInput == "6":
        tkinter.Tk().withdraw()
        appStateValues["mode"] = "intermediate"
        cmpt120imageProj.showInterface(img, "Intermediate Menu", generateMenu(appStateValues))

  # if the user prints an unrecognized value, ask the user for input again
  else:
    print("Log: Unrecognized user input: " + userInput)
    
  
  return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": "",
                  }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

keepRunning = True

while keepRunning:

    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")