from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy - the Interactive Flash Card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Display card
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Korean", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="하다", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# card_back_img = PhotoImage(file="images/card_back.png")

# Display buttons
x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, bg=BACKGROUND_COLOR)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR)
check_button.grid(row=1, column=1)


window.mainloop()