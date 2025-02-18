import cv2

def extract_message(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Image not found.")
        return
    
    message = []
    height, width, _ = img.shape

    for row in range(height):
        for col in range(width):
            char = chr(img[row, col, 0])  # Extract from Blue channel
            if "".join(message[-3:]) == "###":  # Stop at delimiter
                print("Decrypted message:", "".join(message[:-3]))  # Remove delimiter
                return
            message.append(char)

    print("No hidden message found.")

if __name__ == "__main__":
    img_path = input("Enter encrypted image path: ")
    extract_message(img_path)
