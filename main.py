from tkinter import *
from tkinter import messagebox
import pandas as pd
from pandas.errors import EmptyDataError
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
cards_to_review = {}

# ---------------------------- CREATE FLASH CARDS ------------------------------- #
try:
    df = pd.read_csv('data/words_to_learn.csv')
except (FileNotFoundError, EmptyDataError):
    original_df = pd.read_excel(
        'data/korean_1000_words.xlsx',
        sheet_name="Sheet1",        # First sheet (or use sheet name)
        header=0,            # Row to use as column names
        usecols='A:B'       # Only read specified columns
    ).sample(n=100)
    cards_to_review = original_df.to_dict(orient="records")
else:
    cards_to_review = df.to_dict(orient="records")
finally:
    random.shuffle(cards_to_review)


def start_review():
    global current_card, timer
    start_button.config(state="disabled")
    current_card = random.choice(cards_to_review)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(language_text, text="Korean", fill="black")
    canvas.itemconfig(word_text, text=current_card["Korean"], fill="black")
    timer = window.after(3000, flip_card, current_card)

def next_card():
    window.after_cancel(timer)
    if len(cards_to_review) == 0:
        messagebox.showwarning(title="End of Card Deck", message="There are no more cards!")
        window.destroy()
    else:
        start_review()

def flip_card(card):
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")

def is_known():
    cards_to_review.remove(current_card)
    print(len(cards_to_review))
    data = pd.DataFrame(cards_to_review)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

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
word_text = canvas.create_text(400, 263, text="Review", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Display buttons
x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
check_button.grid(row=1, column=1)

start_button = Button(text="Start", bg="white", font=("Ariel", 20, "bold"), command=start_review)
start_button.grid(row=2, column=0, columnspan=2)


window.mainloop()