from tkinter import *
import webview

def search() :
    url = str(ent_0.get())
    web = 'https://www.google.com/search?q='+url

    browser = Tk() 
    browser.geometry("800x450") 
    webview.create_window('TAKING Browser', web) 
    webview.start()

def url() :
    url = str(ent_1.get())
    web = 'https://'+url

    browser = Tk() 
    browser.geometry("800x450") 
    webview.create_window('TAKING Browser', web) 
    webview.start()

root = Tk()
root.title('TAKING Search')
root.geometry('800x450')
root.resizable(width=False, height=False)

Label(root, text='URL://', fg='blue').pack()
ent_1 = Entry(root, width=130)
ent_1.pack()
btn_3 = Button(root, text='go to url', fg='white', bg='green', command=url)
btn_3.pack()

Label(root).pack()
Label(root, text='TAKING', fg='red', font=('Helvetica Neue', 50)).pack()
Label(root, text='Search', fg='green', font=('Helvetica Neue', 20)).pack()

ent_0 = Entry(root, width=50, fg='black', font=('Helvetica Neue', 15))
ent_0.pack()

btn_0 = Button(root, text='Search', fg='white', bg='black', command=search)
btn_0.pack()

Label(root).pack()
btn_1 = Button(root, text='+ Add shorcut', fg='white', bg='green')
btn_1.pack()

for i in range(3) :
    Label(root).pack()

btn_2 = Button(root, text='Service and support', fg='white', bg='black')
btn_2.pack()
Label(root, text='Open source browser under TAKING license').pack()
Label(root, text='Developer rights reserved', fg='red').pack()

root.mainloop()