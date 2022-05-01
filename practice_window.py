# imports
import tkinter as tk

class PracticeWindow():
    def run(self):
        # setup for the UI window
        window = tk.Tk()
        window.title("Hodeeeme")
        window.geometry('800x500')
        bg = tk.PhotoImage(file="images/bg.png")
        bg_label = tk.Label(window, image=bg)
        welcome_label = tk.Label(window, text="Practice")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white')

        p1_butt = tk.Button(text='Free fall', command=self.do_freefall)
        p1_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p2_butt = tk.Button(text='Throw down', command=self.do_throwdown)
        p2_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p3_butt = tk.Button(text='Throw up', command=self.do_throwup)
        p3_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p4_butt = tk.Button(text='Throw at an angle', command=self.do_throwatangle)
        p4_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p5_butt = tk.Button(text='Three Body Problem', command=self.do_threebody)
        p5_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')

        bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        welcome_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        p1_butt.place(relx=0.35, rely=0.40, anchor=tk.CENTER)
        p2_butt.place(relx=0.65, rely=0.40, anchor=tk.CENTER)
        p3_butt.place(relx=0.35, rely=0.55, anchor=tk.CENTER)
        p4_butt.place(relx=0.65, rely=0.55, anchor=tk.CENTER)
        p5_butt.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

        window.mainloop()


    def do_freefall(self):
        pass

    def do_throwup(self):
        pass

    def do_throwdown(self):
        pass

    def do_throwatangle(self):
        pass

    def do_threebody(self):
        pass

