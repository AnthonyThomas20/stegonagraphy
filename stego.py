
import tkinter as tk #GUI
root = tk.Tk()
from PIL import Image
from tkinter import simpledialog

def genData(data):
    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd
def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                if (pix[j] % 2 != 0):
                    pix[j] -= 1

            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                pix[j] -= 1
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                pix[-1] -= 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
def encode():
    img = encode_popup()
    image = Image.open(img, 'r')

    data_input= data_popup()
    if (len(data_input) == 0):
        raise ValueError('Data is empty')


    newimg = image.copy()
    encode_enc(newimg, data_input)

    new_img_name = new_image_popup()
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
def decode():
    img = decode_popup()
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data
def encode_popup():
    image_name=simpledialog.askstring("Encode Details","Enter the image name with extension")
    return image_name
def data_popup():
    data=simpledialog.askstring("Text Input","Enter the text to be encoded")
    return data
def new_image_popup():
    new_image=simpledialog.askstring("Encode Details","Enter the new image name with extension")
    return new_image
def decode_popup():
    decode_image=simpledialog.askstring("Decode Details","enter to image name to be decoded with extension")
    return decode_image
def output():
    w['text']="Decoded Word Is-\n" +decode()

b=tk.Label(root,text=":: Welcome to Steganography ::\n",bg="#d0ae9b",fg="yellow")
close=tk.Button(root,text="Exit",width=8,bg="yellow",fg="#d0ae9b",command=root.destroy)
encoding=tk.Button(root,text="ENCODE",width=8,bg="yellow",fg="#d0ae9b",command=encode)
decoding=tk.Button(root,text="DECODE",width=8,bg="yellow",fg="#d0ae9b",command=output)
w=tk.Label(root, text="\nPress Decode To Decode image\n",bg="#d0ae9b",fg="yellow")
w1=tk.Label(root, text="\nPress Encode To Encode image\n",bg="#d0ae9b",fg="yellow")
head=tk.Label(root,text="\nSTEGANOGRAPHY BY GROUP NO. 11\n",bg="#d0ae9b",fg="yellow")
b.pack(padx=10)
head.pack(padx=10)
encoding.pack()
w1.pack(padx=10)
decoding.pack()
w.pack(padx=10)
close.pack()
root.title("IMAGE STEGANOGRAPHY")
root.configure(background="#d0ae9b")
root.geometry("400x400")
root.mainloop()


