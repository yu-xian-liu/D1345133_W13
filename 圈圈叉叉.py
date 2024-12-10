from tkinter import*
from tkinter import messagebox
username_box={'NMSL123':'123123','YRSB121':'456456','BBBB11':'789789'}
def login():
    user_name = str(username_lab.get())
    key = str(password.get())
    if user_name in username_box:
        if username_box[user_name] == key:
            messagebox.showinfo("登入成功","歡迎")
            Tic_Tac_Toe()
            root.destroy()
        else:
            messagebox.showerror("登入失敗","密碼錯誤")
    else:
        messagebox.showerror("登入失敗","查無此帳號")
player = 0
def Tic_Tac_Toe():
    def btn_click(btn):
        global player
        if btn['text'] == '':
            if player:
                btn['text'] = 'X'
                player = 0
            else:
                btn['text'] = 'O'
                player = 1
            btn['state'] = DISABLED
            check_win()
    def check_win():
        if  btn00['text'] == btn01['text'] == btn02['text'] and btn00['text'] != '':
            print(btn00['text'], 'win')
            messagebox.showinfo("Game Over", btn00['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif  btn03['text'] == btn04['text'] == btn05['text'] and btn03['text'] != '':
            print(btn03['text'], 'win')
            messagebox.showinfo("Game Over", btn03['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif  btn00['text'] == btn03['text'] == btn06['text'] and btn00['text'] != '':
            print(btn00['text'], 'win')
            messagebox.showinfo("Game Over", btn00['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif  btn06['text'] == btn07['text'] == btn08['text'] and btn06['text'] != '':
            print(btn06['text'], 'win')
            messagebox.showinfo("Game Over", btn06['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif  btn01['text'] == btn04['text'] == btn07['text'] and btn01['text'] != '':
            print(btn01['text'], 'win')
            messagebox.showinfo("Game Over", btn01['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif  btn02['text'] == btn05['text'] == btn08['text'] and btn02['text'] != '':
            print(btn02['text'], 'win')
            messagebox.showinfo("Game Over", btn02['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif  btn00['text'] == btn04['text'] == btn08['text'] and btn00['text'] != '':
            print(btn00['text'], 'win')
            messagebox.showinfo("Game Over", btn00['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif  btn02['text'] == btn04['text'] == btn06['text'] and btn02['text'] != '':
            print(btn02['text'], 'win')
            messagebox.showinfo("Game Over", btn02['text'] + " wins")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
        elif (btn00['text']!='' and
              btn01['text']!='' and
              btn02['text']!='' and
              btn03['text']!='' and
              btn04['text']!='' and
              btn05['text']!='' and
              btn06['text']!='' and
              btn07['text']!='' and
              btn08['text']!='' ):
            messagebox.showinfo("Game Over", "平局")
            Tic_Tac_Toe()
            root.destroy()
            set_btn_disabled()
            
        
             
    def set_btn_disabled():
        btn00['state'] = DISABLED
        btn01['state'] = DISABLED
        btn02['state'] = DISABLED
        btn03['state'] = DISABLED
        btn04['state'] = DISABLED
        btn05['state'] = DISABLED
        btn06['state'] = DISABLED
        btn07['state'] = DISABLED
        btn08['state'] = DISABLED
    root = Tk()
    root.title("Tic Tac Toe")
    root.geometry("300x300+200+100")
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    btn00 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn00))
    btn00.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn01 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn01))
    btn01.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn02 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn02))
    btn02.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)
    
    btn03 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn03))
    btn03.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn04 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn04))
    btn04.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn05 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn05))
    btn05.grid(row=1, column=2, sticky=NSEW, pady=2, padx=2)
    
    btn06 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn06))
    btn06.grid(row=2, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn07 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn07))
    btn07.grid(row=2, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn08 = Button(root, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn08))
    btn08.grid(row=2, column=2, sticky=NSEW, pady=2, padx=2)

if __name__=="__main__":
    root=Tk( )
    root.title('登入')
    root.geometry("250x200+200+100")    
    lab1 = Label(root, text="帳號", 
                    font=("Arial", 20),
                    justify=RIGHT)
    lab1.grid(row=0, column=0, padx=10, pady=10)
    username_lab=Entry(root)
    username_lab.grid(row=0, column=1, padx=10, pady=10)
    lab2 = Label(root, text="密碼", 
                font=("Arial", 20),
                justify=RIGHT)
    lab2.grid(row=1, column=0, padx=10, pady=10)
    password=Entry(root,show='㊣')
    password.grid(row=1,column=1,padx=10,pady=10)
    login_btn=Button(root,
                     text="登入",
                     command=login)
    login_btn.grid(row=2,column=1,padx=2,pady=20)
    root.mainloop()