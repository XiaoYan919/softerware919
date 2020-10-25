import requests
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import time
from ctypes import *
import threading

window = tk.Tk()
window.title('小沿汇率查询')
window.geometry('320x568')
window.config(bg="#64BFDA")


# tkinter GUI工具居中展示
def center_window(master, width, height):
    screenwidth = master.winfo_screenwidth()
    screenheight = master.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                            (screenheight - height) / 2)
    master.geometry(size)


# 锁定屏幕
def close_windows():
    user32 = windll.LoadLibrary('user32.dll')
    user32.LockWorkStation()


def notice():
    message = tk.Toplevel(window)
    message.wm_attributes('-topmost', 1)
    center_window(message, 400, 200)
    message.title('锁屏提醒')
    message.config(bg="#64BFDA")
    Label(message, text='定时到了哦！休息一下吧！', justify=CENTER, fg='#18B6ED', font=("黑体", '15')).pack()
    time.sleep(5)
    message.destroy()


class CareForCoders:

    def __init__(self):
        self.countdown_lb = None

    def user_setting(self,root):
        note = LabelFrame(root, text="时间管理", padx=20, pady=20,fg="#1A1717", font=("黑体", '11'))
        note.pack(padx=10, pady=2)
        #输入工作安排
        index = Entry(note,width= 30)
        index.pack()

        lb = LabelFrame(root, text="定时设置(支持小数)", padx=20,pady=20, fg="#1A1717", font=("黑体", '11'))
        lb.pack(padx=10, pady=2)
        self.time_entry = Entry(lb)
        self.time_entry.pack(side='left')
        unit = Label(lb, text="(单位：分)")
        unit.pack(side='right' ,padx=5)

        self.countdown_lb = Label(root,text="休息倒计时:", justify=LEFT,
                                  font=("黑体", '11'))
        self.countdown_lb.pack()
        self.submit = Button(root, text="启动", width=8,
                             command=lambda: self.get_countdown(self.time_entry.get(),root)
                             )
        self.submit.pack(pady=10)

    def get_countdown(self, countdown,root):
        try:
            _float_countdown = float(countdown)
            if _float_countdown <= 0:
                showwarning("提示：", message="倒计时必须为正数！")
            else:
                self.time_entry.config(state=DISABLED)
                self.submit.config(state=DISABLED)
                self.countdown_show(_float_countdown * 60,root)
        except ValueError:
            showwarning("提示：", message="请填写正确的倒计时！")

    def countdown_show(self, countdown_sec,root):
        while countdown_sec:
            countdown_sec -= 1
            time.sleep(1)
            self.countdown_lb.config(text="休息倒计时: %02d:%02d" %
                                          (countdown_sec // 60, countdown_sec % 60))
            root.update()
            # 为了避免突如其来的锁屏，倒计时10秒给出提示...
            if countdown_sec == 10:
                t = threading.Thread(target=notice)
                t.start()
            if countdown_sec < 1:
                # 启动锁屏操作
                close_windows()
                time.sleep(3)
                self.countdown_lb.config(text="欢迎回来...")
                self.time_entry.config(state=NORMAL)
                self.submit.config(state=NORMAL)
                return



#用requests从api接导入数据
def getdata(cointype):
    url = 'http://api.tianapi.com/txapi/fxrate/index'
    var = inputS.get()
    params = {
        'key': 'dd53336d934fbe7de24e68373eb3aa0d',
        'fromcoin': 'CNY',
        'tocoin': cointype,
        'money': var,
    }
    response = requests.get(url=url, params=params).json()
    return response

def gettwd():
    if len(inputS.get())==0:
        entry_var3.set("您还没有输入金额！！")
    else:
        response = getdata('TWD')
        for mou in response["newslist"]:
            truemoney = mou['money']
            entry_var3.set(truemoney)

def getusd():
    if len(inputS.get())== 0:
        entry_var2.set("您还没有输入金额！！")
    else:
        response = getdata('USD')
        for mou in response["newslist"]:
            truemoney = mou['money']
            entry_var2.set(truemoney)

def getjpy():
    if len(inputS.get())==0:
        entry_var4.set("您还没有输入金额！！")
    else:
        response = getdata('JPY')
        for mou in response["newslist"]:
            truemoney = mou['money']
            entry_var4.set(truemoney)

def getkrw():
    if len(inputS.get())==0:
        entry_var5.set("您还没有输入金额！！")
    else:
        response = getdata('KRW')
        for mou in response["newslist"]:
            truemoney = mou['money']
            entry_var5.set(truemoney)

def getgbp():
    if len(inputS.get())==0:
        entry_var6.set("您还没有输入金额！！")
    else:
        response = getdata('GBP')
        for mou in response["newslist"]:
            truemoney = mou['money']
            entry_var6.set(truemoney)

def do_main():
    root = tk.Toplevel(window)
    center_window(root, 300, 350)
    root.resizable(width=False, height=False)
    root.title('时间管理大师')
    root.config(bg="#64BFDA")
    Main = CareForCoders()
    Main.user_setting(root)

    root.mainloop()


ln = tk.Label(window, text='请入人民币金额', bg="#64BFDA", font=('Arial', 12), width=25, height=2)
# ln.grid(row=1,colunm=4)
ln.pack(side='top')
inputS = tk.Entry(window, width=25, bg="#4FD8E8", show=None, font=('Arial', 12))
# inputS.grid(row=1,colunm=5)
inputS.pack(ipady=5)
b3 = tk.Button(window, text="新台币", width=15, height=1, bg="#64BFDA", command=gettwd).pack(pady=5)  # 按钮
entry_var3 = tk.StringVar()
t3 = tk.Entry(window, width=20, textvariable=entry_var3, bg="#64BFDA", font=('Arial', 12), show=None).pack(fill='x')

b2 = tk.Button(window, text="美元", width=15, height=1, bg="#64BFDA", command=getusd).pack(pady=5)  # 按钮
entry_var2 = tk.StringVar()
t2 = tk.Entry(window, width=20, textvariable=entry_var2, bg="#64BFDA", font=('Arial', 12), show=None).pack(pady=5,
                                                                                                           fill='x')

b4 = tk.Button(window, text="日元", width=15, height=1, bg="#64BFDA", command=getjpy).pack(pady=5)  # 按钮
entry_var4 = tk.StringVar()
t4 = tk.Entry(window, width=20, textvariable=entry_var4, bg="#64BFDA", font=('Arial', 12), show=None).pack(pady=5,
                                                                                                           fill='x')

b5 = tk.Button(window, text="韩元", width=15, height=1, bg="#64BFDA", command=getkrw).pack(pady=5)  # 按钮
entry_var5 = tk.StringVar()
t5 = tk.Entry(window, width=20, textvariable=entry_var5, bg="#64BFDA", font=('Arial', 12), show=None).pack(pady=5,
                                                                                                           fill='x')

b6 = tk.Button(window, text="英镑", width=15, height=1, bg="#64BFDA", command=getgbp).pack(pady=5)  # 按钮
entry_var6 = tk.StringVar()
t6 = tk.Entry(window, width=20, textvariable=entry_var6, bg="#64BFDA", font=('Arial', 12), show=None).pack(pady=5,
                                                                                                           fill='x')
b7 = tk.Button(window, text="时间管理", width=15, height=1, bg="#64BFDA", command=do_main).pack(pady=5)

window.mainloop()