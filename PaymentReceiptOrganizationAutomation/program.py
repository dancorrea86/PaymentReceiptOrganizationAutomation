import tkinter as tk
from tkinter import ttk


class windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Organizar de comprovantes")

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, SidePage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
            frame = self.frames[cont]
            # raises the current frame to the top
            frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        label2 = tk.Label(self, text="Hello World!")
        label2.pack(padx=10, pady=10)
        label3 = tk.Button(self, text="Quit", command=self.destroy)
        label3.pack(padx=10, pady=10)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()