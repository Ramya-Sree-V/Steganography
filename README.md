# Steganography - Hide Text in Image

## Overview
This project is a simple steganography application that allows users to hide a text message within an image file. The application provides a graphical user interface (GUI) using Tkinter, where users can load an image, encode a message into it, and decode a hidden message from an image.

## Features
- **Text to Binary Conversion**: Converts text messages into binary format for encoding.
- **Image Encoding**: Embeds the binary message into the least significant bits of the image pixels.
- **Image Decoding**: Extracts the binary message from the image pixels and converts it back to text.
- **GUI**: Provides an easy-to-use interface for loading images, encoding messages, and decoding messages.


## Technologies Used
- Python
- Tkinter (for GUI)
- PIL (Pillow) for image processing

## Installation

- Clone the repository:
     ```bash
     https://github.com/Ramya-Sree-V/Steganography.git
     ```
- Install the required libraries:
  ```bash
  pip install pillow
  ```

## Usage
1. Run the application:
   ```bash
   python Final_steg.py
   ```
   
2. Use the GUI to interact with the application:
   - **Open Image**: Load an image file to encode a message.
   - **Hide Data**: Encode a text message into the loaded image.
   - **Show Data**: Decode and display the hidden message from the loaded image.
   - **Save Image**: Save the encoded image.

## How It Works
1. **Encoding**
   - The encode_image function takes an input image, a message, and an output image path.
   - The message is converted to binary, and each bit of the message is embedded into the least significant bit of the image pixels.
   - An end delimiter ('1111111111111110') is added to mark the end of the message.

2. **Decoding**
   - The decode_image function reads the binary data from the image pixels.
   - It looks for the end delimiter and converts the binary data back to text.
  
## GUI Description
- **Main Window**: The main application window with a title "Steganography - Hide a Text Message in an Image".
- **First Frame**: Displays the loaded image.
- **Second Frame**: Text box for entering and displaying messages.
- **Third Frame**: Buttons for opening an image and saving the encoded image.
- **Fourth Frame**: Buttons for hiding and showing the hidden data.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Inspired by various online resources and tutorials on steganography and Tkinter.
- Thanks to the open-source community for providing the tools and libraries used in this project.

## Contact 
For any questions or feedback, please feel free to contact me at ramyasreev135@gmail.com.







