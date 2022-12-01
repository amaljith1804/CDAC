import pyqrcode as qr
from tkinter import *
from tkinter.filedialog import *


root = Tk()
root.geometry("500x500")
root.title("QR Code Generator")
root.iconbitmap("\\Users\\amal\\Desktop\\Documents\\CDAC\\CLASS\\Module 3\\QRCode.ico")

#global variable
linkOrText = StringVar()
def code_generator():
    string1 = linkOrText.get()
    url = qr.create(string1)
    path_save = asksaveasfilename()
    url.png(path_save+'QRCode.png')
def main():
    label0 = Label(root,text = "Enter link or text",width=20,font=("arial",10,"bold"))
    label0.pack()
    entry0 = Entry(root,textvar = linkOrText)
    entry0.pack()
    button0 = Button(root, text = "Generate QR Code", command=code_generator)
    button0.pack()
    button1 = Button(root,text = "Exit", command=root.quit)
    button1.pack()
if __name__ == "__main__":
    main()
    root.mainloop()
