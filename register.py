from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Title")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="images/Night.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="images/Tree.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # ===== Register Frame =====
        frame1 = Frame(self.root, bg="black")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="green").place(
            x=200, y=25)

        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=70)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=120, width=250)
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=350, y=70)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=350, y=120, width=250)
        # =======
        contact_name = Label(frame1, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=150)
        self.txt_contact_name = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact_name.place(x=50, y=190, width=250)

        email_name = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=350, y=150)
        self.txt_email_name = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email_name.place(x=350, y=190, width=250)
        # =======
        question = Label(frame1, text="Security", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=220)

        self.combo_box = ttk.Combobox(frame1, font=("times new roman", 12), state="readonly", justify="center")
        self.combo_box["values"] = ("select", "Whats your crush Name", "Name of your EX", "Where you were born")
        self.combo_box.place(x=50, y=260, width=250)
        self.combo_box.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=350,
                                                                                                                 y=220)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=350, y=260, width=250)

        # ===

        password_name = Label(frame1, text="Passworrd", font=("times new roman", 15, "bold"), bg="white",
                              fg="gray").place(x=50, y=290)
        self.txt_password_name = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password_name.place(x=50, y=330, width=250)

        confirm_pass_name = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                                  fg="gray").place(x=350, y=290)
        self.txt_confirm_pass_name = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_confirm_pass_name.place(x=350, y=330,width=250)

        chk = Checkbutton(frame1, text="Agree our Terms And Conditons", onvalue=1, offvalue=0, bg="white",
                          font=("times new roman", 10)).place(x=50, y=370)

        self.btn = Button(frame1, text="Register", font=("times new roman", 20), bg="gray", fg="Blue", cursor="hand2")
        self.btn.place(x=260,y=390)

        btn_sign = Button(self.root, text="Log In", font=("times new roman", 20), bg="gray", fg="Blue",
                          cursor="hand2").place(x=260, y=390)


    def register_data(self):
        print(self.txt_fname.get(),
              self.txt_lname.get(),
              self.txt_password_name.get(),
              self.txt_contact_name.get(),
              self.txt_email_name.get(),
              self.combo_box.get(),
              self.txt_confirm_pass_name.get())



root = Tk()
obj = Register(root)
root.mainloop()
