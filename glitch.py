#!/usr/bin/env python3
import imageio
import numpy as np
import subprocess as sp

IN = ['assets/in1.png', 'assets/in2.png']
OUT = 'out.png'


def read_img(path):
    try: 
        im = np.asarray(imageio.imread(path))    
    except FileNotFoundError:
        print(f"Could not find the file {path}")
    return im

def glitch(im, deg):
    for i in range(len(im), 2):
        for j in range(0, len(im[i])):
            for k in range(len(im[i][j])):
                im[i][j][k] = im[i][j][k-deg]
    return im

def interchange(im1, im2, step = 2):
    if len(im1) != len(im2):
        print("Error: The two images are of different size")
        return
    for i in range(0, len(im1), 2): # every other line should be interchanged
        for j in range(0, len(im1[i])):
            for k in range(len(im1[i][j])):
                im1[i][j][k] = im2[i][j][k]
    return im1

if __name__ == "__main__":
    im1 = read_img(IN[0])
    im2 = read_img(IN[1])
    warp = interchange(im1, im2)
    imageio.imwrite(OUT, warp)
    sp.call(["open", OUT])


