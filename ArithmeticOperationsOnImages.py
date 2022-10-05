'''
type the following commands on cmd
to install tkinter => pip install tk
to install opencv => pip install opencv-python

opencv is used to re-size the images and do the arithmetic operations on images
tkinter is used to create the GUI
'''


from tkinter import *
from tkinter import filedialog
import cv2 as cv
from PIL import Image, ImageTk

root = Tk()

# title of the window
root.title('Arithmetic operations on Images')

'''
arithmetic operations cannot be done on different sized images.
Hence, the selected images had to be re-sized and stored in a specific path (path_1, path_2)
[re-sized_a.png] is the file name and can be changed. .png and .jpg types are checked and have no idea
about other types of images and .jpg and .png images can be operated on. matching file types is 
not a must
'''

# path_1, path_2 are the absolute paths of the two images
# no need to hard code this. just specify the folder that re-sized images should be stored
path_1 = 'D:/Images/re-sized_a.png'
path_2 = 'D:/Images/re-sized_b.png'

# size of the image is hard coded to have 200x200 size and can be changed
width = 200
height = 200

# these are the paths to store image outputs. can be changed.
# names should be different or will be overwritten
pathToStoreAddition = 'D:/Images/Addition.png'
pathToStoreSubtraction = 'D:/Images/Subtraction.png'
pathToStoreMultiplication = 'D:/Images/Multiplication.png'
pathToStoreDivision = 'D:/Images/Division.png'

'''
selectImg functions will open a file dialog box to choose files.
any image file can be chosen and they will be re-sized to 200x200 and stored in path_# using opencv
and then tkinter will take the same path to open the files and load it to the GUI
'''


def selectImg1(path, rw, cl):

    # images should be stored in different global variables, otherwise won't show up in the window.
    # don't know the exact reason.
    global img1
    root.filename = filedialog.askopenfilename(initialdir='D:/Images', title="Open an image file",
                                               filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"),
                                                          ("all files", "*.*")))

    # this ensures that if the user cancels the file dialog without choosing a file, nothing happens
    if root.filename:
        src = cv.imread(root.filename, cv.IMREAD_UNCHANGED)

        dsize = (width, height)

        output = cv.resize(src, dsize)

        cv.imwrite(path, output)

        img1 = ImageTk.PhotoImage(Image.open(path))

        Label(root, image=img1, text=path).grid(row=rw, column=cl)


def selectImg2(path, rw, cl):
    global img2
    root.filename = filedialog.askopenfilename(initialdir='D:/Images', title="Open an image file",
                                               filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"),
                                                          ("all files", "*.*")))

    if root.filename:
        src = cv.imread(root.filename, cv.IMREAD_UNCHANGED)

        dsize = (width, height)

        output = cv.resize(src, dsize)

        cv.imwrite(path, output)

        img2 = ImageTk.PhotoImage(Image.open(path))

        Label(root, image=img2, text=path).grid(row=rw, column=cl)


'''
operation functions will take the paths to the previously stored re-sized images as parameters.
path_to_store is used to store the output. rw and cl are used to load the image outputs to the 
grid system of the window
'''


def add(path1, path2, path_to_store, rw, cl):
    global img_addition
    img_1 = cv.imread(path1)
    img_2 = cv.imread(path2)
    output = img_1 + img_2
    cv.imwrite(path_to_store, output)
    img_addition = ImageTk.PhotoImage(Image.open(path_to_store))

    Label(root, image=img_addition, text=path_to_store).grid(row=rw, column=cl)


def sub(path1, path2, path_to_store, rw, cl):
    global img_subtraction
    img_1 = cv.imread(path1)
    img_2 = cv.imread(path2)
    output = img_1 - img_2
    cv.imwrite(path_to_store, output)
    img_subtraction = ImageTk.PhotoImage(Image.open(path_to_store))

    Label(root, image=img_subtraction, text=path_to_store).grid(row=rw, column=cl)


def mul(path1, path2, path_to_store, rw, cl):
    global img_multiplication
    img_1 = cv.imread(path1)
    img_2 = cv.imread(path2)
    output = img_1 * img_2
    cv.imwrite(path_to_store, output)
    img_multiplication = ImageTk.PhotoImage(Image.open(path_to_store))

    Label(root, image=img_multiplication, text=path_to_store).grid(row=rw, column=cl)


def div(path1, path2, path_to_store, rw, cl):
    global img_division
    img_1 = cv.imread(path1)
    img_2 = cv.imread(path2)
    output = img_1 // img_2
    cv.imwrite(path_to_store, output)
    img_division = ImageTk.PhotoImage(Image.open(path_to_store))

    Label(root, image=img_division, text=path_to_store).grid(row=rw, column=cl)


# creating buttons
# lambda function is given to the command as a parameter because that function has to have
# parameters of its own.
# command is called when the button is clicked
selectImgBtn1 = Button(root, text='Select Image a', command=lambda: selectImg1(path_1, 1, 0))
selectImgBtn2 = Button(root, text='Select Image b', command=lambda: selectImg2(path_2, 1, 2))

# creating the operation buttons
addBtn = Button(text='Add', command=lambda: add(path_1, path_2, pathToStoreAddition, 3, 0))
subBtn = Button(text='Subtract', command=lambda: sub(path_1, path_2, pathToStoreSubtraction, 3, 1))
mulBtn = Button(text='Multiply', command=lambda: mul(path_1, path_2, pathToStoreSubtraction, 3, 2))
divBtn = Button(text='Divide', command=lambda: div(path_1, path_2, pathToStoreSubtraction, 3, 3))

# adding the buttons to a window as a grid
selectImgBtn1.grid(row=0, column=0, columnspan=2)
selectImgBtn2.grid(row=0, column=2, columnspan=2)

addBtn.grid(row=2, column=0)
subBtn.grid(row=2, column=1)
mulBtn.grid(row=2, column=2)
divBtn.grid(row=2, column=3)

# tkinter runs an infinite loop to continuously check for new events happening in the window
root.mainloop()
