from tkinter import ttk
from typing import Literal, Callable
import json



class BorderlessScrollbar(ttk.Scrollbar):
    def __init__(
            self, 
            master, 
            background: str = "#5F5F5F", 
            troughcolor: str = "#202020", 
            active_color: str = "#737373", 
            orient: Literal["horizontal", "vertical"] = "vertical",
            command: Callable[..., tuple[float, float] | None] | str = ""
        ):
        super().__init__(master=master, orient=orient, command=command)
        self.background = background
        self.troughcolor = troughcolor
        self.active_color = active_color
        self.set_scrollbar_style()

    def set_scrollbar_style(self):
        style = ttk.Style()
        style.theme_use("classic")
        with open("../Style/Scrollbar.json", "r", encoding="utf-8") as file:
            scrollbar_style_template: dict = json.load(file)
        scrollbar_style_sheet = dict()
        for key, value in scrollbar_style_template.items():
            if value == "background":
                scrollbar_style_sheet[key] = self.background
            elif value == "troughcolor":
                scrollbar_style_sheet[key] = self.troughcolor
            else:
                scrollbar_style_sheet[key] = value
        print(scrollbar_style_sheet)
        style.map("TScrollbar", background=[('active', self.active_color)])
        style.configure("Vertical.TScrollbar", **scrollbar_style_sheet)
        style.configure("Horizontal.TScrollbar", **scrollbar_style_sheet)


if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("单独配置的 Scrollbar 示例")
    text_box = tk.Text(root, width=40, height=10)
    text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = BorderlessScrollbar(root, command=text_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_box.config(yscrollcommand=scrollbar.set)
    for i in range(20):
        text_box.insert(tk.END, f"这是第 {i + 1} 行文本。\n")

    root.mainloop()
