
# Importing the required packages
from PIL import Image
import cv2
from collections import Counter
import numpy as np
import os
import argparse

# Reading the target image, resizing it and flattening the pixel values into a 1D array
def Reading_test(img):
    img = Image.open(img)
    width, height = img.size
    Size.append(width//10)
    Size.append(height//10)
    img = img.resize((width//10, height//10))
    img_arr = np.asarray(img)
    return img_arr.flatten()

# Reading the directory images
def Reading(img):
    img = Image.open(img)
    newsize = (Size[0], Size[1])
    img = img.resize(newsize)
    img_arr = np.array(img).astype('float64')
    return img_arr.flatten()

# Generating a histogram for the pixel values of the image and storing them
def Count_Histogram(img):
    RH = Counter(img)
    H = []
    for i in range(256):
        if i in RH.keys():
            H.append(RH[i])
        else:
            H.append(0)
    return H

# Measuring the Euclidean Distance between the images
def Euclidean_Distance(img, test_img):
    d = 0
    for i in range(len(img)):
        d += np.square(img[i]-test_img[i])
    return np.sqrt(d)

# Generating a dissimilarity score of the images being compared
def Score_generator(s_img, t_img_hist):
    s_img = Reading(s_img)
    s_img_hist = Count_Histogram(s_img)
    E_dist = Euclidean_Distance(s_img_hist, t_img_hist)
    return E_dist

if __name__ == '__main__':

    # Building a command line argument
    parser = argparse.ArgumentParser(description = 'To check a given folder and return the image most similar to the given target image')

    # Collecting the filename to the folder and the target image
    parser.add_argument('img_file', type = str, help = 'The url of the folder containing the images that are being checked')
    parser.add_argument('img', type = str, help = 'The url of the target image being used to check')

    # Optional parameter to restrict the search in the given folder to only one type of files
    parser.add_argument(
        "--filetype",
        type=str,
        default=None,
        help="Only files with the specified type will be checked (e.g. .jpg, .png, etc,.)"
    )
    args = parser.parse_args()

    # to be replaced string and file extension filter
    img_folder = args.img_file
    img = args.img
    type_filter = args.filetype
    print('\n')
    print(f"Comparing the image {img} with images in the folder \"{img_folder}\"\n")

    # Running across the given folder and adding the filename of the images into an array
    dir_content = os.listdir(img_folder)
    path_dir_content = [os.path.join(img_folder, doc) for doc in dir_content]
    imgs = [doc for doc in path_dir_content if os.path.isfile(doc)]

    Scores = []
    Size = []
    t_img = Reading_test(img)
    t_img_hist = Count_Histogram(t_img)

    # Generating the scores, by checking images and then storing them into an array
    for i in range(len(dir_content)):
        Scores.append(Score_generator(imgs[i], t_img_hist))

    # Selecting the most similar element based on the least dissimilarity score
    Similar_img = imgs[Scores.index(min(Scores))]
    scale_percent = 50
    t_img = cv2.imread(img)

    # Resizing the target image and the most similar image for displaying on the screen
    width, height = round(t_img.shape[1] * scale_percent / 100), round(t_img.shape[0] * scale_percent / 100)
    t_img = cv2.resize(t_img, (width, height), interpolation = cv2.INTER_AREA)
    cv2.imshow('The test image', t_img)
    Image = cv2.imread(Similar_img)
    width, height = round(Image.shape[1] * scale_percent / 100), round(Image.shape[0]* scale_percent / 100)
    Image = cv2.resize(Image, (width, height), interpolation = cv2.INTER_AREA)
    cv2.imshow('Most Similar image', Image)
    cv2.waitKey()