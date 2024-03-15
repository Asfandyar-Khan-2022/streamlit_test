import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import requests
import numpy as np

st.title("Pokemon Explorer!")

def get_details(poke_number):
	try:
		url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
		response = requests.get(url)
		pokemon = response.json()
		return (pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']),
		                pokemon['sprites']['other']['official-artwork']['front_default'], 
						pokemon['cries']['latest'],
						pokemon['types'][0]['type']['name'])
	except:
		return 'Error', np.NAN, np.NAN, np.NAN


pokemon_number = st.slider("Pick a pokemon",
						   min_value=1,
						   max_value=150
						   )



d = {'name': [get_details(pokemon_number)[0]], 'height': [get_details(pokemon_number)[1]], 'weight': [get_details(pokemon_number)[2]], 'moves': [get_details(pokemon_number)[3]], 'type': [get_details(pokemon_number)[6]]}

df = pd.DataFrame(d)

print(df)

name, height, weight, moves, image, cries, type = get_details(pokemon_number)

pokemon_colours = {
    "normal": "#A8A77A",
    "fire": "#EE8130",
    "water": "#6390F0",
    "electric": "#F7D02C",
    "grass": "#7AC74C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#735797",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD",
    "stellar": "#FFD700"
}

print(pokemon_colours[type])

df_height = pd.DataFrame({'Height': [5, height, 7], 'Column': ['Growlithe', name, 'Bulbasaur']})
df_height.set_index('Column', inplace=True)
df_height.index.name = 'Name'

st.table(df)
st.audio(cries)
st.image(image)
st.bar_chart(df_height, color=pokemon_colours[type])
