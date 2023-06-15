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
    #st.write(answers)
    api_url = f'http://localhost:5000/predict?user_answers={answers}'
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
       
    st.pyplot(plot_results())

    st.plotly_chart(draw_bubble_plot())

    st.plotly_chart(draw_map())

    