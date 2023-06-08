'''
Creates the interface (streamlit)
'''
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from params import DATA_PATH
from preprocess import preprocess
from Feat_engine import feature_engineering

start_button_clicked = False

if 'counter' not in st.session_state.keys():
    st.session_state.counter = 0
i = st.session_state.counter

if 'answers' not in st.session_state.keys():
    st.session_state.answers = []
answers = st.session_state.answers

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

def update(select):
        answers.append(int(select))
        global i
        i += 1
        st.session_state.answers = answers
        st.session_state.counter = i

def show_q_a(i):

    select = st.selectbox(
        f"{i+1})  {questions[i]}",
        ('Select a number', '1', '2', '3', '4', '5')
    )
    if select != 'Select a number':
        st.write('You selected:', select)
        name = 'Continue' if i < 27 else 'Submit'
        st.button(name, on_click=update, args=select)


def show_plots():
    df = pd.read_csv(DATA_PATH, delimiter = '\t')
    #df.head()

    df_after_preprocess = preprocess(df)
    df_after_featureng = feature_engineering(df_after_preprocess)

    #Avearges
    #df_after_featureng
    df_average = df_after_featureng.mean(axis=0)
    df_average_traits = df_average.iloc[:27]
    average_df = pd.DataFrame(df_average_traits)

    fig = px.bar(average_df,title="Average score for each question")
    fig.update_layout(xaxis_title="Average scores", yaxis_title="Questions")
    fig.update_traces(marker=dict(size=12,
                                line=dict(width=2,
                                            color='DarkSlateGrey')),
                                            selector=dict(mode='markers'))

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)

    fig2 = go.Figure(go.Indicator(
        mode = "number+gauge+delta",
        gauge = {'shape': "bullet"},
        delta = {'reference': 4.3},
        domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
        value = 5,
        title = {'text': "Average score"}))

    st.plotly_chart(fig2)

    fig3 = go.Figure(go.Indicator(
        mode="number+delta",
        value=3,
        number={'suffix': "", 'prefix': "Your score: ", 'font': {'size': 52}},
        delta={'position': "bottom", 'reference': 4},
        title={'text': " average score for question"}))

    # Update layout
    fig3.update_layout(paper_bgcolor="lightgray",)
    st.plotly_chart(fig3)


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