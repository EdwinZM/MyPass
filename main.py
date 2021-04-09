import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(width=430, height=320)

image = tkinter.PhotoImage(file="logo.png")

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

web_input = tkinter.Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
email_input = tkinter.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
pass_input = tkinter.Entry(width=21)
pass_input.grid(column=1, row=3, sticky="w")

#Buttons

gen_btn = tkinter.Button(text="Generate Password")
gen_btn.grid(column=2, row=3, sticky="w")
add_btn = tkinter.Button(text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()