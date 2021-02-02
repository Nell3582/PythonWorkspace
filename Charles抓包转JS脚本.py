import jsonpath
import json
import pyperclip
import tkinter as tk
from tkinter import filedialog
from pathlib import path
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

# file_path = filedialog.askopenfilename() #获取单个文件
file_paths = filedialog.askopenfilenames() #获取多个文件,并返回一个路径元祖,通过遍历可得到所选文件的绝对路径
for Fpath in file_paths:
    with open(Fpath, 'r') as fobj:
        f = fobj.readlines()
        print(f)



