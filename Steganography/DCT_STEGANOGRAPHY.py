from PIL import Image
import os

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


def save_stego_image(image, filename):
    try:
        image.save(filename)
        print(f"Stego image saved as {filename}")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while trying to save the stego image.")



def calculate_DCT(image,txt):
def decode_DCT(image,key):



def main():
    imgPath = str(input("Please enter the path of the image: "))
    img = openImage(imgPath)
    if img:
        print("1: Encode")
        print("2: Decode")
        whoswho = str(input("Please Select a function (1 or 2): "))
        if whoswho == '1':
            txt = str(input("Please enter your text that you want to hide: ") + "D$T")
            encode_name = str(input("Please enter a file name (ex: image.png): "))
            img = calculate_DCT(img,txt)
            if img != 0:
              save_image = save_stego_image(img, encode_name)  # Save the stego image

        elif whoswho == '2':
            decoded_message = decode_DCT(img , "D$T")
            print("Çözülen metin:", decoded_message)
        else:
            print("Please enter a valid message")



if __name__ == "__main__":
    main()
