# Import stremlit and other libraries
import streamlit as st
import random

# Set up the page
st.set_page_config(
    page_title="Hero Creator",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

# Text input for favorite color
favorite_color = st.text_input('What is your favorite color?')

# Text input for favorite animal
favorite_animal = st.text_input('What is your favorite animal?')

# Text input for a random lucky number
favorite_number = st.text_input('What is your lucky number?')

# create a selecting a superpower from a list
superpower = st.selectbox('What is your superpower?', ['Flying', 'Invisibility', 'Strength', 'Speed', 'Intelligence'])

#concate the text inputs to a super hero name
super_hero_name = f"{favorite_color} {favorite_animal} {superpower} {favorite_number}"

# Display the super hero name
st.write(f'Your super hero name is {super_hero_name}')

#  generate a motto for the super hero
motto = st.text_input('What is your motto?')

# Display the motto
st.write(f'Your motto is {motto}')

# Define list of superhero catchphrases
catchphrases = ["**Justice never sleeps!** – A hero who fights tirelessly for truth and fairness.",
    "**Light in the darkest hour.** – Someone who shines hope when all seems lost.",
    "**Strength is nothing without heart.** – A powerful hero who leads with compassion.",
    "**One hero can change the world.** – Emphasizing the impact of a single act of courage.",
    "**Born to protect, sworn to fight!** – For the unstoppable warrior of justice.",
    "**Fear is temporary, heroism is eternal!** – A motto to embrace bravery.",
    "**The impossible is just a challenge waiting to be conquered.** – A hero who defies limits.",
    "**With great power comes great responsibility.** – A classic lesson in heroism!",
    "**Hope is my weapon, courage is my shield!** – A hero who stands for unwavering faith.",
    "**Evil never wins while heroes stand tall!** – A battle cry against villainy!",
]

# Add a button to "Generate Random Superhero Catchphrase" and show a random quote from a predefined list.
if st.button('Generate Random Superhero Catchphrase'):
    st.write(f'Your catchphrase is {random.choice(catchphrases)}')