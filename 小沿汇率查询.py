
import requests
import tkinter as tk


window = tk.Tk()
window.title('小沿汇率查询')
window.geometry('320x568')
window.config(bg="#64BFDA")


ln = tk.Label(window,text='请入人民币金额',bg="#64BFDA", font=('Arial', 12), width=25, height=2)
#ln.grid(row=1,colunm=4)
ln.pack(side='top')
inputS = tk.Entry(window,width=25 ,bg="#4FD8E8", show=None,font=('Arial', 12))
#inputS.grid(row=1,colunm=5)
inputS.pack(ipady=5)

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


b3 = tk.Button(window,text="新台币",width=15,height=1,bg="#64BFDA",command=gettwd).pack(pady=5) #按钮
entry_var3 = tk.StringVar()
t3 = tk.Entry(window,width=20,textvariable=entry_var3,bg="#64BFDA", font=('Arial', 12),show=None).pack(fill='x')

b2 = tk.Button(window,text="美元",width=15,height=1,bg="#64BFDA",command=getusd).pack(pady=5) #按钮
entry_var2 = tk.StringVar()
t2 = tk.Entry(window,width=20, textvariable=entry_var2,bg="#64BFDA",font=('Arial', 12),show=None).pack(pady=5,fill='x')

b4 = tk.Button(window,text="日元",width=15,height=1,bg="#64BFDA",command=getjpy).pack(pady=5) #按钮
entry_var4 = tk.StringVar()
t4 = tk.Entry(window,width=20, textvariable=entry_var4,bg="#64BFDA",font=('Arial', 12),show=None).pack(pady=5,fill='x')

b5 = tk.Button(window,text="韩元",width=15,height=1,bg="#64BFDA",command=getkrw).pack(pady=5) #按钮
entry_var5 = tk.StringVar()
t5 = tk.Entry(window,width=20, textvariable=entry_var5,bg="#64BFDA",font=('Arial', 12),show=None).pack(pady=5,fill='x')

b6 = tk.Button(window,text="英镑",width=15,height=1,bg="#64BFDA",command=getgbp).pack(pady=5)  #按钮
entry_var6 = tk.StringVar()
t6 = tk.Entry(window,width=20, textvariable=entry_var6,bg="#64BFDA",font=('Arial', 12),show=None).pack(pady=5,fill='x')



window.mainloop()