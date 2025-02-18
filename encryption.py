import cv2
import numpy as np
import os

def embed_message(img_path, message, output_path="encryptedImage.png"):
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Image not found.")
        return

    height, width, _ = img.shape
    max_chars = height * width  # Maximum characters that can be stored
    if len(message) > max_chars:
        print(f"Message too long! Max characters allowed: {max_chars}")
        return
    
    message += "###"  # Adding a delimiter to indicate the end of the message
    index = 0

    for row in range(height):
        for col in range(width):
            if index < len(message):
                img[row, col, 0] = ord(message[index])  # Storing in the Blue channel
                index += 1
            else:
                break

    cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save as lossless PNG
    os.system(f"start {output_path}")  # Opens the image
    print("Message embedded successfully!")

if __name__ == "__main__":
    img_path = input("Enter image path: ")
    msg = input("Enter secret message: ")
    embed_message(img_path, msg)
