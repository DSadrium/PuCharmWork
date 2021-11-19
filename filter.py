import numpy as np
from PIL import Image


def get_img(path):
    """
    Reduce the picture to the type of nparray
    :param path: the path to the picture as a string
    :return: nparry of pixels
    >>> img_to_nparr("test/firsttest.jpg")
    array([[[255, 62, 105]]], dtype=uint8)
    """
    img = Image.open(path)
    return np.array(img)


def save_img(img, name):
    """
    Save an image from nparray to image file
    :param img: nparray to save
    :param name: filename
    """
    res = Image.fromarray(img)
    res.save(name)


def get_pixel_art(img, size, grayscale):
    """
    Creating pixel art np.array with size - called size
    :param img: image in type np.array
    :param size: pixel size
    :param grayscale: grayscale in image
    :return: black and white pixel in type np.array
    >>> get_pixel_art(get_img('Tests/secondtest.jpg'), 10, 10)
    array([[[110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110]],
    <BLANKLINE>
           [[110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110]],
    <BLANKLINE>
           [[110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110]],
    <BLANKLINE>
           [[110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110]],
    <BLANKLINE>
           [[110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110]],
    <BLANKLINE>
           [[110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110],
            [110, 110, 110]]], dtype=uint8)
    """
    width = len(img)
    height = len(img[1])

    for x in range(0, width, size):
        for y in range(0, height, size):
            brightness = get_brightness(img, size, x, y)
            img[x: x + size, y: y + size] = brightness - brightness % grayscale
    return img


def get_brightness(img, size, x, y):
    """
    Getting the average bright of pixels
    :param img: image in type np.array
    :param size: radius point for average bright
    :param x: x pixel's coordinate
    :param y: y pixel's coordinate
    :return: average bright in type int
    """
    return np.average(img[x: x + size, y: y + size])


#img = get_img(input("Write the picture's path - "))
#size = int(input("Write pixel's size - "))
#grayscale = int(input("Write grayscale's count - "))
#save_img(get_pixel_art(img, size, grayscale), 'res.jpg')
