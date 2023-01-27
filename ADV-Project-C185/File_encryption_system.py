from tkinter import *
from tkinter import filedialog as fd
import hashlib
import os

root=Tk()
root.geometry("250x190")
root.title("Apply MD5 or SHA256")
root.configure(bg="sky blue")

def apply_md5():
    print("MD5 function")
    text_file = fd.askopenfilename(title="Open a text document", filetypes=(("Text files", "*.txt"),))
    print(text_file)
    with open(text_file, "r") as f:
        read_ok = f.read()
        file_results = hashlib.md5(read_ok.encode())
        file_hexa = file_results.hexdigest()
        print(file_hexa)
        md5_file = open("md5.txt", "w")
        md5_file.write(file_hexa)
    """
    name = os.path.basename(text_file)
    read_mode = open(name, "r")
    read_ok = text_file.read()
    file_results = hashlib.md5(read_ok.encode())
    file_hexa = file_results.hexdigest()
    print(file_hexa)
    md5_file = open("md5.txt", "w")
    md5_file.write(file_hexa)
    text_file.close()
    md5_file.close()
    """
    
def apply_sha256():
    print("SHA function")   
    text_file = fd.askopenfilename(title="Open a text document", filetypes=(("Text files", "*.txt"),))
    print(text_file)
    with open(text_file, "r") as f:
        read_ok = f.read()
        file_results = hashlib.sha256(read_ok.encode())
        file_hexa = file_results.hexdigest()
        print(file_hexa)
        sha256_file = open("sha256.txt", "w")
        sha256_file.write(file_hexa)
    
    
btn=Button(root, text="Apply MD5",command=apply_md5, fg="white", bg="light green", bd=0)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256, fg="white", bg="light green", bd=0)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()
