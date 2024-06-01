import streamlit as st
import pygame
from music import *
import numpy as np
import pandas as pd
import time

pygame.init()

st.header(":musical_note: Music Visualizer :musical_note:", divider=True)

st.write(" ")
st.write(" ")

st.subheader("Upload your music file")

file = st.file_uploader("Add file")
if file is not None:
   
    placeholder = st.empty()
    placeholder.audio(file)

    loading_text = st.empty()
    loading_text.text("Loading graph ...")

    chat = get_characteristics(file)

    loading_text.empty()
else:
    st.write("No files uploaded.")


st.write(" ")
st.write(" ")

# Create a placeholder for the bar chart
chart_title = st.empty()
chart_placeholder = st.empty()
chart_subtitle = st.empty()

try:
    for i in range(len(chat[0])):
        chart_data = pd.DataFrame(
            {
                "time": chat[0][:i+1],  # length
                "pitch": chat[1][:i+1],  # pitch
                "frequency": chat[2][:i+1],  # frequency
            }
        )

        is_loading = False

        # Update the bar chart in the placeholder
        chart_title.write(f"#### Bar Chart Showing Frequency and Pitch over a Duration of a Song")
        chart_subtitle.write(f"#### (Second {i+1}/{len(chat[0])})")
        chart_placeholder.bar_chart(chart_data, x="time", y=["pitch", "frequency"], color=["#FF0000", "#0000FF"])

        # Wait for 0.1 seconds
        time.sleep(0.1)


except:
    pass


