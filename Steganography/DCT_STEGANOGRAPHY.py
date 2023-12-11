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
    
    
    DCT steganography is a technique of hiding data in an image by modifying the discrete cosine transform (DCT) coefficients of the image. The encoder and decoder algorithms are as follows:

- Encoder: 
    - Input: A cover image, a secret message, and a key.
    - Output: A stego image with the secret message embedded in it.
    - Steps:
        1. Convert the cover image from RGB to YCbCr color space.
        2. Divide the Y component (luminance) of the image into 8x8 blocks.
        3. Apply DCT to each block and obtain the DCT coefficients matrix.
        4. Quantize the DCT coefficients using a predefined quantization table.
        5. Convert the secret message into a binary stream using the key.
        6. Embed the binary stream into the quantized DCT coefficients by replacing the least significant bits (LSBs) of some selected coefficients with the bits of the message. The selection of coefficients can be done using a pseudorandom number generator (PRNG) with the key as the seed.
        7. Perform inverse quantization and inverse DCT on the modified coefficients to obtain the stego blocks.
        8. Combine the stego blocks and convert the image back to RGB color space.

- Decoder:
    - Input: A stego image, a key, and the length of the secret message.
    - Output: The secret message extracted from the stego image.
    - Steps:
        1. Convert the stego image from RGB to YCbCr color space.
        2. Divide the Y component (luminance) of the image into 8x8 blocks.
        3. Apply DCT to each block and obtain the DCT coefficients matrix.
        4. Quantize the DCT coefficients using the same quantization table as in the encoder.
        5. Extract the LSBs of some selected coefficients using the same PRNG with the key as in the encoder.
        6. Concatenate the extracted bits to form a binary stream.
        7. Convert the binary stream into a text message using the key.
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



def encode_DCT(cover_image,txt):

# STEP 2: Read secret message and convert it in binary.
    # Converts text message into binary
    binary_text = ''.join(format(ord(char), '08b') for char in txt)  # binary_text is a string
    print("Binary representation of the text:", binary_text)
    # Splits binary text into 8-bit segments and stores in a list
    binary_list = [binary_text[i:i + 8] for i in range(0, len(binary_text), 8)]
    print("Binary representation of the text as List:", binary_list)


# STEP-3: The cover image is broken into 8×8 block of pixels.
    # Break the cover image into 8x8 blocks of pixels0
    block_size = 8
    height, width = cover_image.shape
    blocks = []
    # Now, 'blocks' contains 8x8 pixel blocks of the cover image.
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = cover_image[y:y + block_size, x:x + block_size]
            blocks.append(block)

# STEP 4: Subtract 128 from each block of pixels
    for i in range(len(blocks)):
        blocks[i] = np.subtract(blocks[i], 128)

# Step 5: Apply DCT to each block
    dct_blocks = []
    for block in blocks:
        # Apply DCT to the block and keep it as an 8x8 matrix
        dct_block = cv2.dct(np.float32(block))
        # Ensure that the DCT block is 8x8, if not pad it with zeros
        if dct_block.shape != (8, 8):
            dct_block = np.pad(dct_block, ((0, 8 - dct_block.shape[0]), (0, 8 - dct_block.shape[1])), mode='constant')
        dct_blocks.append(dct_block)


# STEP 6: Compress each block through quantization table
    quantization_table = np.array(
        [[16, 11, 10, 16, 24, 40, 51, 61],
         [12, 12, 14, 19, 26, 58, 60, 55],
         [14, 13, 16, 24, 40, 57, 69, 56],
         [14, 17, 22, 29, 51, 87, 80, 62],
         [18, 22, 37, 56, 68, 109, 103, 77],
         [24, 35, 55, 64, 81, 104, 113, 92],
         [49, 64, 78, 87, 103, 121, 120, 101],
         [72, 92, 95, 98, 112, 100, 103, 99]]
    )

    compressed_blocks = []
    for dct_block in dct_blocks:
        compressed_block = np.round(dct_block / quantization_table)
        compressed_blocks.append(compressed_block)


    # Step 7: Calculate LSB of each DC coefficient and replace with each bit of the secret message
    secret_message_index = 0  # Initialize an index to keep track of the secret message bits

    for compressed_block in compressed_blocks:
        # Access the DC coefficient (top-left) of the 8x8 block
        dc_coefficient = compressed_block[0, 0]

        # Extract the secret message bit
        if secret_message_index < len(binary_list):
            # Get the next bit from the secret message
            bit_to_hide = int(binary_list[secret_message_index])

            # Convert dc_coefficient to an integer and replace the LSB with the bit to hide
            dc_coefficient = int(dc_coefficient)
            dc_coefficient = (dc_coefficient & 254) | bit_to_hide

            # Update the DC coefficient in the compressed block
            compressed_block[0, 0] = dc_coefficient

            # Move to the next bit in the secret message
            secret_message_index += 1
        else:
            # If we have used all bits of the secret message, break the loop
            break

    """ burdan sonrası sıkıntılı"""
    stego_image = np.zeros_like(cover_image)
    stego_index = 0

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            stego_block = compressed_blocks[stego_index]
            stego_block = np.multiply(stego_block, quantization_table)
            stego_block = cv2.idct(np.float32(stego_block))
            stego_block = np.add(stego_block, 128)

            stego_height, stego_width = stego_block.shape
            end_y, end_x = y + stego_height, x + stego_width

            if end_y <= height and end_x <= width:
                stego_image[y:end_y, x:end_x] = stego_block
            else:
                # Crop the stego block if it doesn't fit exactly
                cropped_stego_block = stego_block[:min(stego_height, height - y), :min(stego_width, width - x)]
                stego_image[y:end_y, x:end_x] = cropped_stego_block

            stego_index += 1

    return stego_image  # Return the stego image as a NumPy array

# use C:\Users\DELL\Desktop\opencv\photos\z.jpg


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
            encode_name = str(input("Please enter a file name (ex: image.png): "))
            img = encode_DCT(img,txt)
            save_stego_image(img, encode_name)  # Save the stego image

       # elif whoswho == '2':
            #decoded_message = decode_DCT(img , "D$T")
            #print("Çözülen metin:", decoded_message)
        else:
            print("Please enter a valid message")



if __name__ == "__main__":
    main()
