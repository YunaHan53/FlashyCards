from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CREATE FLASH CARDS ------------------------------- #
df = pd.read_excel(
    'data/korean_1000_words.xlsx',
    sheet_name="Sheet1",        # First sheet (or use sheet name)
    header=0,            # Row to use as column names
    usecols='A:B',       # Only read specified columns
    nrows=100            # Only read first 100 rows
)
vocab_dictionary = df.to_dict(orient="records")

def next_card():
    current_card = random.choice(vocab_dictionary)
    canvas.itemconfig(language_text, text="Korean")
    canvas.itemconfig(word_text, text=current_card["Korean"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy - the Interactive Flash Card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Display card
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# card_back_img = PhotoImage(file="images/card_back.png")

# Display buttons
x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()