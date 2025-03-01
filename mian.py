import mysql.connector as c
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter import Tk, ttk
con = c.connect(user = 'root', host = "localhost", passwd = "admin",database = "blood_bank")
cur = con.cursor()
ls = ["A+","B+","AB+","O+","A-","B-","AB-","O-"]
def donate():
    window2 = Tk()
    window2.geometry("900x400")
    l1 = tk.Label(window2, text = "Name of Donator", width = 30 , font = "bold")
    l1.grid(row= 1, column = 1)
    e1 = tk.Entry(window2, width=30)
    e1.grid(row =1, column = 3)
    l2 = tk.Label(window2, text = "Blood Group", width = 30, font = "bold")
    l2.grid(row =3, column =1)
    e2 = StringVar(window2)
    e2.set("Blood Group")
    drop = OptionMenu(window2, e2, *ls)
    drop.grid(row= 3, column = 3)
    b1 = tk.Button(window2, text = "Proceed",width = 30, command = lambda:add_user(e1,e2))
    b1.grid(row= 5, column = 2)
    window2.mainloop()

def add_user(e1,e2):
    name = e1.get()
    blood = e2.get()
    try:
        cmd = "update bank set qty = qty + 1 where blood_type = '{}'".format(blood)
        cur.execute(cmd)
        con.commit()
        cmd = "insert into user values('{}','{}')".format(name,blood)
        cur.execute(cmd)
        con.commit()
        messagebox.showinfo("Success","Successfully Updated the database")
    except Exception as e:
        messagebox.showerror("Error","We ran down some error -->  " + str(e) + "  please try again...")

def check_stock():
    window3 = Tk()
    window3.geometry("900x400")
    l1 = tk.Label(window3, text = "Blood Group",width = 30, font = "bold")
    l1.grid(row= 1, column =1 )
    e1 = StringVar(window3)
    e1.set("Blood Group")
    drop = OptionMenu(window3, e1,*ls)
    drop.grid(row= 1, column =3)
    b1 = tk.Button(window3, text = "Check By Blood Group",width = 30, command = lambda: check_by_blood(e1))
    b1.grid(row =2 , column = 2)
    b2 = tk.Button(window3, text = "List All in Store",width = 30, command = lambda: check_all_blood())
    b2.grid(row =3 , column = 2)
    window3.mainloop()

def check_by_blood(e1):
    blood_type = e1.get()
    window4 = Tk()
    window4.geometry("600x600")
    tree = ttk.Treeview(window4, columns  = ("c1","c2"), show = "headings", height = 30)
    tree.column("#1", anchor = "center")
    tree.heading("#1", text = "Blood Type")
    tree.column("#2", anchor = "center")
    tree.heading("#2", text = "Quantity")

    cmd = "select * from bank where blood_type = '{}'".format(blood_type)
    cur.execute(cmd)
    data = cur.fetchone()
    bl = data[0]
    qty = data[1]
    tree.insert('','end', text = "1", values =(bl,qty))
    tree.grid(row  =1 , column =1)
    window4.mainloop()

def check_all_blood():
    window4 = Tk()
    window4.geometry("600x600")
    tree = ttk.Treeview(window4, columns  = ("c1","c2"), show = "headings", height = 30)
    tree.column("#1", anchor = "center")
    tree.heading("#1", text = "Blood Type")
    tree.column("#2", anchor = "center")
    tree.heading("#2", text = "Quantity")

    cmd = "select * from bank"
    cur.execute(cmd)
    data = cur.fetchall()
    c = 1
    for i in data:
        bl = i[0]
        qty = i[1]
        tree.insert('','end', text = str(c), values =(bl,qty))
        c +=1
    tree.grid(row  =1 , column =1)
    window4.mainloop()
    

def check_donor():
    window5 = Tk()
    window5.geometry("900x600")
    l1 = tk.Label(window5, text = "Name of Donator", width = 30 , font = "bold")
    l1.grid(row= 1, column = 1)
    e1 = tk.Entry(window5, width=30)
    e1.grid(row =1, column = 3)
    b1 = tk.Button(window5, text = "Check By Name",width = 30, command = lambda: check_by_name(e1))
    b1.grid(row =2 , column = 2)
    b2 = tk.Button(window5, text = "List All Donor",width = 30, command = lambda: check_all_user())
    b2.grid(row =3 , column = 2)
    window5.mainloop()
def check_by_name(e1):
    name = e1.get()
    try:
        window6 = Tk()
        window6.geometry("600x600")
        tree = ttk.Treeview(window6, columns  = ("c1","c2"), show = "headings", height = 30)
        tree.column("#1", anchor = "center")
        tree.heading("#1", text = "Donor Name")
        tree.column("#2", anchor = "center")
        tree.heading("#2", text = "Blood Group")

        cmd = "select * from user where name = '{}'".format(name)
        cur.execute(cmd)
        data = cur.fetchall()
        c = 1
        for i in data:
            name = i[0]
            bl_gp = i[1]
            tree.insert('','end', text = str(c), values =(name,bl_gp))
            c +=1
        tree.grid(row  =1 , column =1)
    except Exception as e:
        messagebox.showerror("Error","We ran into some error -->  "+ str(e) + "  Please try again...")


def check_all_user():
    try:
        window7 = Tk()
        window7.geometry("600x600")
        tree = ttk.Treeview(window7, columns  = ("c1","c2"), show = "headings", height = 30)
        tree.column("#1", anchor = "center")
        tree.heading("#1", text = "Donor Name")
        tree.column("#2", anchor = "center")
        tree.heading("#2", text = "Blood Group")

        cmd = "select * from user"
        cur.execute(cmd)
        data = cur.fetchall()
        c = 1
        for i in data:
            name = i[0]
            bl_gp = i[1]
            tree.insert('','end', text = str(c), values =(name,bl_gp))
            c +=1
        tree.grid(row  =1 , column =1)
    except Exception as e:
        messagebox.showerror("Error","We ran into some error -->  "+ str(e) + "  Please try again...")




window =Tk()
window.geometry("500x500")
window.configure(bg = "blue")
l1 = tk.Label(window, text = "Welcome to Blood Bank", width = 30, font = "bold")
l1.pack()
l1.configure(bg ="black", fg = "white")
b1 = tk.Button(window, text = "Donate", width = 30 ,command = lambda:donate())
b1.pack()
b2 = tk.Button(window, text = "Check Stock", width = 30 , command = lambda:check_stock())
b2.pack()
b3 = tk.Button(window,text = "Check Donor", width = 30, command = lambda: check_donor())
b3.pack()
window.mainloop()
