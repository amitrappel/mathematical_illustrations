import streamlit as st
from itertools import product
from random import choice
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

genders = ['m', 'f']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
combos = list(product(genders, days))
N = 20000

question = '''
A man states that he has two children and that at least one of them is a boy born on a Tuesday. 
What is the probability that the man has two boys?
'''


@st.cache  # 👈 This function will be cached
def make_data(dt):
    history = [((choice(genders), choice(days)), (choice(genders), choice(days))) for _ in range(N)]
    conditional_ps = []
    for n in range(100, N, 1):
        conditional_history = [tup for tup in history[:n] if ('m', 'Tuesday') in tup]
        conditional_ps.append(sum([is_two_boys(tup) for tup in conditional_history]) /
                              len(conditional_history))
    return conditional_ps


def is_two_boys(tup):
    return tup[0][0] == 'm' and tup[1][0] == 'm'

### Page

st.write(question)

dt = int(datetime.now().timestamp() / 10000)
conditional_ps = make_data(dt)

button_create_data = st.button('Create new random data')
if button_create_data:
    dt_data = datetime.now().timestamp()
    conditional_ps = make_data(dt_data)

n = st.slider('N', min_value=1, max_value=N, value=100)  # 👈 this is a widget

probs = pd.Series(conditional_ps, name='Conditional');
fig, ax = plt.subplots(1, 1)
ax.set(xlim=(1, n), ylim=(0.3, 0.7))
ax.axhline(13/27, color='red', lw=3)
ax.text(x=0.9*n, y=0.45, s=r'$\frac{13}{27}$', fontsize=14, style='oblique')
probs[:n].plot(xlabel='$N$ (Number of families tested', ylabel='Probability of 2 boys', ax=ax);
st.write(fig)
