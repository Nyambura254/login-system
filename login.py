#importing module

from tkinter import*
import sqlite3


#setting  up the main frame
#for the application after importing the modules
root = Tk()
root.title("LifeCheck-Pharm Login Application")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#designing the layout
#after creating main frame add some layout to the application.
#=====VARIABLES=====#
USERNAME=StringVar()
PASSWORD=StringVar()


#=========FRAMES=======#
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)


#==========LABELS======#
lbl_title = Label(Top, text = "LifeCheck-Pharm Login Application", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)


#========ENTRY WIDGETS======#
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)


#========BUTTON WIDGETS======#
btn_login = Button(Form, text="Login", width=45, command="Login")
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', "Login")


#creating database connection
#after setting up the design, create a database function.

#=======methods======#
def Database():
    global conn, cursor
    conn= sqlite3.connect("pythontut.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'member' (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT*FROM 'member' WHERE 'username'='admin' AND 'password' ='admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO 'member' (username,password) VALUES ('admin', 'admin')")
        conn.commit()


#creating the main function:   to check if the user exists in the database.
# after login a new window should pop up.
        
def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
 
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("LifeCheck-Pharm Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
 
def Back():
    Home.destroy()
    root.deiconify()

    
#initializing the application after saving to run the code
#and check if the main is initialize propery.

#======initialization=====#

if __name__ == '__main__':
    root.mainloop()
    


