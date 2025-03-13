from customtkinter import CTkCanvas
import tkinter as tk


class RoundedRectangle(CTkCanvas):
    def __init__(
            self,
            master,
            text="",
            round_radius=28,
            **kwargs
    ):
        self.bg = kwargs.pop("bg", "#C1E8BB")
        self.text = text
        self.master = master
        super().__init__(bg=self.transparent_color)
        self.r = round_radius // 2

    @property
    def transparent_color(self):
        try:
            return self.master.cget("bg")
        except tk.TclError:
            return "SystemButtonFace"

    def place(self, *args, **kwargs):
        super().place(*args, **kwargs)
        self.update()
        self.__draw(self.bg)

    def config(self, *args, **kwargs):
        bg = kwargs.pop("bg", None)
        if bg is not None:
            self.__draw(bg)
        super().config(*args, **kwargs)

    def __draw(self, bg):
        width, height = self.winfo_width(), self.winfo_height()
        self.create_rectangle(
            0, self.r, width, height - self.r, fill=bg, outline=bg
        )

        self.create_rectangle(
            self.r, 0, width - self.r, height, fill=bg, outline=bg
        )

        self.create_aa_circle(self.r, self.r, self.r, fill=bg)
        self.create_aa_circle(self.r, height - self.r, self.r, fill=bg)
        self.create_aa_circle(width - self.r, self.r, self.r, fill=bg)
        self.create_aa_circle(width - self.r, height - self.r, self.r, fill=bg)
        self.create_text(width // 2, height // 2, text=self.text, font=("微软雅黑", 14), fill="white")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("320x100+500+300")
    flat_btn = RoundedRectangle(root, bg="red", text="十 新建")
    flat_btn.place(x=40, y=30, width=230, height=30)
    root.mainloop()
