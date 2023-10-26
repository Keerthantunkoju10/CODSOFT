import tkinter as tk

class Calculator:

    def __init__(self, master):
        self.master = master

        # Create the frames
        self.frame1 = tk.Frame(master)
        self.frame2 = tk.Frame(master)

        # Create the labels
        self.label1 = tk.Label(self.frame1, text="First Number:")
        self.label2 = tk.Label(self.frame1, text="Second Number:")
        self.label3 = tk.Label(self.frame2, text="Result:")

        # Create the entries
        self.entry1 = tk.Entry(self.frame1)
        self.entry2 = tk.Entry(self.frame1)
        self.entry3 = tk.Entry(self.frame2)

        # Create the buttons
        self.button1 = tk.Button(self.frame1, text="+", command=self.add)
        self.button2 = tk.Button(self.frame1, text="-", command=self.subtract)
        self.button3 = tk.Button(self.frame1, text="*", command=self.multiply)
        self.button4 = tk.Button(self.frame1, text="/", command=self.divide)

        # Pack the labels and entries
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.label3.pack()
        self.entry3.pack()

        # Pack the buttons
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()

        # Place the frames
        self.frame1.place(x=0, y=0)
        self.frame2.place(x=100, y=0)

    def add(self):
        self.result = float(self.entry1.get()) + float(self.entry2.get())
        self.entry3.delete(0, "end")
        self.entry3.insert(0, str(self.result))

    def subtract(self):
        self.result = float(self.entry1.get()) - float(self.entry2.get())
        self.entry3.delete(0, "end")
        self.entry3.insert(0, str(self.result))

    def multiply(self):
        self.result = float(self.entry1.get()) * float(self.entry2.get())
        self.entry3.delete(0, "end")
        self.entry3.insert(0, str(self.result))

    def divide(self):
        self.result = float(self.entry1.get()) / float(self.entry2.get())
        self.entry3.delete(0, "end")
        self.entry3.insert(0, str(self.result))

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
