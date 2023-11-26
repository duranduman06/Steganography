from PIL import Image
import os
import numpy as np


def openImage(imgPath):
    img = None
    try:
        if os.path.exists(imgPath):
            img = Image.open(imgPath, "r")
        else:
            print("Error: The specified path is incorrect. The file does not exist.")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while trying to open the image.")
    return img


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
    key_txt = ''.join(format(ord(char), '08b') for char in key)

    for y in range(height):
        for x in range(width):
                pixel = list(image.getpixel((x, y))[:3])
                for c in range(3):                          # Do this for every color channel R,G,B
                    current_binary += str(pixel[c] & 1)     # Extracts the lsb value of the each color channel in a pixel and adds it into the current binary string.
                    if len(current_binary) == 8:            # Check for every 8 bits (like for every char).
                        binary_text += current_binary
                        if binary_text.endswith(key_txt):   # Check if the binary text ends with the key part.
                            decoded_message = "".join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text),8))  # Convert the binary format to char format.
                            decoded_message = decoded_message.replace(key,"")  # Remove the key from the decoded message.
                            return decoded_message
                        current_binary = ""
                        binary_index += 1

    decoded_message = "".join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8)) # Convert the binary format to char format.
    decoded_message = decoded_message.replace(key, "")  # Remove the key from the decoded message.
    return decoded_message


def calculate_LSB(image, binary_text):


    image = image.convert("RGB")
    width, height = image.size
    array = np.array(list(image.getdata()))
    total_pixels = array.size // 3
    total_bits = total_pixels * 3
    max_characters = total_bits // 8

    if len(binary_text) > total_bits:
        print("Warning: Text may not be fully hidden in the image. It exceeds the image capacity.")

    binary_index = 0
    for y in range(height):
        for x in range(width):
            if binary_index < len(binary_text):
                pixel = list(image.getpixel((x, y))[:3])
                for c in range(3):
                    if binary_index < len(binary_text):
                        pixel[c] = (pixel[c] & 254) | int(binary_text[binary_index])
                        binary_index += 1
                image.putpixel((x, y), tuple(pixel))
            else:
                break
    #print(binary_text) # asıl text
    #print(binary_text[:binary_index]) #ilk fotoğraf için yazılacak kısım
    #print(binary_text[binary_index:]) #textin kalan kısmı

    return image, binary_index < len(binary_text),binary_index  # Return the updated image and a flag indicating if there is remaining text




def encode_text(img, remaining_text, counter):
    img, has_remaining_text,binary_index = calculate_LSB(img, remaining_text)
    print(has_remaining_text,binary_index)
    filename = f"{counter}.png"
    save_stego_image(img, filename)
    return img, remaining_text[binary_index:] if has_remaining_text else ""

def main():
    imgPath = str(input("Please enter the path of the image: "))
    img = openImage(imgPath)

    if img:
        print("1: Encode")
        print("2: Decode")
        whoswho = str(input("Please Select a function (1 or 2): "))

        if whoswho == '1':
            txt = str(input("Please enter your text that you want to hide: ") + "L$B")
            encode_name = "1.png"
            binary_text = ''.join(format(ord(char), '08b') for char in txt)

            counter = 1  # Counter for naming multiple images
            while binary_text:  # Continue encoding until all text is encrypted
                img, binary_text = encode_text(img, binary_text, counter)
                counter += 1

                if binary_text:  # If there is remaining text, ask for another image
                    img_path = str(input("Please enter the path of the next image: "))
                    img = openImage(img_path)

        elif whoswho== '2':
            decoded_message = decode_LSB(img, "L$B")
            print("Çözülen metin:", decoded_message)

        else:
            print("Please enter a valid message")

if __name__ == "__main__":
    main()
