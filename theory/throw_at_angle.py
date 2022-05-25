# imports
import tkinter as tk
from theory.practice.throw_at_angle import ThrowAtAngle as th
global gapp


class ThrowAtAngle:
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
        self.window.title("Course - Throw at an angle")
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
        welcome_label = tk.Label(second_frame, text="Horizontal Throw")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white', pady=20)
        middle_label = tk.Label(second_frame, text="Throw at an angle")
        middle_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white', pady=20)
        t1 = """In projectile motion, horizontal and vertical motion are independent of each other,as neither movement affects the other. This is the principle of compound motion that Galileo established in 1638 and used to demonstrate the parabolic form of projectile motion. The horizontal and vertical components of a projectile's velocity are independent, so the ballistic trajectory is a parabola of constant acceleration, as in a spacecraft with constant acceleration in the absence of other external forces. On Earth, acceleration varies with altitude and direction with latitude/longitude. This results in an elliptical trajectory that is very close to a parabola when viewed on a small scale. Since in this system the acceleration occurs only in the vertical direction, the horizontal component of the velocity remains constant and corresponds to its initial value. The vertical component of the movement is nothing more than free fall, just as described in the previous chapter. The components of the acceleration are """
        p1 = tk.Label(second_frame, text=t1)
        t2 = """So the acceleration on the vertical axis is not zero, the velocity vector and the components can be written as follows"""
        p2 = tk.Label(second_frame, text=t2)
        t3 = """Because the velocities are nonzero on both the horizontal and vertical axes, there are separate equations for the x and y directions """
        p3 = tk.Label(second_frame, text=t3)
        t4 = """Rewriting these equations, one can find a function y(x) that represents the trajectory of the bullet without considering the time of plotting """
        p4 = tk.Label(second_frame, text=t4)
        t5 = """This case bears a close resemblance to the case discussed above, with the difference that an angle φ has been introduced between the horizontal axis and the orientation of the velocity vector. Because of this angle, the projectile also has an initial velocity component on the vertical axis, rather than just the horizontal axis """
        p5 = tk.Label(second_frame, text=t5)
        t6 = """Because the velocities are nonzero on both the horizontal and vertical axes, there are separate equations for the x and y directions """
        p6 = tk.Label(second_frame, text=t6)
        t7 = """Rewriting these equations, one can find a function y(x) that represents the trajectory of the bullet without considering the time of plotting """
        p7 = tk.Label(second_frame, text=t7)

        p1.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1160, padx=30, pady=25)
        p2.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1160, padx=30, pady=25)
        p3.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1160, padx=30, pady=25)
        p4.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1160, padx=30, pady=25)
        p5.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1160, padx=30, pady=25)
        p6.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1160, padx=30, pady=25)
        p7.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1160, padx=30, pady=25)

        img1 = tk.PhotoImage(file="images/ta1.png")
        img1_lbl = tk.Label(second_frame, image=img1, pady=25)
        img2 = tk.PhotoImage(file="images/ta2.png")
        img2_lbl = tk.Label(second_frame, image=img2, pady=25)
        img3 = tk.PhotoImage(file="images/ta3.png")
        img3_lbl = tk.Label(second_frame, image=img3, pady=25)
        img4 = tk.PhotoImage(file="images/ta4.png")
        img4_lbl = tk.Label(second_frame, image=img4, pady=25)
        img5 = tk.PhotoImage(file="images/ta5.png")
        img5_lbl = tk.Label(second_frame, image=img5, pady=25)
        img6 = tk.PhotoImage(file="images/ta6.png")
        img6_lbl = tk.Label(second_frame, image=img6, pady=25)
        img7 = tk.PhotoImage(file="images/ta7.png")
        img7_lbl = tk.Label(second_frame, image=img7, pady=25)
        img8 = tk.PhotoImage(file="images/ta8.png")
        img8_lbl = tk.Label(second_frame, image=img8, pady=25)
        buttom = tk.Button(second_frame, text='Practice', command=lambda: self.do_practice())
        buttom.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        fw_img = tk.PhotoImage(file="images/arrow_fw.png")
        hm_img = tk.PhotoImage(file="images/home.png")
        bck_img = tk.PhotoImage(file="images/arrow_bck.png")
        forward_butt = tk.Button(second_frame, image=fw_img, command=lambda: self.do_threebody(), bg='#0e1c1d',
                                 fg='white', pady=30, border=0)
        back_butt = tk.Button(second_frame, image=bck_img, command=lambda: self.do_throwdown(), bg='#0e1c1d',
                              fg='white', pady=30, border=0)
        home_butt = tk.Button(second_frame, image=hm_img, command=lambda: self.do_course(), bg='#0e1c1d', fg='white',
                              pady=30, border=0)

        # pack all the UI elements to the frame
        welcome_label.grid(row=0, column=1)
        forward_butt.grid(row=0, column=2)
        back_butt.grid(row=0, column=0)
        home_butt.grid(row=1, column=0)
        p1.grid(row=2, column=1)
        img1_lbl.grid(row=3, column=1)
        p2.grid(row=4, column=1)
        img2_lbl.grid(row=5, column=1)
        p3.grid(row=6, column=1)
        img3_lbl.grid(row=7, column=1)
        p4.grid(row=8, column=1)
        img4_lbl.grid(row=9, column=1)
        img5_lbl.grid(row=10, column=1)
        middle_label.grid(row=11, column=1)
        p5.grid(row=12, column=1)
        img6_lbl.grid(row=13, column=1)
        p6.grid(row=14, column=1)
        img7_lbl.grid(row=15, column=1)
        p7.grid(row=16, column=1)
        img8_lbl.grid(row=17, column=1)
        buttom.grid(row=18, column=1)

        # Add that New Frame a Window In The Canvas
        self.my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        self.window.mainloop()

    def do_practice(self):
        freefall = th()
        theory = ThrowAtAngle()
        global gapp
        theory.app = gapp
        freefall.app = gapp
        freefall.practice = theory
        self.window.destroy()
        freefall.run(theory, gapp, h=100, m=1, v=20, phi=30, t=5)

    def do_threebody(self):
        self.practice.do_threebody(window=self.window)

    def do_throwdown(self):
        print(self.practice)
        if type(self.practice) is ThrowAtAngle:
            global gapp
            gapp.do_courses(self.window)
        else:
            self.practice.do_throwdown(window=self.window)

    def do_course(self):
        global gapp
        print(gapp)
        print(self.practice)
        gapp.do_courses(self.window)