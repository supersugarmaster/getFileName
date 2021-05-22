#-*- coding = utf-8 -*-
#@Time : 2021/5/22 12:53
#@Author : Robert Weng
#@File : getFileName.py
#@Software : PyCharm

import tkinter as tk
from tkinter import filedialog
import os
import re

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

folderPath = filedialog.askdirectory() #获得选择好的文件夹
# Filepath = filedialog.askopenfilename() #获得选择好的文件
filenames = os.listdir(folderPath)
saveFile = filedialog.asksaveasfilename(initialfile='文件名.txt')
file = open(saveFile,'w')
pattern = re.compile('.+(?=\.)')

for filename in filenames:
    file.write(pattern.match(filename).group()+'\n')

file.close()