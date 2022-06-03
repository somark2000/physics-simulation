# imports
import tkinter as tk
from theory.practice.vertical_throw_up import VerticalThrowUp as vt
global gapp


class VerticalThrowUp:
    def __init__(self):
        self.y_scrollbar = None
        self.my_canvas = None
        self.sec = None
        self.main_frame = None
        self.window = None
        self.app = None
        self.practice = None

    def run(self, practice, app):
        self.practice = practice
        self.app = app
        global gapp
        gapp = app
        # setup for the UI window
        self.window = tk.Tk()
        self.window.configure(bg='#0e1c1d')
        self.window.geometry("1300x900")
        self.window.title("Course - Vertical throw up")
        # Create A Main frame
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        # Create Frame for X Scrollbar
        self.sec = tk.Frame(self.main_frame)
        self.sec.pack(fill=tk.X, side=tk.BOTTOM)

        # Create A Canvas
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add A Scrollbars to Canvas
        self.y_scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.my_canvas.yview)
        self.y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.my_canvas.configure(bg='#0e1c1d')
        self.my_canvas.bind("<Configure>", lambda e: self.my_canvas.config(scrollregion=self.my_canvas.bbox(tk.ALL)))

        # Create Another Frame INSIDE the Canvas
        second_frame = tk.Frame(self.my_canvas)
        second_frame.configure(bg='#0e1c1d')
        welcome_label = tk.Label(second_frame, text="Throw Up")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white', pady=30)
        t1 = """This case is identical to the previous one, the only difference being that the initial speed is not zero and its upwards orientation determines the sign of the coefficient v0 """
        p1 = tk.Label(second_frame, text=t1)
        t2 = """As in this case, the equations of motion and the equations for the velocities for the upward throw are as follows """
        p2 = tk.Label(second_frame, text=t2)
        t3 = """Based on the equations above, it can be stated that the positions time dependency will be a parabola with a maximum higher than the initial position and the velocity will decrease with a constant rate from its maximum value at the beginning and will be 0 at the exact same moment the projectile will peak in its height """
        p3 = tk.Label(second_frame, text=t3)

        p1.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)
        p2.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)
        p3.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)

        img1 = tk.PhotoImage(file="images/vt.png")
        img1_lbl = tk.Label(second_frame, image=img1, pady=25)
        img2 = tk.PhotoImage(file="images/vtu1.png")
        img2_lbl = tk.Label(second_frame, image=img2, pady=25)
        buttom = tk.Button(second_frame, text='Practice', command=lambda: self.do_practice())
        buttom.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        fw_img = tk.PhotoImage(file="images/arrow_fw.png")
        hm_img = tk.PhotoImage(file="images/home.png")
        bck_img = tk.PhotoImage(file="images/arrow_bck.png")
        forward_butt = tk.Button(second_frame, image=fw_img, command=lambda: self.do_throwdown(), bg='#0e1c1d',
                                 fg='white', pady=30, border=0)
        back_butt = tk.Button(second_frame, image=bck_img, command=lambda: self.do_freefall(), bg='#0e1c1d',
                                 fg='white', pady=30, border=0)
        home_butt = tk.Button(second_frame, image=hm_img, command=lambda: self.do_course(), bg='#0e1c1d', fg='white',
                              pady=30, border=0)

        # pack all the UI elements to the frame
        welcome_label.grid(row=0, column=1)
        p1.grid(row=1, column=1)
        p2.grid(row=2, column=1)
        img1_lbl.grid(row=3, column=1)
        p3.grid(row=4, column=1)
        img2_lbl.grid(row=5, column=1)
        buttom.grid(row=10, column=1)
        forward_butt.grid(row=0, column=2)
        back_butt.grid(row=0, column=0)
        home_butt.grid(row=1, column=0)

        # Add that New Frame a Window In The Canvas
        self.my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        self.window.mainloop()

    def do_practice(self):
        freefall = vt()
        theory = VerticalThrowUp()
        global gapp
        theory.app = gapp
        freefall.app = gapp
        freefall.practice = theory
        self.window.destroy()
        freefall.run(theory, gapp, h=20, m=1, v=10, t=3)

    def do_throwdown(self):
        try:
            self.practice.do_throwdown(window=self.window)
        except:
            gapp.do_courses(self.window)

    def do_freefall(self):
        print(self.practice)
        if type(self.practice) is VerticalThrowUp:
            global gapp
            gapp.do_courses(self.window)
        else:
            self.practice.do_freefall(window=self.window)

    def do_course(self):
        global gapp
        print(gapp)
        print(self.practice)
        gapp.do_courses(self.window)
