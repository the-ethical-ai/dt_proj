'''
Creates the interface (streamlit)
'''
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
import ipdb

start_button_clicked = False

if 'counter' not in st.session_state.keys():
    st.session_state.counter = 0
i = st.session_state.counter

if 'answers' not in st.session_state.keys():
    st.session_state.answers = []
global answers
answers = st.session_state.answers
#
questions = ["It's not wise to tell your secrets.",
             "I like to use clever manipulation to get my way.",
             "Whatever it takes, you must get the important people on your side. ",
             "Avoid direct conflict with others because they may be useful in the future.",
             "It’s wise to keep track of information that you can use against people later.",
             "You should wait for the right time to get back at people. ",
             "There are things you should hide from other people because they don’t need to know.",
             "Make sure your plans benefit you, not others.",
             "Most people can be manipulated.",
             "People see me as a natural leader. ",
             "I hate being the center of attention.",
             "Many group activities tend to be dull without me.",
             "I know that I am special because everyone keeps telling me so. ",
             "I like to get acquainted with important people. ",
             "I feel embarrassed if someone compliments me.",
             "I have been compared to famous people. ",
             "I am an average person.",
             "I insist on getting the respect I deserve.",
             "I like to get revenge on authorities.",
             "I avoid dangerous situations.",
             "Payback needs to be quick and nasty. ",
             "People often say I’m out of control. ",
             "It’s true that I can be mean to others. ",
             "People who mess with me always regret it.",
             "I have never gotten into trouble with the law.",
             "I enjoy having sex with people I hardly know.",
             "I’ll say anything to get what I want.",
             "Are you a US citizen?"]
#
def update(select):
#    #st.button("Submit")
    #if st.button("Submit"):
     #   api_url = f'http://localhost:4000/predict?user_answers={answers}'
        #breakpoint()
        #response = requests.get(api_url)
        #prediction = response.json()
        #breakpoint()
        #pred_1 = prediction["Psych_Pred"]
        #pred_2 = prediction["Narc_Pred"]
        #pred_3 = prediction["Mach_Pred"]

        #st.write(pred_1)

      #  st.write(api_url)
#        #q1 = st.number_input("q1", value=1)
#        #q2 = st.number_input("q2", value=1)
#        #q3 = st.number_input("q3", value=1)
#        #q4 = st.number_input("q4", value=1)
#        #q5 = st.number_input("q5", value=1)
#        #q6 = st.number_input("q6", value=1)
#        #q7 = st.number_input("q7", value=1)
#        #q8 = st.number_input("q8", value=1)
#        #q9 = st.number_input("q9", value=1)
#        #q10 = st.number_input("q10", value=1)
#        #q11 = st.number_input("q11", value=1)
#        #q12 = st.number_input("q12", value=1)
#        #q13 = st.number_input("q13", value=1)
#        #q14 = st.number_input("q14", value=1)
#        #q15 = st.number_input("q15", value=1)
#        #q16 = st.number_input("q16", value=1)
#        #q17 = st.number_input("q17", value=1)
#        #q18 = st.number_input("q18", value=1)
#        #q19 = st.number_input("q19", value=1)
#        #q20 = st.number_input("q20", value=1)
#        #q21 = st.number_input("q21", value=1)
#        #q22 = st.number_input("q22", value=1)
#        #q23 = st.number_input("q23", value=1)
#        #q24 = st.number_input("q24", value=1)
#        #q25 = st.number_input("q25", value=1)
#        #q26 = st.number_input("q26", value=1)
#        #q27 = st.number_input("q27", value=1)
#        #q28 = st.number_input("q28", value=1)
#        #params = dict(q1=q1,
#        #              q2=q2,
#        #              q3=q3,
#        #              q4=q4,
#        #              q5=q5,
#        #              q6=q6,
#        #              q7=q7,
#        #              q8=q8,
#        #              q9=q9,
#        #              q10=q10,
#        #              q11=q11,
#        #              q12=q12,
#        #              q13=q13,
#        #              q14=q14,
#        #              q15=q15,
#        #              q16=q16,
#        #              q17=q17,
#        #              q18=q18,
#        #              q19=q19,
#        #              q20=q20,
#        #              q21=q21,
#        #              q22=q22,
#        #              q23=q23,
#        #              q24=q24,
#        #              q25=q25,
#        #              q26=q26,
#        #              q27=q27,
#        #              q28=q28
#        params = {'user_answers': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]}
#        api_url = 'http://localhost:4000/predict'
#        #breakpoint()
#        response = requests.get(api_url, params=params)
#        prediction = response.json()
#        #breakpoint()
#        pred_1 = prediction["Psych_Pred"]
#        pred_2 = prediction["Narc_Pred"]
#        pred_3 = prediction["Mach_Pred"]
#        pred = prediction['sample']
#        st.header(f'Prediction: {pred_3}')
    #else:
    answers.append(int(select))
    global i
    i += 1
    st.session_state.answers = answers
    st.session_state.counter = i

global preds

def placement(x:int):
    if x == -1:
        st.write('You placed below the expected score')
    elif x == 0:
        st.write('You are within the expected range')
    else:
        st.write('You are above the expected score')

