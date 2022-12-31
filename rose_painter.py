import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Parametrization taken from here: https://en.wikipedia.org/wiki/Rose_(mathematics)

question = 'Please choose k'
st.write(question)
k = st.slider('k', min_value=1, max_value=20, value=4)  # 👈 this is a widget

t = np.linspace(1e-3, k*np.pi, 12345)
x = np.cos(k*t) * np.cos(t)
y = np.cos(k*t) * np.sin(t)

fig, ax = plt.subplots(1, 1)
ax.set(xlim=(-2, 2), ylim=(-2, 2))
ax.scatter(x, y, s=3, c='red')
st.write(fig)
