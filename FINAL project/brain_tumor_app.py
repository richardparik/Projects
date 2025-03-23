from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import webbrowser
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Okno
window = customtkinter.CTk()
window.minsize(700, 400)
window.resizable(False, False)
window.title("Brain Tumor app")
icon_path = resource_path("icon_brain.ico")
window.iconbitmap(icon_path)
window.config(bg="#5b5b5b")
my_font = customtkinter.CTkFont(family="Cambria", size=16, weight="bold")
customtkinter.set_appearance_mode("Dark")

# Canvas
canvas = customtkinter.CTkCanvas(window, width=470, height=220, bg="#d3d3d3")
canvas.pack(pady=(10, 0))
brain_img = Image.open(resource_path("canvas_brain.png"))
canvas.image = ImageTk.PhotoImage(Image.open(resource_path("canvas_brain.png")))
canvas.create_image(0, 0, anchor="nw", image=canvas.image)

# Frame
GPS_frame = customtkinter.CTkFrame(window, fg_color="#5b5b5b")
GPS_frame.pack(pady=10)

# Buttons with icons using CTkImage
github_icon = customtkinter.CTkImage(Image.open(resource_path("icon_github.png")))
colab_icon = customtkinter.CTkImage(Image.open(resource_path("icon_colab.png")))
slides_icon = customtkinter.CTkImage(Image.open(resource_path("icon_slides.png")))
kaggle_icon = customtkinter.CTkImage(Image.open(resource_path("icon_kaggle.png")))

github_button = customtkinter.CTkButton(
    GPS_frame, text=" GitHub repository",
    image=github_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://github.com/richardparik/Projects/tree/master/FINAL%20project")
)
github_button.pack(pady=5)

colab_button = customtkinter.CTkButton(
    GPS_frame, text=" Colab notebook",
    image=colab_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://colab.research.google.com/github/richardparik/Projects/blob/master/FINAL%20project/Final_project.ipynb")
)
colab_button.pack(pady=5)

final_pres_button = customtkinter.CTkButton(
    GPS_frame, text=" Final presentation",
    image=slides_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://docs.google.com/presentation/d/1mnFfKyp6MdNfgLgWNUqYdjkljmHksM0cNtp4gPG4Wws/edit?slide=id.p#slide=id.p")
)
final_pres_button.pack(pady=5)

kaggle_button = customtkinter.CTkButton(
    GPS_frame, text=" Kaggle dataset",
    image=kaggle_icon,
    fg_color="#5b5b5b", border_spacing=3, corner_radius=8, border_color="black",
    hover_color="#707070", font=my_font, text_color="white",
    command=lambda: webbrowser.open("https://www.kaggle.com/datasets/denizkavi1/brain-tumor")
)
kaggle_button.pack(pady=5)



# Main program
window.mainloop()

