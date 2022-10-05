import streamlit as st
from itertools import product
from random import choice
import pandas as pd
import matplotlib.pyplot as plt

genders = ['m', 'f']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
combos = list(product(genders, days))

def is_two_boys(tup):
    return tup[0][0] == 'm' and tup[1][0] == 'm'

# @st.cache  # 👈 This function will be cached
def make_data():
    N = 10000

    # Do something really slow in here!
    history = [((choice(genders), choice(days)), (choice(genders), choice(days))) for _ in range(N)]
    for n in range(100, N, 10):
        conditional_history = [tup for tup in history[:n] if ('m', 'Tuesday') in tup]
        conditional_ps = []
        conditional_ps.append(sum([is_two_boys(tup) for tup in conditional_history]) /
                              len(conditional_history))
    return conditional_ps



conditional_ps = make_data()

n = st.slider('N', min_value=10, max_value=10000)  # 👈 this is a widget

probs = pd.Series(conditional_ps, name='Conditional');
fig, ax = plt.subplots(1, 1)
probs[:n].plot(xlabel='$N$ (Number of families tested)', ylabel='Probability of 2 boys', ax=ax);
fig