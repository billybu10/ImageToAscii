#!/usr/bin/python

import string
from typing import final
from PIL import Image, ImageOps
import argparse

parser = argparse.ArgumentParser()

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def fun_agumens():
    parser.add_argument("inputFile", help="input file")
    parser.add_argument("outputFile", help="output file")
    parser.add_argument("finalWidth", type=int, help="width of final ascii art")
    parser.add_argument("finalHeight", type=int, help="height of final ascii art")
    args = parser.parse_args()
    global inputFile
    inputFile = args.inputFile
    global outputFile
    outputFile = args.outputFile
    global finalWidth
    finalWidth = args.finalWidth
    global finalHeight
    finalHeight = args.finalHeight

def fun_readFile(inputFile):
    try:
        wsad = Image.open(inputFile)
    except:
        print("This path is invalid")
    return wsad

def fun_size(wsad, finalWidth, finalHeight):
    size = wsad.resize((finalWidth, finalHeight))
    return size

def fun_greysc(size):
    greysc = ImageOps.grayscale(size)
    return greysc

def fun_char(greysc, finalWidth):
    pixels = greysc.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    pixelCount = len(characters)  
    asciiImage = "\n".join([characters[index:(index+finalWidth)] for index in range(0, pixelCount, finalWidth)])
    return asciiImage

def fun_write(asciiImage, outputFile):
    with open(outputFile, "w") as f:
        f.write(asciiImage)

def main():
    fun_agumens()
    asciiImage = fun_char(fun_greysc(fun_size(fun_readFile(inputFile), finalWidth, finalHeight)), finalWidth)
    print(asciiImage)
    fun_write(asciiImage, outputFile)

main()