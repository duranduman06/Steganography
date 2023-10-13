from PIL import Image
import sys
"""
A. Lsb Based Steganography

Algorithm to embed text message:-
    Step 1: Read the cover image and text message which is to be hidden in the cover image.
    Step 2: Convert text message in binary.
    Step 3: Calculate LSB of each pixels of cover image.
    Step 4: Replace LSB of cover image with each bit of secret message one by one.
    Step 5: Write stego image

Algorithm to retrieve text message:-
    Step 1: Read the stego image.
    Step 2: Calculate LSB of each pixels of stego image.
    Step 3: Retrieve bits and convert each 8 bit into character.
"""
from PIL import Image
import os
# use C:\Users\DELL\Desktop\opencv\photos\z.jpg


def openImage(imgPath):
    img = None  # Initialize img as None
    try:
        if os.path.exists(imgPath): #if the image path exists correctly
            img = Image.open(imgPath)
        else:
            print("Error: The specified path is incorrect. The file does not exist.")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while trying to open the image.")

    return img  # Return the img variable

def textHide():
    txt = str(input("Please enter your text that you want to hide: "))

    # Convert text message into binary
    binary_text = ''.join(format(ord(char), '08b') for char in txt) #binary_text is a string

    # Split binary text into 8-bit segments and store in a list
    binary_list = [binary_text[i:i + 8] for i in range(0, len(binary_text), 8)]
    print("Binary representation of the text:", binary_list)

    return txt # Return the txt variable

def main():
    imgPath = str(input("Please enter the path of the image: "))
    img = openImage(imgPath)
    if img:
        textHidden = textHide()
        print(textHidden)



if __name__ == "__main__":
    main()
