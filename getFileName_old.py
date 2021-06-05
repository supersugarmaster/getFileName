#-*- coding = utf-8 -*-
#@Time : 2021/5/22 12:53
#@Author : Robert Weng
#@File : getFileName.py
#@Software : PyCharm

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

    def getFileName(folder):
        filenames = os.listdir(folder)

        for i,filename in enumerate(filenames):
            match = pattern.match(filename)

            if match == None:               #遇到文件夹就递归
                print('已读取目录：'+folder+'/'+filename)
                file.write('\n文件夹名：%s\n'%filename)
                getFileName(folder+'/'+filename)
            else:
                file.write(match.group()+'\n')
                if i == len(filenames)-1:
                    file.write('\n')
                print('文件名：'+filename)

    getFileName(folderPath)
    file.close()
    # pattern = re.compile('.+(?=\.)')
    # filename = 'GitWorkSpace'
    # if pattern.match(filename) == None:
    #     print('OK')
if __name__ == '__main__':
    while 1:
        try:
            showFileName()
            break
        except NotADirectoryError as e:
            print('此文件缺少后缀名，请修改后重新选择目标文件夹：'+e.filename)
            i = input('修改完毕后请按任意键继续，或按e退出程序：')
            if i == 'e' or i == 'E':
                break
            else:
                continue
