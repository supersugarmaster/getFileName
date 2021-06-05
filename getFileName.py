# -*- coding: UTF-8 -*-
"""
@author:wb.wengchengshuo2017
@file:getFileName.py
@time:2021/06/06
"""

import tkinter as tk
from tkinter import filedialog
import os
import re

def showFileName():
    '''打开选择文件夹对话框'''
    root = tk.Tk()
    root.withdraw()
    print('请选择目标文件夹')
    folderPath = filedialog.askdirectory() #获得选择好的文件夹
    # Filepath = filedialog.askopenfilename() #获得选择好的文件
    print('请选择保存路径')
    saveFile = filedialog.asksaveasfilename(initialfile='文件名.txt')
    file = open(saveFile, 'w',encoding='utf-8')
    pattern = re.compile('.+(?=\.)')

    #当前路径下所有非目录子文件
    for root, dirs, files in os.walk(folderPath):
        file.write(root+':\n')
        for f in files:
            f = pattern.match(f)
            file.write(f.group()+'\n')
        file.write('\n')

    file.close()

if __name__=='__main__':
    showFileName()