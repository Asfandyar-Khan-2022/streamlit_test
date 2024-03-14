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
						pokemon['types']['type']['name'])
	except:
		return 'Error', np.NAN, np.NAN, np.NAN
	

pokemon_number = st.slider("Pick a pokemon",
						   min_value=1,
						   max_value=150
						   )




d = {'name': [get_details(pokemon_number)[0]], 'height': [get_details(pokemon_number)[1]], 'weight': [get_details(pokemon_number)[2]], 'moves': [get_details(pokemon_number)[3]], 'types': [get_details(pokemon_number)[6]]}

df = pd.DataFrame(d)

print(df)



name, height, weight, moves, image, cries = get_details(pokemon_number)

# df = pd.DataFrame(name, height)

# st.write(f'Name: {name}')
# st.write(f'Height: {height}')
# st.write(f'Weight: {weight}')
# st.write(f'Move Count: {moves}')
st.table(df)
st.audio(cries)
st.image(image)

