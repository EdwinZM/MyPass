import tkinter
import os
from tkinter import messagebox
import random
from PIL import ImageTk
import json

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_input.delete(0, len(pass_input.get()))
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'
    , 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z','1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$','%'
    ,'&','/','*', '+','-','@']

    password = ""

    for i in range(random.randint(8, 15)):
        x = random.choice(characters)
        password += x
    pass_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():

    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {website:{
        "email": email,
        "password": password
    }}

    if len(website) > 0 and len(email) > 0 and len(password) >= 8:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("./user_info.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except:
                with open("./user_info.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("./user_info.json", "w") as file:
                    json.dump(data, file, indent=4)
        web_input.delete(0, len(website))
        pass_input.delete(0, len(password))
    
    else:
        messagebox.showerror(title="Error submitting info.", 
        message="Fields shouldn't be empty and password must be greater than 8 characters.")

def search():
    search_web = web_input.get()

    try:
        with open("./user_info.json") as file:
            data = json.load(file)
            content = data[search_web]
            email = content["email"]
            password = content["password"]
        
        messagebox.showinfo(title=f"{search_web}", message=f"Email: {email}\nPassword: {password}")
    except:
        messagebox.showerror(title="Error on Search", message="Website information not found.")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=430, height=320)

image = ImageTk.PhotoImage(file=resource_path("logo.png"))

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(0, 0, image=image, anchor="nw")
canvas.grid(column=1, row=0)

#Labels

web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = tkinter.Label(text="Password:")
pass_label.grid(column=0, row=3)

#Entries

web_input = tkinter.Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()
email_input = tkinter.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
pass_input = tkinter.Entry(width=21)
pass_input.grid(column=1, row=3)

#Buttons

gen_btn = tkinter.Button(text="Generate Password", command=generate_password)
gen_btn.grid(column=2, row=3, sticky="w")
add_btn = tkinter.Button(text="Add", width=36, command=save_info)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn = tkinter.Button(text="Search", command=search)
search_btn.grid(column=2, row=1, sticky="e w")



window.mainloop()