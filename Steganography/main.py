from PIL import Image
import sys
import numpy as np
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
# use C:\Users\Lenovo\Desktop\Default_Ground.png

def openImage(imgPath):
    img = None  # Initialize img as None
    try:
        if os.path.exists(imgPath): #if the image path exists correctly
            img = Image.open(imgPath,"r")
        else:
            print("Error: The specified path is incorrect. The file does not exist.")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while trying to open the image.")

    return img  # Return the img variable


def calculate_LSB(image,txt):

    # Convert text message into binary
    binary_text = ''.join(format(ord(char), '08b') for char in txt)  # binary_text is a string
    print("Binary representation of the text:" ,binary_text)
    # Split binary text into 8-bit segments and store in a list
    binary_list = [binary_text[i:i + 8] for i in range(0, len(binary_text), 8)]
    print("Binary representation of the text as List:", binary_list)


    image = image.convert("RGB")
    width, height = image.size
    array = np.array(list(image.getdata()))
    total_pixels = array.size // 3 #RGB

    lsb_values = []  # Initialize an empty list to store LSB values
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))  # Get the pixel at (x, y)
            lsb = [pixel[c] & 1 for c in range(3)]  # Calculate LSB for each channel (R, G, B)
            lsb_values.append(lsb)
    # Print LSB values (for the first 10 pixels)
    for i, lsb in enumerate(lsb_values[:10]):
        print(f"Pixel {i + 1}: R={lsb[0]}, G={lsb[1]}, B={lsb[2]}")



    if len(binary_text) > total_pixels * 3:
        print("Text too long to be hidden in the image.")
    else:
        binary_index = 0  # Initialize an index for the binary message
        for y in range(height):
            for x in range(width):
                if binary_index < len(binary_text):  # Check if there are more bits to hide
                    pixel = list(image.getpixel((x, y))[:3])  # Get the pixel at (x, y) and extract the RGB channels
                    for c in range(3):  # Loop through R, G, B channels
                        if binary_index < len(binary_text):  # Check if there are more bits to hide
                            pixel[c] = (pixel[c] & 254) | int(binary_text[binary_index])
                            binary_index += 1
                    image.putpixel((x, y), tuple(pixel))  # Update the pixel in the image
                else:
                    break
    return image

def save_stego_image(image, filename):
    try:
        image.save(filename)
        print(f"Stego image saved as {filename}")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while trying to save the stego image.")

def decode_LSB(image, key):
    width, height = image.size
    binary_text = ""
    binary_index = 0
    current_binary = ""

    for y in range(height):
        for x in range(width):
            if binary_index < 8:  # Assuming each character is 8 bits
                pixel = list(image.getpixel((x, y))[:3])
                for color_channel in range(3):
                    current_binary += str(pixel[color_channel] & 1)
                    if len(current_binary) == 8:
                        if current_binary.endswith(key):
                            return binary_text

                        binary_text += current_binary
                        current_binary = ""
                        binary_index += 1
    decoded_message = "".join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8))
    return decoded_message

# C:\Users\DELL\Desktop\Steganography\Steno\Steganography\img.png

def main():
    imgPath = str(input("Please enter the path of the image: "))
    img = openImage(imgPath)
    if img:
        print("1: Encode")
        print("2: Decode")
        whoswho = str(input("Please Select a function (1 or 2): "))
        if whoswho == '1':
            txt = str(input("Please enter your text that you want to hide: ") + "L$B")
            encode_name = str(input("Please enter a file name (ex: image.png): "))
            img = calculate_LSB(img,txt)
            save_image = save_stego_image(img, encode_name)  # Save the stego image

        elif whoswho == '2':
            decoded_message = decode_LSB(img , "L$B")
            print("Çözülen metin:", decoded_message)
        else:
            print("Please enter a valid message")



if __name__ == "__main__":
    main()
