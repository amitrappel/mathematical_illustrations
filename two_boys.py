import streamlit as st
from itertools import product
from random import choice
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

genders = ['m', 'f']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
combos = list(product(genders, days))

question = '''
A man states that he has two children and that at least one of them is a boy born on a Tuesday. 
What is the probability that the man has two boys?
'''


@st.cache  # 👈 This function will be cached
def make_data(dt):
    N = 10000

    # Do something really slow in here!
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

dt = datetime.now().timestamp()

button_create_data = st.button('Create new random data')
if button_create_data:
    dt_data = datetime.now().timestamp()
    conditional_ps = make_data(dt_data)

    n = st.slider('N', min_value=10, max_value=10000)  # 👈 this is a widget

    try:
        conditional_ps = make_data(dt_data)
    except:
        conditional_ps = make_data(dt)
    probs = pd.Series(conditional_ps, name='Conditional');
    fig, ax = plt.subplots(1, 1)
    probs[:n].plot(xlabel='$N$ (Number of families tested)', ylabel='Probability of 2 boys', ax=ax);
    # plt.show()
    st.write(fig)