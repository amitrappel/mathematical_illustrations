import streamlit as st
from itertools import product
from random import choice
import pandas as pd
import matplotlib.pyplot as plt

st.title('Aaa')
genders = ['m', 'f']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
combos = list(product(genders, days))

N = 10000
history = [((choice(genders), choice(days)), (choice(genders), choice(days))) for _ in range(N)]

def is_two_boys(tup):
    return tup[0][0] == 'm' and tup[1][0] == 'm'

conditional_ps = []

for n in range(100, N, 10):
    conditional_history = [tup for tup in history[:n] if ('m', 'Tuesday') in tup]
    conditional_ps.append(sum([is_two_boys(tup) for tup in conditional_history]) /
        len(conditional_history))

probs = pd.Series(conditional_ps, name='Conditional');
fig, ax = plt.subplots(1, 1)
probs.plot(xlabel='$N$ (Number of families tested)', ylabel='Probability of 2 boys', ax=ax);
st.write(fig)

# print('aaa')
