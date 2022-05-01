import tkinter as tk
from tkinter import ttk
import ctypes
import requests

def prelogin(user_entry, username, passwd_entry, passwd):
    user_entry.get()
    str_user = username.get()
    passwd_entry.get()
    str_pass = passwd.get()
    login(str_user, str_pass)

def login(user, passwd):
    url = "https://its4.pku.edu.cn/cas/ITSClient"
    payload = {
        # 填写账号和密码
        'username': user,
        'password': passwd,
        'iprange': 'free',
        'cmd': 'open'
    }
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    result = requests.post(url, params=payload, headers=headers)
    login_status(int(result.text.split(sep='"')[1] == "succ"))

def login_status(stat):
    global info
    global textLine
    if stat == True:
        info.set("已连接")
    elif stat == False:
        info.set("用户名或密码错误")
    else:
        info.set("请检查你的网络环境")


window = tk.Tk()
window.title("网关")
window.geometry("226x200")

# hidpi settings for windows
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
window.tk.call('tk', 'scaling', ScaleFactor/75)

info = tk.StringVar()
info.set("请输入用户名和密码")
textLine = ttk.Label(textvariable= info)
textLine.pack()

username = tk.StringVar()
user_entry = ttk.Entry(textvariable=username)
user_entry.pack()

passwd = tk.StringVar()
passwd_entry = ttk.Entry(textvariable=passwd)
passwd_entry.pack()

login_button = ttk.Button(text="连接", command= lambda:prelogin(user_entry, username, passwd_entry, passwd))
login_button.pack()
window.mainloop()