def finish(select):
        api_url = f'http://localhost:4000/predict?user_answers={answers}'
        #breakpoint()
        #response = requests.get(api_url)
        #prediction = response.json()
        #breakpoint()
        #pred_1 = prediction["Psych_Pred"]
        #pred_2 = prediction["Narc_Pred"]
        #pred_3 = prediction["Mach_Pred"]

        #st.write(pred_1)

        #st.write(api_url)
        response = requests.get(api_url)
        global preds
        preds = response.json()
        #preds = st.session_state.preds
        #st.write(preds)

        st.write('PSYCHOPATHY')
        placement(preds["Psych_Pred"])
        st.write('NARCISSISM')
        placement(preds["Narc_Pred"])
        st.write('MACHIAVELLIANISM')
        placement(preds["Mach_Pred"])


#
def show_q_a(i):#
    select = st.selectbox(
        f"{i+1})  {questions[i]}",
        ('Select a number', '1', '2', '3', '4', '5')
    )
    if select != 'Select a number':
        st.write('You selected:', select)
        if (i < 27):
            name = 'Continue'
            st.button(name, on_click=update, args=select,key='a43')
        else:
            name = 'Submit'
            st.button(name, on_click=finish, args=select,key='a43')


#
#
#
#
#
#
#def show_plots():
#    df = pd.read_csv(DATA_PATH, delimiter = '\t')
#    #df.head()#

#    df_after_preprocess = preprocess(df)
#    df_after_featureng = feature_engineering(df_after_preprocess)#

#    #Avearges
#    #df_after_featureng
#    df_average = df_after_featureng.mean(axis=0)
#    df_average_traits = df_average.iloc[:27]
#    average_df = pd.DataFrame(df_average_traits)#

#    fig = px.bar(average_df,title="Average score for each question")
#    fig.update_layout(xaxis_title="Average scores", yaxis_title="Questions")
#    fig.update_traces(marker=dict(size=12,
#                                line=dict(width=2,
#                                            color='DarkSlateGrey')),
#                                            selector=dict(mode='markers'))#

#    # Display the bar chart in Streamlit
#    st.plotly_chart(fig)#

#    fig2 = go.Figure(go.Indicator(
#        mode = "number+gauge+delta",
#        gauge = {'shape': "bullet"},
#        delta = {'reference': 4.3},
#        domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
#        value = 5,
#        title = {'text': "Average score"}))#

#    st.plotly_chart(fig2)#

#    fig3 = go.Figure(go.Indicator(
#        mode="number+delta",
#        value=3,
#        number={'suffix': "", 'prefix': "Your score: ", 'font': {'size': 52}},
#        delta={'position': "bottom", 'reference': 4},
#        title={'text': " average score for question"}))#

#    # Update layout
#    fig3.update_layout(paper_bgcolor="lightgray",)
#    st.plotly_chart(fig3)
#
#
def show_initial_text():
    if not start_button_clicked:
        st.subheader("Introducing the Psychopathy, Narcissism, Machiavellianism Assessment: Discover Your Personality Score!")
        links = "[Machiavellianism](https://en.wikipedia.org/wiki/Machiavellianism_(psychology))&nbsp;&nbsp;[Narcissism](https://en.wikipedia.org/wiki/Narcissism) &nbsp; &nbsp;[Psychopathy](https://en.wikipedia.org/wiki/Psychopathy)"
        st.markdown(f"""
            - Uncover intriguing insights about your personality with just a few clicks!
            - Not sure what they are? &nbsp; {links}
        """)

        st.markdown("""
            Our interactive web interface offers a quick and engaging way to assess your Machiavellian tendencies. No lengthy explanations or excessive reading required!
            Simply answer 28 questions by selecting a score from 1 to 5. It's as easy as giving your honest opinion.
        """)

        st.markdown("1 - Strongly Disagree &nbsp;&nbsp; 2 - Disagree &nbsp;&nbsp;  3 - Neutral &nbsp;&nbsp;  4 - Agree &nbsp;&nbsp;  5 - Strongly Agree")

        st.markdown("Trust your instincts for the most accurate results.")
        st.markdown("Once you've finished answering all the questions, we'll generate your personalized Machiavellianism/Psychopathy/Narcissism score and compare it to the average score of other 2 traits.")
        st.markdown("Curious to see where you stand?")
        st.markdown("But wait, there's more! We'll also provide you with a predicted Machiavellianism/Psychopathy/Narcissism score based on your responses. Unleash your inner strategist and uncover the hidden aspects of your personality.")
        st.markdown("Ready to dive in? Begin the assessment now and unlock a fascinating glimpse into your Machiavellianism/Psychopathy/Narcissism score. Let's get started!")

        st.write(
            "<style>div.stButton > button {display: block; margin: 0 auto;}</style>",
            unsafe_allow_html=True
        )
    return True

show_initial_text()
show_q_a(i)
#show_plots()
#st.write('answers', answers)







#params = {'user_answers': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]}
#api_url = f'http://localhost:4000/predict?user_answers={answers}'
#breakpoint()
#response = requests.get(api_url)
#prediction = response.json()
#breakpoint()
#pred_1 = prediction["Psych_Pred"]
#pred_2 = prediction["Narc_Pred"]
#pred_3 = prediction["Mach_Pred"]

#st.write(pred_1)
#st.write(api_url)
