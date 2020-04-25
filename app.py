import tkinter as tk
from tkinter import ttk
import tkinter

import random

import requests

def random_pokemon ():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'order': pokemon['order'],
    }

def run ():
    my_pokemon = random_pokemon()

    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight, base_experience, order) ')

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else :
        print('Draw!')

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

myapp = tkinter.Tk()
myapp.title("Pokémon Top Trumps")
myapp.configure(bg='red')

myapp.geometry("250x50")
myapp.iconbitmap(r'C:\Users\star_\PycharmProjects\toptrumps\Pokemon-Ash-PNG-Clipart.ico')

ttk.Style().configure("TButton", relief="flat", background="#ccc", padx=5, pady=5)
btn = ttk.Button(text="Choose Pokémon", command=run)
btn.pack()
myapp.frame = tk.Frame(myapp)
myapp.frame.pack(side="bottom", fill="both", expand=False)
myapp.label = tk.Label(myapp, text="Choose your stat in the Python Console")
myapp.label.pack(in_=myapp.frame)

myapp.mainloop()