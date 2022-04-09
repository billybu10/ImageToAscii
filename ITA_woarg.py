#!/usr/bin/python

from PIL import Image, ImageOps

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

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
    inputFile = input("Enter input file: ")
    outputFile = input("Enter output file: ")
    finalWidth = int(input("Enter output file width: "), 10)
    finalHeight = int(input("Enter output file height: "), 10)
    asciiImage = fun_char(fun_greysc(fun_size(fun_readFile(inputFile), finalWidth, finalHeight)), finalWidth)
    print(asciiImage)
    fun_write(asciiImage, outputFile)

    
    
main()