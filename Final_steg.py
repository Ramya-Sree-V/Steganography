from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Steganography - Hide a Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2c041d")

def text_to_binary(text):
    # Convert each character to its binary representation
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text

def binary_to_text(binary):
    # Convert binary data to text by splitting into 8-bit chunks
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)

def encode_image(input_image_path, output_image_path, message):
    image = Image.open(input_image_path)
    encoded_image = image.copy()
    width, height = image.size

    binary_message = text_to_binary(message) + '1111111111111110'  # End delimiter
    data_index = 0
    message_length = len(binary_message)

    for y in range(height):
        for x in range(width):
            if data_index < message_length:
                pixel = list(image.getpixel((x, y)))

                for n in range(3):  # RGB channels
                    if data_index < message_length:
                        pixel[n] = pixel[n] & ~1 | int(binary_message[data_index])
                        data_index += 1

                encoded_image.putpixel((x, y), tuple(pixel))

    encoded_image.save(output_image_path)
    print(f"Message encoded and saved to {output_image_path}")

def decode_image(image_path):
    image = Image.open(image_path)
    width, height = image.size

    binary_message = ""
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):  # RGB channels
                binary_message += str(pixel[n] & 1)

    delimiter = '1111111111111110'
    message_end = binary_message.find(delimiter)
    if message_end != -1:
        binary_message = binary_message[:message_end]

    message = binary_to_text(binary_message)
    print("Decoded message:", message)
    return message

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetype=(("PNG File", "*.png"),
                                                    ("JPG File", "*.jpg"),
                                                    ("All Files", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img, width=250, height=250)
    lb1.image = img

def Hide():
    global secret
    message = text1.get(1.0, END)
    output_image_path = "hidden.png"
    encode_image(filename, output_image_path, message)

def Show():
    decoded_message = decode_image(filename)
    text1.delete(1.0, END)
    text1.insert(END, decoded_message)

def save():
    pass  # Save functionality is handled in the Hide function

# ICON
image_icon = PhotoImage(file="fairy.jpg")
root.iconphoto(False, image_icon)

# LOGO
logo = PhotoImage(file="circle.png")
Label(root, image=logo, bg="#2c041d").place(x=10, y=0)

Label(root, text="CYBER SCIENCE", bg="#2c041d", fg="white", font="arial 25 bold").place(x=100, y=20)

# FIRST FRAME
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lb1 = Label(f, bg="black")
lb1.place(x=40, y=10)

# SECOND FRAME
frame2 = Frame(root, bd=3, width=340, height=280, bg="#c8a2c9", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="#c8a2c9", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# THIRD FRAME
frame3 = Frame(root, bd=3, bg="#601a3e", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#601a3e", fg="white").place(x=20, y=5)

# FOURTH FRAME
frame4 = Frame(root, bd=3, bg="#601a3e", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#601a3e", fg="white").place(x=20, y=5)

root.mainloop()
