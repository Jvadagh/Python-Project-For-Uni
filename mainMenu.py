from pathlib import Path
from tkinter import *

import Multyplayer

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("200x250")
window.configure(bg="#9E9E9E")

canvas = Canvas(
    window,
    bg="#9E9E9E",
    height=250,
    width=200,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=15.0,
    y=183.0,
    width=170.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open(Multyplayer),
    relief="flat"
)
button_2.place(
    x=15.0,
    y=131.0,
    width=170.0,
    height=26.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_3 clicked'),
    relief="flat"
)
button_3.place(
    x=17.0,
    y=80.0,
    width=170.0,
    height=26.0
)

canvas.create_text(
    42.0,
    17.0,
    anchor="nw",
    text="TIC TAC TOE",
    fill="#FFFFFF",
    font=("Lato Bold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
