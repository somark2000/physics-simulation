# imports
import tkinter as tk


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
        # setup for the UI window
        self.window = tk.Tk()
        self.window.configure(bg='#0e1c1d')
        self.window.geometry("1200x900")
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
        welcome_label = tk.Label(second_frame, text="Free Fall")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white', pady=20)
        t1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sodales sagittis enim, nec mattis nunc placerat sit amet. Sed egestas ornare turpis. Ut accumsan nulla eget orci molestie venenatis. Vestibulum lobortis lectus quis odio pharetra vehicula. Mauris at velit semper, dignissim nisl non, pulvinar velit. Nulla sit amet egestas mi, a vehicula leo. Mauris arcu sapien, porttitor vitae semper in, sodales rutrum odio. Donec rhoncus massa vel est lobortis tristique. Fusce eu pellentesque nisi, ac rhoncus turpis. Ut vehicula, mauris a mattis sagittis, odio diam vehicula nisl, a sollicitudin lorem ante in lacus."""
        p1 = tk.Label(second_frame, text=t1)
        p2 = tk.Label(second_frame, text=t1)
        p3 = tk.Label(second_frame, text=t1)
        p4 = tk.Label(second_frame, text=t1)
        p5 = tk.Label(second_frame, text=t1)

        p1.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p2.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p3.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p4.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p5.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)

        # pack all the UI elements to the frame
        welcome_label.grid(row=0, column=0)
        p1.grid(row=1, column=0)
        p2.grid(row=2, column=0)
        p3.grid(row=3, column=0)
        p4.grid(row=4, column=0)
        p5.grid(row=5, column=0)

        # Add that New Frame a Window In The Canvas
        self.my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        self.window.mainloop()