from customtkinter import *
import webview

root = CTk()
root.title('TAKING Browser')
root.geometry('800x450')
root.resizable(width=False, height=False)

ent_0 = CTkEntry(master=root, placeholder_text="Search URL://", width=700)
ent_0.place(x=15, y=10)

btn_0 = CTkButton(master=root, text="Go to URL", width=50, fg_color="green")
def url():
    url = str(ent_0.get())
    web = 'https://'+url

    browser = CTk() 
    browser.geometry("800x450") 
    webview.create_window('TAKING Browser', web) 
    webview.start()

btn_0.configure(command=url)
btn_0.place(x=720, y=10)

lbl_0 = CTkLabel(master=root, text="TAKING", font=('Helvetica Neue', 80))
lbl_0.place(x=260, y=80)
lbl_1 = CTkLabel(master=root, text="Browser", font=('Helvetica Neue', 20))
lbl_1.place(x=550, y=90)

ent_1 = CTkEntry(master=root, placeholder_text="Search....", width=500, height=40, corner_radius=20)
ent_1.place(x=150, y=170)
btn_1 = CTkButton(master=root, text="Go", width=50)
def find():
    url = str(ent_1.get())
    web = 'https://www.google.com/search?q='+url

    browser = CTk() 
    browser.geometry("800x450") 
    webview.create_window('TAKING Browser', web) 
    webview.start()

btn_1.configure(command=find)
btn_1.place(x=660, y=175)

btn_2 = CTkButton(master=root, text="Add Shortcut +", width=50, fg_color='black')
btn_2.place(x=370, y=220)

btn_3 = CTkButton(master=root, text="Service and support", width=50, fg_color='red')
btn_3.place(x=360, y=340)

lbl_2 = CTkLabel(master=root, text="Open source browser under TAKING license", font=('Helvetica Neue', 13))
lbl_2.place(x=300, y=370)
lbl_3 = CTkLabel(master=root, text="Developer rights reserved", font=('Helvetica Neue', 13))
lbl_3.place(x=350, y=390)
lbl_4 = CTkLabel(master=root, text="New Version!", font=('Helvetica Neue', 13))
lbl_4.place(x=680, y=410)

root.mainloop()