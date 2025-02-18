Image Steganography using Python
This project demonstrates image-based steganography, in which a secret message is embedded in an image by altering the pixel values implemented by Python and OpenCV. Then, we use a decryption script to extract the hidden message later.

📌 Features

✅ Store a secret message within any image with no visible changes

✅ Redeem hidden data from a encrypt image

✅ Lossless PNG Format Handles Data Corruption

✅ Python-Powered Easy and Light-Weighted Implementation

🛠 Technologies Used

Python – Primary programming language

OpenCV – For image processing (modifying the pixel values)

NumPy – Arrays for fast pixel processing
📂 Project Structure
📁 Image-Stegano
│── 📜 encrypt.py       # Script to hide a message in an image
│── 📜 decrypt.py       # Script to extract the hidden message
│── 📜 README.md        # Project documentation
│── 📂 images           # Folder to store input/output images
│   ├── input.png       # Original image (before encryption)
│   ├── encrypted.png   # Image containing the hidden message

🚀 Installation & Setup
Step 1: Clone the Repository
git clone https://github.com/yourusername/Image-Stegano.git
cd Image-Stegano
Step 2: Install Dependencies
Ensure you have Python installed, then install the required libraries:
pip install opencv-python numpy
🔐 How to Encrypt (Hide a Message)
Run the encryption script:
python encrypt.py
Enter the path of the image where the message should be hidden.
Type the secret message to hide.
The modified image (encryptedImage.png) will be generated with the message embedded.
🔓 How to Decrypt (Extract the Message)
Run the decryption script:
python decrypt.py
Enter the path of the encrypted image.
The hidden message will be extracted and displayed.
📌 Example Usage
Encryption Example
$ python encrypt.py
Enter image path: input.png
Enter secret message: Hello, this is a hidden message!
Message embedded successfully!
✅ The output image encryptedImage.png now contains the secret message.

Decryption Example
$ python decrypt.py
Enter encrypted image path: encryptedImage.png
Decrypted message: Hello, this is a hidden message!
✅ The original message is successfully retrieved.

🔮 Future Enhancements
🔹 Add encryption (AES) for better security
🔹 GUI-based interface using Tkinter or PyQt
🔹 Support for different image formats (BMP, TIFF, etc.)
🔹 Optimize storage using LSB (Least Significant Bit) encoding

