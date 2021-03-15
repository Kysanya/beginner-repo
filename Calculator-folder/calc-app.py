# Calculator

from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master

        master.geometry("312x324")
        master.resizable(0, 0)
        master.title("Calculator")

        self.input_frame = Frame(master, width=312, height=50, bg="#CCBCBC", highlightbackground="#A288A6",
                            highlightcolor="#BB9BB0", highlightthickness=2)
        self.input_frame.pack(side=TOP)

        self.e = Entry(self.input_frame, width=50, borderwidth=5, justify=RIGHT, font=('Verdana', 14, 'bold'))
        self.e.grid(row=0, column=0)
        self.e.pack(ipady=2)

        self.btn_frame = Frame(master, width=312, height=272.5, bg="#F1E3E4")
        self.btn_frame.pack()

        # Buttons
        # First row

        btn_7 = Button(self.btn_frame, width=10, height=3, text="7", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("7"))
        btn_7.grid(row=1, column=0, padx=1, pady=1)
        btn_8 = Button(self.btn_frame, width=10, height=3, text="8", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("8"))
        btn_8.grid(row=1, column=1, padx=1, pady=1)
        btn_9 = Button(self.btn_frame, width=10, height=3, text="9", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("9"))
        btn_9.grid(row=1, column=2, padx=1, pady=1)
        btn_add = Button(self.btn_frame, width=10, height=3, text="+", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                         command=lambda: self.btn_click("+"))
        btn_add.grid(row=1, column=3, padx=1, pady=1)

        # second row

        btn_4 = Button(self.btn_frame, width=10, height=3, text="4", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("4"))
        btn_4.grid(row=2, column=0, padx=1, pady=1)
        btn_5 = Button(self.btn_frame, width=10, height=3, text="5", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("5"))
        btn_5.grid(row=2, column=1, padx=1, pady=1)
        btn_6 = Button(self.btn_frame, width=10, height=3, text="6", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("6"))
        btn_6.grid(row=2, column=2, padx=1, pady=1)
        btn_minus = Button(self.btn_frame, width=10, height=3, text="-", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                           command=lambda: self.btn_click("-"))
        btn_minus.grid(row=2, column=3, padx=1, pady=1)

        # Third row

        btn_1 = Button(self.btn_frame, width=10, height=3, text="1", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("1"))
        btn_1.grid(row=3, column=0, padx=1, pady=1)
        btn_2 = Button(self.btn_frame, width=10, height=3, text="2", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("2"))
        btn_2.grid(row=3, column=1, padx=1, pady=1)
        btn_3 = Button(self.btn_frame, width=10, height=3, text="3", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("3"))
        btn_3.grid(row=3, column=2, padx=1, pady=1)
        btn_multiply = Button(self.btn_frame, width=10, height=3, text="*", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                              command=lambda: self.btn_click("*"))
        btn_multiply.grid(row=3, column=3, padx=1, pady=1)

        # Fourth row

        btn_0 = Button(self.btn_frame, width=22, height=3, text="0", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                       command=lambda: self.btn_click("0"))
        btn_0.grid(row=4, columnspan=2, padx=1, pady=1)
        btn_point = Button(self.btn_frame, width=10, height=3, text=".", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                           command=lambda: self.btn_click("."))
        btn_point.grid(row=4, column=2, padx=1, pady=1)
        btn_divide = Button(self.btn_frame, width=10, height=3, text="/", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                            command=lambda: self.btn_click("/"))
        btn_divide.grid(row=4, column=3, padx=1, pady=1)

        # Fifth row

        btn_clear = Button(self.btn_frame, width=34, height=3, text="Del", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                           command=lambda: self.btn_click("Del"))
        btn_clear.grid(row=5, columnspan=3, padx=1, pady=1)
        btn_equals = Button(self.btn_frame, width=10, height=3, text="=", fg="#1C1D21", bg="#CCBCBC", cursor="hand2",
                            command=lambda: self.btn_click("="))
        btn_equals.grid(row=5, column=3, padx=1, pady=1)

        # btn click method

    def btn_click(self, value):
        try:
            current_num = str(self.e.get())
            # check if user clicked Del
            if value == 'Del':
                self.e.delete(-1, END)
            # check if = sign was clicked
            elif value == '=':
                result = str(eval(current_num))
                self.e.delete(-1, END)
                self.e.insert(0, result)
            else:
                self.e.delete(0, END)
                self.e.insert(-1, current_num + value)
        except NameError:
            print("Sorry, The operation cannot be Completed.")
        except ZeroDivisionError:
            print("Math Error! Zero Division is not allowed")
        except SyntaxError:
            print("Wrong Math Operation. Try again")


if __name__ == '__main__':
    root = Tk()
    app = Calculator(root)
    root.mainloop()
