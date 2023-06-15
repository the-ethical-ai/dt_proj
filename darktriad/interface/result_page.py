import streamlit as st
import json
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
#from params import DATA_PATH
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
import requests
from darktriad.ml_logic.graphs import draw_map, draw_question_dist_barplots, draw_bubble_plot, plot_results

import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('PORT')

def result_page():
    st.balloons()
    st.header("Your personal result")
    #st.write("Your result")
    #st.markdown(" ")

    finish()
    #st.button("Results",on_click=finish(st.session_state.answers),key="a44")
    # Add content specific to Page 4
    # scores
    # plots
    # interpretation

def placement(x:int):
   if x == -1:
       st.write('You placed below the expected score')
   elif x == 0:
       st.write('You are within the expected range')
   else:
       st.write('You are above the expected score')


def finish():
    answers=st.session_state.answers
    api_url = f'http://localhost:{PORT}/predict?user_answers={answers}'

    #st.write(answers)

    response = requests.get(api_url)
    global preds
    preds = response.json()

    st.divider()

    st.subheader('PSYCHOPATHY')
    placement(preds["Psych_Pred"])
    st.markdown(" ")
    st.subheader('NARCISSISM')
    placement(preds["Narc_Pred"])
    st.markdown(" ")
    st.subheader('MACHIAVELLIANISM')
    placement(preds["Mach_Pred"])

    st.pyplot(plot_results(answers))

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    st.plotly_chart(draw_bubble_plot())

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    question_list = ["M1: It's not wise to tell your secrets.",
                    "M2: I like to use clever manipulation to get my way.",
                    "M3: Whatever it takes, you must get the important people on your side.",
                    "M4: Avoid direct conflict with others because they may be useful in the future.",
                    "M5: It's wise to keep track of information that you can use against people later.",
                    "M6: You should wait for the right time to get back at people.",
                    "M7: There are things you should hide from other people because they don't need to know.",
                    "M8: Make sure your plans benefit you, not others.",
                    "M9: Most people can be manipulated.",
                    "N1: People see me as a natural leader.",
                    "N2: I hate being the center of attention.",
                    "N3: Many group activities tend to be dull without me.",
                    "N4: I know that I am special because everyone keeps telling me so. ",
                    "N5: I like to get acquainted with important people. ",
                    "N6: I feel embarrassed if someone compliments me.",
                    "N7: I have been compared to famous people. ",
                    "N8: I am an average person.",
                    "N9: I insist on getting the respect I deserve.",
                    "P1: I like to get revenge on authorities.",
                    "P2: I avoid dangerous situations.",
                    "P3: Payback needs to be quick and nasty.",
                    "P4: People often say I'm out of control.",
                    "P5: It's true that I can be mean to others. ",
                    "P6: People who mess with me always regret it.",
                    "P7: I have never gotten into trouble with the law.",
                    "P8: I enjoy having sex with people I hardly know.",
                    "P9: I'll say anything to get what I want."]

    question_slider = st.slider("Select Trait Type Question (1: Machiavellianism, 2: Narcissism, 3: Psychopathy)",
                                min_value=1, max_value=3, step=1)

    start_index = (question_slider - 1) * 9
    end_index = start_index + 9
    display_list = question_list[start_index:end_index]

    if question_slider == 1:
        st.write("Here are the Machiavellianism questions:")
        st.write("")
        for string in display_list:
            st.text(string)
    elif question_slider == 2:
        st.write("Here are the Narcissism questions:")
        st.write("")
        for string in display_list:
            st.text(string)
    if question_slider == 3:
        st.write("Here are the Psychopathy questions:")
        st.write("")
        for string in display_list:
            st.text(string)

    st.plotly_chart(draw_map())
