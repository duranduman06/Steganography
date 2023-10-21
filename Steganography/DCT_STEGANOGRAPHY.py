from PIL import Image
import os
import cv2
import numpy as np
"""
B. DCT Based Steganography  Algorithm to embed text message:- 
    Step 1: Read cover image. 
    Step 2: Read secret message and convert it in binary. 
    Step 3: The cover image is broken into 8×8 block of pixels. 
    Step 4: Working from left to right,  top  to bottom subtract 128 in each block of pixels. 
    Step 5: DCT is applied to each block. 
    Step 6: Each  block  is  compressed  through  quantization table. 
    Step 7: Calculate LSB of each DC coefficient  and replace with each bit of secret message. 
    Step 8: Write stego image. 

Algorithm to retrieve text message:- 
    Step 1: Read stego image. 
    Step 2: Stego image is broken into 8×8 block of pixels. 
    Step 3: Working from left to right,  top  to bottom subtract 128 in each block of pixels. 
    Step 4: DCT is applied to each block. 
    Step 5: Each  block  is  compressed  through  quantization table. 
    Step 6: Calculate LSB of each DC coefficient. 
    Step 7: Retrieve and convert each 8 bit into character.
"""

def openImage(imgPath):
    cover_image = None  # Initialize img as None
    try:
        if os.path.exists(imgPath): #if the image path exists correctly
            cover_image = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        else:
            print("Error: The specified path is incorrect. The file does not exist.")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while trying to open the image.")

    return cover_image  # Return the img variable


def save_stego_image(image, filename):
    try:
        image.save(filename)
        print(f"Stego image saved as {filename}")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while trying to save the stego image.")



def calculate_DCT(cover_image,txt):
    # Converts text message into binary
    binary_text = ''.join(format(ord(char), '08b') for char in txt)  # binary_text is a string
    print("Binary representation of the text:", binary_text)
    # Splits binary text into 8-bit segments and stores in a list
    binary_list = [binary_text[i:i + 8] for i in range(0, len(binary_text), 8)]
    print("Binary representation of the text as List:", binary_list)


# STEP-3 The cover image is broken into 8×8 block of pixels.
    # Break the cover image into 8x8 blocks of pixels
    block_size = 8
    height, width = cover_image.shape
    blocks = []
    # Now, 'blocks' contains 8x8 pixel blocks of the cover image.
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = cover_image[y:y + block_size, x:x + block_size]
            blocks.append(block)
    print(blocks)




#def decode_DCT(image,key):

def main():
    imgPath = str(input("Please enter the path of the image: "))
    img = openImage(imgPath)
    if img is None:
        print("Failed to open the image.")
    else:
        print("1: Encode")
        print("2: Decode")
        whoswho = str(input("Please Select a function (1 or 2): "))
        if whoswho == '1':
            txt = str(input("Please enter your text that you want to hide: ") + "D$T")
            #encode_name = str(input("Please enter a file name (ex: image.png): "))
            img = calculate_DCT(img,txt)
            #save_image = save_stego_image(img, encode_name)  # Save the stego image

        elif whoswho == '2':
            decoded_message = decode_DCT(img , "D$T")
            print("Çözülen metin:", decoded_message)
        else:
            print("Please enter a valid message")



if __name__ == "__main__":
    main()
