# imports
import tkinter as tk
from theory.practice.three_body import ThreeBody as tb
global gapp


class ThreeBody:
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
        self.window.geometry("1200x900")
        self.window.title("Course - Three-Body Problem")
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
        welcome_label = tk.Label(second_frame, text="Three-Body Problem")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white', pady=20)
        t1 = """In classical mechanics, the three-body problem is a problem that involves determining the initial 
        positions and moments of three-point masses and solving their subsequent motion according to Newton's laws of 
        motion and Newton's law of universal gravitation. The three-body problem is a special case of the n-body 
        problem, where, in contrast to the two-body problem, there are no there is a general closed solution. Because 
        the resulting dynamical system is chaotic for most initial conditions, numerical methods are usually required 
        to approximate the trajectory, despite some limited problems that are analytically solvable """
        p1 = tk.Label(second_frame, text=t1)
        p2 = tk.Label(second_frame, text=t1)

        p1.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p2.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)

        buttom = tk.Button(second_frame, text='Practice', command=lambda: self.do_practice())
        buttom.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        hm_img = tk.PhotoImage(file="images/home.png")
        bck_img = tk.PhotoImage(file="images/arrow_bck.png")
        back_butt = tk.Button(second_frame, image=bck_img, command=lambda: self.do_throwatangle(), bg='#0e1c1d',
                              fg='white', pady=30, border=0)
        home_butt = tk.Button(second_frame, image=hm_img, command=lambda: self.do_course(), bg='#0e1c1d', fg='white',
                              pady=30, border=0)

        # pack all the UI elements to the frame
        welcome_label.grid(row=0, column=0)
        home_butt.grid(row=0, column=2)
        back_butt.grid(row=0, column=0)
        p1.grid(row=1, column=0)
        p2.grid(row=2, column=0)

        # Add that New Frame a Window In The Canvas
        self.my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        self.window.mainloop()

    def do_practice(self):
        freefall = tb()
        theory = ThreeBody()
        global gapp
        theory.app = gapp
        freefall.app = gapp
        freefall.practice = theory
        self.window.destroy()
        freefall.run(theory, gapp)

    def do_throwatangle(self):
        print(self.practice)
        if type(self.practice) is ThreeBody:
            global gapp
            gapp.do_courses(self.window)
        else:
            self.practice.do_throwatangle(window=self.window)

    def do_course(self):
        global gapp
        print(gapp)
        print(self.practice)
        gapp.do_courses(self.window)