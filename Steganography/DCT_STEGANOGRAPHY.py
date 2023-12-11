from PIL import Image
import numpy as np


def my_dct(block):
    N = block.shape[0]
    result = np.zeros_like(block, dtype=float)

    for u in range(N):
        cu = 1.0 / np.sqrt(2) if u == 0 else 1.0
        for v in range(N):
            cv = 1.0 / np.sqrt(2) if v == 0 else 1.0
            sum_val = 0.0

            for i in range(N):
                for j in range(N):
                    sum_val += block[i, j] * np.cos((2 * i + 1) * u * np.pi / (2 * N)) * np.cos(
                        (2 * j + 1) * v * np.pi / (2 * N))

            result[u, v] = cu * cv * sum_val / np.sqrt(N)

    return result


def my_idct(block):
    N = block.shape[0]
    result = np.zeros_like(block, dtype=float)

    for i in range(N):
        for j in range(N):
            sum_val = 0.0

            for u in range(N):
                for v in range(N):
                    cu = 1.0 / np.sqrt(2) if u == 0 else 1.0
                    cv = 1.0 / np.sqrt(2) if v == 0 else 1.0
                    sum_val += cu * cv * block[u, v] * np.cos((2 * i + 1) * u * np.pi / (2 * N)) * np.cos(
                        (2 * j + 1) * v * np.pi / (2 * N))

            result[i, j] = sum_val / np.sqrt(N)

    return result


def dct_encode(image_path, message):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img = img.convert('L')

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Embed the message in 8x8 blocks using the DCT
    message_index = 0
    for i in range(0, img_array.shape[0], 8):
        for j in range(0, img_array.shape[1], 8):
            block = img_array[i:i + 8, j:j + 8]
            block_dct = np.round(my_dct(block))

            # Embed the message in the DC coefficient of each block
            if message_index < len(message):
                block_dct[0, 0] = int(block_dct[0, 0]) & 0b11111110  # Clear the LSB
                block_dct[0, 0] = int(block_dct[0, 0]) | (
                    int(ord(message[message_index]) & 1))  # Set the LSB with the message bit

                message_index += 1

            img_array[i:i + 8, j:j + 8] = np.round(my_idct(block_dct))

    # Convert the NumPy array back to an image
    encoded_img = Image.fromarray(img_array.astype('uint8'))

    # Save the encoded image
    encoded_img.save('encoded_image.png')
    print("Image encoded and saved as encoded_image.png")


def dct_decode(encoded_image_path, message_length):
    # Open the encoded image
    encoded_img = Image.open(encoded_image_path)

    # Convert the image to a NumPy array
    encoded_array = np.array(encoded_img)

    # Extract the message from the DC coefficient of each 8x8 block
    message = ''
    for i in range(0, encoded_array.shape[0], 8):
        for j in range(0, encoded_array.shape[1], 8):
            block = encoded_array[i:i + 8, j:j + 8]
            dc_coefficient = block[0, 0]
            message += str(int(dc_coefficient) & 1)

    # Convert binary message to characters
    decoded_message = ''.join([chr(int(message[i:i + 8], 2)) for i in range(0, len(message), 8)])

    return decoded_message


# Save the message in the image
image_path = input("Enter the path of the image: ")
message_to_hide = input("Enter the message to hide: ")
dct_encode(image_path, message_to_hide)

# Decode the message from the encoded image
encoded_image_path = 'encoded_image.png'
decoded_message = dct_decode(encoded_image_path, len(message_to_hide))
print("Decoded Message:", decoded_message)
