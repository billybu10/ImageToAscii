#!/usr/bin/python

from PIL import Image, ImageOps

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def main():
    inputFile = input("Enter input file: ")
    outputFile = input("Enter output file: ")
    finalWidth = input("Enter output file width: ")
    finalHeight = input("Enter output file height: ")
    try:
        wsad = Image.open(inputFile)
    except:
        print("This path is invalid")
    size = wsad.resize((finalWidth, finalHeight))
    greysc = ImageOps.grayscale(size)
    pixels = greysc.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    pixel_count = len(characters)  
    ascii_image = "\n".join([characters[index:(index+finalWidth)] for index in range(0, pixel_count, finalWidth)])
    print(ascii_image)
    with open(outputFile, "w") as f:
        f.write(ascii_image)
    
main()