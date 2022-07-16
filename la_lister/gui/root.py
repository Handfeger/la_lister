from __future__ import annotations

from tkinter import Canvas, Label, Tk


class Gui:
    def __init__(self) -> None:
        self.root: Tk = Tk()
        lab = Label(self.root, text="Hello World")
        lab.pack()

    def make_fullscreen(self) -> Gui:
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # --- fullscreen ---

        # root.overrideredirect(True)  # sometimes it is needed to toggle fullscreen
        # but then window doesn't get events from system
        # root.overrideredirect(False) # so you have to set it back

        self.root.attributes("-fullscreen", True)  # run fullscreen
        self.root.wm_attributes("-topmost", True)  # keep on top

        # --- closing methods ---

        # close window with key `ESC`
        def _on_escape(event):
            print("escaped")
            self.root.destroy()

        self.root.bind("<Escape>", _on_escape)

        # close window after 5s if `ESC` will not work
        # self.root.after(20000, self.root.destroy)

        return self

    def run(self) -> None:
        self.root.mainloop()
