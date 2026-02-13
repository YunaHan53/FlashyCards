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
current_card = {}

def start_review():
    global current_card, timer
    current_card = random.choice(vocab_dictionary)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(language_text, text="Korean", fill="black")
    canvas.itemconfig(word_text, text=current_card["Korean"], fill="black")
    timer = window.after(3000, flip_card, current_card)

def next_card():
    window.after_cancel(timer)
    start_review()

def flip_card(card):
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy - the Interactive Flash Card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Display card
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
# Display card text
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Display buttons
x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
check_button.grid(row=1, column=1)

start_button = Button(text="Start",bg="white", font=("Ariel", 20, "bold"), command=start_review)
start_button.grid(row=2, column=0, columnspan=2)


window.mainloop()