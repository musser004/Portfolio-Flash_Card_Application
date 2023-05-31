from tkinter import *
from random import randint
import pandas

# Constants

BACKGROUND_COLOR = "#DDE6ED"
FONT_NAME = "Arial"

# Pulling in data with pandas, then formatting via dictionary/list comprehension

dict1 = pandas.read_csv("./data/spanish_words.csv")
core_dict = {row.Spanish: row.English for (index, row) in dict1.iterrows()}
core_list = [x for x in core_dict]

# Function to pick a word from the list and display it. Word printed to console


def choose_word():
    global card_word, side
    side = 0
    card_word = core_list[randint(0, len(core_list))]
    print(card_word)
    canvas.itemconfig(background, image=card_front_img)
    canvas.itemconfig(title_text, text="Spanish", fill="#DDE6ED")
    canvas.itemconfig(word_text, text=card_word, fill="#DDE6ED")

# Function to flip the card and display the English translation or to flip it back and display the original Spanish word


def flip_card():
    global side
    if side == 0 or side % 2 == 0:
        card_answer = core_dict[card_word]
        canvas.itemconfig(background, image=card_back_img)
        canvas.itemconfig(title_text, text="English", fill="#27374D")
        canvas.itemconfig(word_text, text=card_answer, fill="#27374D")
        side += 1
    elif side % 2 != 0:
        canvas.itemconfig(background, image=card_front_img)
        canvas.itemconfig(title_text, text="Spanish", fill="#DDE6ED")
        canvas.itemconfig(word_text, text=card_word, fill="#DDE6ED")
        side += 1

# Function to remove card from the list, then pick another word to restart the process


def correct_answer():
    core_list.remove(card_word)
    choose_word()

# TKinter GUI initial setup


window = Tk()
window.title("Spanish Frequency Dictionary - Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=1000, height=650, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Pulling in image files, then setting up images/text

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
check_img = PhotoImage(file="./images/check_mark.png")
flip_img = PhotoImage(file="./images/flip_mark.png")
background = canvas.create_image(500, 325, image=card_front_img)
title_text = canvas.create_text(500, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(500, 263, text="", font=(FONT_NAME, 60, "bold"))

# Adding functionality/buttons to GUI

right_button = Button(image=check_img, highlightthickness=0, command=correct_answer)
right_button.grid(column=1, row=2)
wrong_button = Button(image=flip_img, highlightthickness=0, command=flip_card)
wrong_button.grid(column=0, row=2)

# choose_word function is called to kickstart the process, mainloop to run TKinter window

choose_word()
window.mainloop()
